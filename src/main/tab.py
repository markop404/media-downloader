# Media Downloader - Web video/audio downloader
# Copyright (C) 2024  Marko Pejić

# This file is part of Media Downloader

# Media Downloader is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Media Downloader is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import threading
import time
import os

from PySide6.QtWidgets import QMessageBox, QWidget, QFileDialog
from PySide6.QtCore import QCoreApplication, QUrl, QDir, QStandardPaths, QSize
from PySide6.QtGui import QPixmap, QKeySequence, QShortcut

import utils, ytdlp_helpers
from .settings import Settings
from ui import Ui_Tab


class Tab(QWidget):
    def __init__(self, parent, pretty_tab_number):
        super().__init__()
        self.setup_ui()
        self.SETTINGS = [
            {
                "name": "download-format",
                "set-value-func": self.ui.formatComboBox.setCurrentText,
                "get-value-func": self.ui.formatComboBox.currentText,
            },
            {
                "name": "crop-thumbnails",
                "set-value-func": self.ui.cropThumbnailsCheckBox.setChecked,
                "get-value-func": self.ui.cropThumbnailsCheckBox.isChecked,
            },
            {
                "name": "embed-subtitles",
                "set-value-func": self.ui.embedSubtitlesCheckBox.setChecked,
                "get-value-func": self.ui.embedSubtitlesCheckBox.isChecked,
            },
        ]
        self.settings_manager = Settings()
        self.setup_vars(parent, pretty_tab_number)
        self.load_settings()
        self.update_download_directory_indicators()
        self.setup_filedialog()
        self.event_invoker = utils.Invoker()
        self.connect_signals_and_slots()
        self.update_qualities(clear=True)


    def load_settings(self):
        if self.settings_manager.load_setting("remember-tab-settings"):
            for setting in self.SETTINGS:
                value = self.settings_manager.load_setting(setting["name"])
                if value != None:
                    setting["set-value-func"](value)
            
            if download_dir := self.settings_manager.load_setting("download-dir"):
                if os.path.exists(download_dir):
                    self.download_directory = download_dir
                    self.update_download_directory_indicators()
        else:
            for setting in self.SETTINGS:
                value = self.settings_manager.DEFAULT_SETTINGS[setting["name"]]["value"]
                setting["set-value-func"](value)
    

    def update_settings(self):
        self.update_qualities(placeholder_only=True)
    

    def save_settings(self):
        for setting in self.SETTINGS:
            self.settings_manager.setValue(setting["name"], setting["get-value-func"]())
        
        self.settings_manager.setValue("download-dir", self.download_directory)


    def setup_ui(self):
        self.ui = Ui_Tab()
        self.ui.setupUi(self)

        QShortcut(QKeySequence("Alt+f"), self).activated.connect(
            lambda:
                self.show_combobox_popup(
                    self.ui.formatComboBox,
                )
        )
        QShortcut(QKeySequence("Alt+q"), self).activated.connect(
            lambda:
                self.show_combobox_popup(
                    self.ui.qualityComboBox,
                )
        )
        QShortcut(QKeySequence("Alt+s"), self).activated.connect(
            lambda:
                self.show_combobox_popup(
                    self.ui.subtitlesComboBox,
                )
        )

        self.ui.formatComboBox.replace_all_items(Settings.CONSTANT_SETTTINGS["formats"])


    def setup_vars(self, parent, pretty_tab_number):
        self.parent = parent
        self.pretty_tab_number = pretty_tab_number
        self.download_directory = QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)
        self.thread_running = False
        self.cancel_progress = False
        self.user_answer = False
        self.subtitles = None
        self.qualities = None
    

    def setup_filedialog(self):
        self.file_dialog = QFileDialog(self)
        self.file_dialog.setFileMode(QFileDialog.Directory)
        self.file_dialog.setDirectory(self.download_directory)
    

    def connect_signals_and_slots(self):
        self.ui.dataPullButton.clicked.connect(self.start_update_info)
        self.ui.downloadButton.clicked.connect(self.start_download)
        self.ui.setDownloadFolderButton.clicked.connect(self.set_download_location)
        self.ui.formatComboBox.currentTextChanged.connect(lambda: self.update_qualities())
        self.ui.plainTextEdit.textChanged.connect(self.on_text_change)


    def prep_thread_start(self):
        self.thread_running = True

        self.ui.plainTextEdit.cleanup()
        urls = self.ui.plainTextEdit.get_lines()
        self.update_status_indicators(
            situation="extracting_urls",
            progress=(1, len(urls)),
            percentage=0
        )

        self.ui.plainTextEdit.setReadOnly(True)
        self.ui.qualityComboBox.setEnabled(False)
        self.ui.subtitlesComboBox.setEnabled(False)

        return urls
    

    def prep_thread_exit(self, situation=None, percentage=0):
        self.thread_running = False
        self.cancel_progress = False
        
        to_run = [
            lambda: self.restore_widgets_to_normal(),
            lambda: self.update_qualities(),
            lambda: self.update_subtitles(),
            lambda: self.update_status_indicators(situation, percentage=percentage),
        ]
        for func in to_run:
            self.run_in_gui_thread(func)
    
    
    def start_update_info(self):
        if not self.ui.plainTextEdit.toPlainText():
            return

        if not self.thread_running:
            urls = self.prep_thread_start()
            data_pull_button_text = (
                self.settings_manager.CONSTANT_SETTTINGS["button_text"]["refresh"]["secondary"]
            )
            self.ui.dataPullButton.setText(data_pull_button_text)
            self.ui.downloadButton.setEnabled(False)
            threading.Thread(target=lambda: self.update_info(urls), daemon=True).start()
        elif self.thread_running:
            self.cancel_progress = True
            self.ui.dataPullButton.setEnabled(False)
            self.update_status_indicators("cancelling_data_pull")


    def start_download(self):
        if not self.ui.plainTextEdit.toPlainText():
            return

        if not self.thread_running:
            urls = self.prep_thread_start()
            download_button_text = (
                self.settings_manager.CONSTANT_SETTTINGS["button_text"]["download"]["secondary"]
            )
            self.ui.downloadButton.setText(download_button_text)
            self.ui.dataPullButton.setEnabled(False)
            self.ui.formatComboBox.setEnabled(False)
            self.ui.setDownloadFolderButton.setEnabled(False)
            self.ui.embedSubtitlesCheckBox.setEnabled(False)
            self.ui.cropThumbnailsCheckBox.setEnabled(False)
            threading.Thread(target=lambda: self.download(urls), daemon=True).start()
        else:
            self.cancel_progress = True
            self.ui.downloadButton.setEnabled(False)
            self.update_status_indicators(situation="cancelling_download")


    def update_info(self, urls):
        try:
            urls, failed_urls1, exit_status, errors = ytdlp_helpers.extract_urls(
                urls,
                on_progress=lambda 
                    processed_url_count,
                    total_url_count,
                    situation="extracting_urls":
                        self.url_extraction_progress(
                            situation,
                            processed_url_count,
                            total_url_count
                        ),
            )
        except SystemExit:
            self.prep_thread_exit("data_pull_cancelled")
            return
        except BaseException as e:
            self.prep_thread_exit("data_pull_failed")
            print(e)
            return
        if not exit_status:
            self.prep_thread_exit("no_internet")
            return
        elif not urls and failed_urls1:
            self.handle_invalid_url_warning(failed_urls1, error_type="data_pull")
            self.prep_thread_exit("data_pull_failed")
            return

        self.run_in_gui_thread(
            lambda:
                self.update_status_indicators(
                    situation="pulling_data",
                    progress=(1, len(urls)),
                    percentage=0,
                )
        )
        
        try:
            data, failed_urls2, exit_status, errors = ytdlp_helpers.extract_data(
                urls,
                on_progress=lambda
                    processed_url_count,
                    total_url_count,
                    situation="pulling_data":
                        self.url_extraction_progress(
                            situation,
                            processed_url_count,
                            total_url_count
                        ),
            )
        except SystemExit:
            self.prep_thread_exit("data_pull_cancelled")
            return
        except BaseException as e:
            print(e)
            self.prep_thread_exit("data_pull_failed")
            return
        failed_urls = failed_urls1.union(failed_urls2)
        if not exit_status:
            self.prep_thread_exit("no_internet")
            return
        elif failed_urls and not data:
            self.handle_invalid_url_warning(failed_urls, error_type="data_pull")
            self.prep_thread_exit("data_pull_failed")
            return
        
        if failed_urls and data:
            self.handle_invalid_url_warning(failed_urls, error_type="data_pull")

        try:
            self.qualities, self.subtitles = ytdlp_helpers.extract_basic_info(data)
        except BaseException as e:
            print(e)
            self.prep_thread_exit("data_pull_failed")
            return
        
        self.prep_thread_exit("data_pull_finished", percentage=100)


    def download(self, urls):
        try:
            urls, failed_urls1, exit_status, errors = ytdlp_helpers.extract_urls(
                urls,
                lambda
                    processed_url_count,
                    total_url_count,
                    situation="extracting_urls":
                        self.url_extraction_progress(
                            situation,
                            processed_url_count,
                            total_url_count
                        )
            )
        except SystemExit:
            self.prep_thread_exit("download_cancelled")
            return
        except BaseException as e:
            print(e)
            self.prep_thread_exit("download_failed")
            return

        if not exit_status:
            self.prep_thread_exit("no_internet")
            return
        elif not urls and failed_urls1:
            self.handle_invalid_url_warning(failed_urls1)
            self.prep_thread_exit("download_failed")
            return

        self.run_in_gui_thread(
            lambda:
                self.update_status_indicators(
                    situation="downloading",
                    progress=(1, len(urls)),
                    percentage=0,
                )
        )

        file_type, quality, subtitle_lang = self.get_download_opts()

        try:
            failed_urls2, exit_status, errors = ytdlp_helpers.download(
                urls=urls,
                subtitle_lang=subtitle_lang,
                on_progress=self.download_progress,
                download_location=self.download_directory,
                file_type=file_type,
                quality=quality,
                postprocessor_progress=self.postprocess_progress,
                on_url_progress=self.url_download_progress,
                embed_subtitles=self.ui.embedSubtitlesCheckBox.isChecked(),
                crop_thumbnails=self.ui.cropThumbnailsCheckBox.isChecked(),
            )
        except SystemExit:
            self.prep_thread_exit("download_cancelled")
            return
        except BaseException as e:
            print(e)
            self.prep_thread_exit("download_failed")
            return
        failed_urls = failed_urls1.union(failed_urls2)
        if not exit_status:
            self.prep_thread_exit("no_internet")
            return
        elif failed_urls == urls:
            self.handle_invalid_url_warning(failed_urls)
            self.prep_thread_exit("download_failed")
            return

        if failed_urls:
            self.handle_invalid_url_warning(failed_urls)
        self.prep_thread_exit("download_finished", 100)


    def display_invalid_url_warning(self, text):
        answer = QMessageBox.warning(
            self,
            self.settings_manager.CONSTANT_SETTTINGS["window_titles"]["error"].replace(
                "<pretty_tab_number>",
                str(self.pretty_tab_number)
            ),
            text,
            buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            defaultButton=QMessageBox.StandardButton.Yes,
        )
        if answer == QMessageBox.Yes:
            self.user_answer = True
        else:
            self.user_answer = False

        self.parent.popup_window_running = False
    

    def handle_invalid_url_warning(self, urls, error_type="download"):
        if error_type == "download":
            beggining_text = f"The following {len(urls)} URLs couldn't be downloaded:"
        else:
            beggining_text = f"The following {len(urls)} URLs are invalid:"

        url_list_text = "<ul>"
        for url in urls:
            url_list_text += f"<li><a href=\"{url}\">{url}</a></li>"
        url_list_text += "</ul>"

        ending_text = "Remove them from the text entry?"
        text = beggining_text + url_list_text + ending_text

        while self.parent.popup_window_running:
            time.sleep(0.01)

        self.parent.popup_window_running = True
        self.run_in_gui_thread(lambda: self.display_invalid_url_warning(text))

        while self.parent.popup_window_running:
            time.sleep(0.01)

        if self.user_answer:
            self.run_in_gui_thread(lambda: self.ui.plainTextEdit.remove_lines(urls))


    def on_text_change(self):
        if not self.ui.plainTextEdit.setting_text and not self.thread_running:
            self.update_status_indicators()
            self.update_qualities(clear=True)
            self.update_subtitles(clear=True)


    def show_combobox_popup(self, combobox):
        if not self.thread_running:
            combobox.showPopup()


    def run_in_gui_thread(self, fn):
        QCoreApplication.postEvent(
            self.event_invoker,
            utils.InvokeEvent(fn)
        )


    def set_download_location(self):
        if self.file_dialog.exec():
            self.download_directory = self.file_dialog.selectedFiles()[0]
            self.update_download_directory_indicators()


    def url_extraction_progress(self, situation, processed_url_count, total_url_count):
        if self.cancel_progress:
            raise SystemExit
        if processed_url_count + 1 <= total_url_count:
            processed_url_count += 1

        try:
            percentage = int(((processed_url_count - 1) / total_url_count) * 100)
        except:
            return

        self.run_in_gui_thread(
            lambda:
                self.update_status_indicators(
                    situation=situation,
                    progress=(processed_url_count, total_url_count),
                    percentage=percentage,
                )
        )


    def download_progress(self, data, processed_url_count, total_url_count):
        if self.cancel_progress:
            raise SystemExit
        percentage = None
    
        if data["status"] == "downloading":            
            if "downloaded_bytes" in data and "total_bytes" in data:
                if data["downloaded_bytes"] and data["total_bytes"]:
                    try:
                        percentage = int((data["downloaded_bytes"] / data["total_bytes"]) * 100)
                    except:
                        percentage = None
            elif "fragment_index" in data and "fragment_count" in data:
                if data["fragment_index"] and data["fragment_count"]:
                    try:
                        percentage = int((data["fragment_index"] / data["fragment_count"]) * 100)
                    except:
                        percentage = None
        
        if processed_url_count + 1 <= total_url_count:
            self.run_in_gui_thread(
                lambda:
                    self.update_status_indicators(
                        situation="downloading",
                        progress=(processed_url_count + 1, total_url_count),
                        percentage=percentage,
                    )
            )


    def url_download_progress(self, url, processed_url_count, total_url_count):
        if self.cancel_progress:
            raise SystemExit

        if processed_url_count < total_url_count:
            percentage = 0
        else:
            percentage = None
        if processed_url_count + 1 <= total_url_count:
            self.run_in_gui_thread(
                lambda:
                    self.update_status_indicators(
                        situation="downloading",
                        progress=(processed_url_count + 1, total_url_count),
                        percentage=percentage,
                    )
            )
        if self.settings_manager.load_setting("remove-downloaded-urls"):
            self.ui.plainTextEdit.remove_lines([url])
    

    def postprocess_progress(self, data, processed_url_count, total_url_count):
        if self.cancel_progress:
            raise SystemExit
        self.run_in_gui_thread(
            lambda:
                self.update_status_indicators(
                    situation="converting",
                    progress=(processed_url_count + 1, total_url_count),
                    percentage=100,
                )
        )


    def get_download_opts(self):
        file_type = self.ui.formatComboBox.currentData()
        subtitles = self.ui.subtitlesComboBox.currentData()
        selected_quality = self.ui.qualityComboBox.currentData()
        
        if selected_quality:
            quality = selected_quality
        else:
            if file_type == "mp4":
                quality = self.settings_manager.load_setting("preferred-resolution")
            elif file_type == "mp3":
                quality = self.settings_manager.load_setting("preferred-bitrate")
        
        return file_type, selected_quality, subtitles


    def update_qualities(self, clear=False, placeholder_only=False):
        _format = self.ui.formatComboBox.currentData()

        if _format == "mp4":
            placeholder_text = (
                Settings.CONSTANT_SETTTINGS["preferred-resolutions"]
                [self.settings_manager.load_setting("preferred-resolution")]
            )
        elif _format == "mp3":
            placeholder_text = (
                Settings.CONSTANT_SETTTINGS["preferred-bitrates"]
                [self.settings_manager.load_setting("preferred-bitrate")]
            )
        self.ui.qualityComboBox.setPlaceholderText(placeholder_text)
        
        if not placeholder_only:
            if clear:
                self.qualities = None
                self.ui.qualityComboBox.replace_all_items()
                return
            elif isinstance(self.qualities, dict):
                combobox_qualities = {}
                suffix = ""
                preferred_quality = 0
                default_quality = 0

                if _format == "mp4":
                    suffix = "p"
                    qualities = self.qualities["resolutions"]
                    preferred_quality = self.settings_manager.load_setting("preferred-resolution")
                elif _format == "mp3":
                    suffix = " kbps"
                    qualities = self.qualities["bitrates"]
                    preferred_quality = self.settings_manager.load_setting("preferred-bitrate")

                for repetition, quality in enumerate(sorted(qualities, reverse=True)):
                    combobox_qualities[quality] = str(quality) + suffix
                    if not default_quality and quality <= preferred_quality:
                        default_quality = quality
                    if repetition == 0:
                        combobox_qualities[quality] += " (Best)"

                self.ui.qualityComboBox.replace_all_items(combobox_qualities, default_item=default_quality)


    def update_subtitles(self, clear=False):
        subtitles = {}
        if clear:
            self.subtitles = None
            self.ui.subtitlesComboBox.replace_all_items()
            return
        elif self.subtitles and isinstance(self.subtitles, dict):
            subtitles.update({"": "None"})
            subtitles.update(self.subtitles)
        
        self.ui.subtitlesComboBox.replace_all_items(subtitles)


    def update_download_directory_indicators(self):
        dir_name = QDir(self.download_directory).dirName()
        full_path = QUrl.fromLocalFile(self.download_directory).toString()

        if dir_name:
            new_text = f"<a href=\"{full_path}\">{dir_name}</a>"
        else:
            new_text = f"<a href=\"{full_path}\">{self.download_directory}</a>"

        self.ui.downloadFolderIndicatorLabel.setText(new_text)
        self.ui.downloadFolderIndicatorLabel.setToolTip(self.download_directory)


    def update_status_indicators(self, situation=None, progress=None, percentage=None):
        tab_index = self.parent.ui.tabWidget.indexOf(self)
        if situation:
            if progress and len(progress) == 2:
                progress_text = f" ({progress[0]}/{progress[1]})"
            else:
                progress_text = ""
            situation_text = self.settings_manager.CONSTANT_SETTTINGS["status_label_text"][situation]
            text = f"{situation_text}{progress_text}"
            icon = self.settings_manager.CONSTANT_SETTTINGS["status_label_icons"][situation]
            
            self.ui.statusLabel.setText(text)
            self.ui.statusIconLabel.setPixmap(icon.pixmap(QSize(28, 28)))
            if isinstance(percentage, int):
                self.ui.progressBar.setValue(percentage)
            self.parent.update_tab_status_indicators(
                tab_index,
                self.pretty_tab_number,
                situation,
                progress,
            )
        else:
            self.ui.statusLabel.setText("")
            self.ui.progressBar.setValue(0)
            self.parent.update_tab_status_indicators(tab_index, self.pretty_tab_number)
            self.ui.statusIconLabel.setPixmap(QPixmap())


    def restore_widgets_to_normal(self):
        self.ui.plainTextEdit.setReadOnly(False)
        self.ui.formatComboBox.setEnabled(True)
        self.ui.qualityComboBox.setEnabled(True)
        self.ui.subtitlesComboBox.setEnabled(True)
        self.ui.setDownloadFolderButton.setEnabled(True)
        self.ui.embedSubtitlesCheckBox.setEnabled(True)
        self.ui.cropThumbnailsCheckBox.setEnabled(True)
        self.ui.dataPullButton.setEnabled(True)
        self.ui.downloadButton.setEnabled(True)
        self.ui.dataPullButton.setText(
            self.settings_manager.CONSTANT_SETTTINGS["button_text"]["refresh"]["default"]
        )
        self.ui.downloadButton.setText(
            self.settings_manager.CONSTANT_SETTTINGS["button_text"]["download"]["default"]
        )