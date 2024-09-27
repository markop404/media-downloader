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


from threading import Thread
from time import sleep
import sys

from PySide6.QtWidgets import QMessageBox, QWidget, QFileDialog
from PySide6.QtCore import QCoreApplication, QUrl, QDir, QStandardPaths, QSize
from PySide6.QtGui import QPixmap, QKeySequence, QShortcut

from src import ui
from src import utils


class Tab(QWidget):
    def __init__(self, parent, pretty_tab_number):
        super().__init__()
        self.setup_ui()
        self.setup_vars(parent, pretty_tab_number)
        self.setup_filedialog()
        self.update_download_directory_indicators()
        self.event_invoker = utils.Invoker()
        self.connect_signals_and_slots()


    def setup_ui(self):
        self.ui = ui.Ui_Tab()
        self.ui.setupUi(self)

        QShortcut(QKeySequence("Alt+f"), self).activated.connect(lambda: self.show_combobox_popup(self.ui.formatComboBox))
        QShortcut(QKeySequence("Alt+q"), self).activated.connect(lambda: self.show_combobox_popup(self.ui.qualityComboBox))
        QShortcut(QKeySequence("Alt+s"), self).activated.connect(lambda: self.show_combobox_popup(self.ui.subtitlesComboBox))


    def setup_vars(self, parent, pretty_tab_number):
        self.parent = parent
        self.pretty_tab_number = pretty_tab_number
        self.download_location = QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)
        self.thread_running = False
        self.cancel_progress = False
        self.subtitles = {}
        self.qualities = {"video": {}, "audio": []}
        self.user_answer = None
        self.changing_plain_text_edit = False
    

    def setup_filedialog(self):
        self.file_dialog = QFileDialog(self)
        self.file_dialog.setFileMode(QFileDialog.Directory)
        self.file_dialog.setDirectory(self.download_location)
    

    def connect_signals_and_slots(self):
        self.ui.dataPullButton.clicked.connect(self.start_update_info)
        self.ui.downloadButton.clicked.connect(self.start_download)
        self.ui.setDownloadFolderButton.clicked.connect(self.set_download_location)
        self.ui.formatComboBox.currentTextChanged.connect(self.show_new_qualities)
        self.ui.plainTextEdit.textChanged.connect(self.on_text_change)


    def update_status_indicators(self, situation=None, progress=None, percentage=None):
        tab_index = self.parent.ui.tabWidget.indexOf(self)
        if situation:
            if progress and len(progress) == 2:
                progress_text = f" ({progress[0]}/{progress[1]})"
            else:
                progress_text = ""

            self.ui.statusLabel.setText(f"{ui.Config.STATUS_LABEL_TEXT[situation]}{progress_text}")
            if percentage:
                self.ui.progressBar.setValue(percentage)
            self.parent.update_tab(tab_index, self.pretty_tab_number, situation, progress)
            self.ui.statusIconLabel.setPixmap(ui.Config.STATUS_LABEL_ICONS[situation].pixmap(QSize(28, 28)))
        else:
            self.ui.statusLabel.setText(str())
            self.ui.progressBar.setValue(0)
            self.parent.update_tab(tab_index, self.pretty_tab_number)
            self.ui.statusIconLabel.setPixmap(QPixmap())


    def update_download_directory_indicators(self):
        base_name = QDir(self.download_location).dirName()
        href = QUrl.fromLocalFile(self.download_location).toString()

        if base_name:
            new_text = f"<a href=\"{href}\">{base_name}</a>"
        else:
            new_text = f"<a href=\"{href}\">{self.download_location}</a>"

        self.ui.downloadFolderIndicatorLabel.setText(new_text)
        self.ui.downloadFolderIndicatorLabel.setToolTip(self.download_location)


    def prep_thread_start(self):
        self.thread_running = True

        urls = utils.plain_text_to_set(self.ui.plainTextEdit.toPlainText())
        self.change_plain_text_edit(utils.list_to_plain_text(urls))
        self.update_status_indicators(situation="extracting_urls", progress=(1, len(urls)))

        self.ui.plainTextEdit.setReadOnly(True)
        self.ui.qualityComboBox.setEnabled(False)
        self.ui.subtitlesComboBox.setEnabled(False)

        return urls
    

    def prep_thread_exit(self, situation=None, percentage=0):
        self.thread_running = False
        self.cancel_progress = False
        self.run_in_gui_thread(lambda: self.restore_widgets_to_normal(situation, percentage))
    

    def restore_widgets_to_normal(self, situation, percentage):
        self.ui.plainTextEdit.setReadOnly(False)
        self.ui.formatComboBox.setEnabled(True)
        self.ui.qualityComboBox.setEnabled(True)
        self.ui.subtitlesComboBox.setEnabled(True)
        self.ui.setDownloadFolderButton.setEnabled(True)
        self.ui.embedSubtitlesCheckBox.setEnabled(True)
        self.ui.cropThumbnailsCheckBox.setEnabled(True)
        self.ui.dataPullButton.setEnabled(True)
        self.ui.downloadButton.setEnabled(True)
        self.ui.dataPullButton.setText(ui.Config.BUTTON_TEXT["refresh"]["default"])
        self.ui.downloadButton.setText(ui.Config.BUTTON_TEXT["download"]["default"])
        self.update_status_indicators(situation, percentage=percentage)
    
    
    def start_update_info(self):
        if not self.ui.plainTextEdit.toPlainText():
            return

        if not self.thread_running:
            urls = self.prep_thread_start()
            self.ui.dataPullButton.setText(ui.BUTTON_TEXT["refresh"]["secondary"])
            self.ui.downloadButton.setEnabled(False)
            Thread(target=lambda: self.update_info(urls), daemon=True).start()
        elif self.thread_running:
            self.cancel_progress = True
            self.ui.dataPullButton.setEnabled(False)
            self.update_status_indicators("cancelling_data_pull")


    def start_download(self):
        if not self.ui.plainTextEdit.toPlainText():
            return

        if not self.thread_running:
            urls = self.prep_thread_start()
            self.ui.downloadButton.setText(ui.BUTTON_TEXT["download"]["secondary"])
            self.ui.dataPullButton.setEnabled(False)
            self.ui.formatComboBox.setEnabled(False)
            self.ui.setDownloadFolderButton.setEnabled(False)
            self.ui.embedSubtitlesCheckBox.setEnabled(False)
            self.ui.cropThumbnailsCheckBox.setEnabled(False)
            Thread(target=lambda: self.download(urls), daemon=True).start()
        else:
            self.cancel_progress = True
            self.ui.downloadButton.setEnabled(False)
            self.update_status_indicators(situation="cancelling_download")


    def url_extraction_progress(self, situation, processed_url_count, total_url_count):
        if self.cancel_progress:
            raise SystemExit
        if processed_url_count + 1 <= total_url_count:
            processed_url_count += 1

        try:
            percentage = int(((processed_url_count - 1) / total_url_count) * 100)
        except:
            return

        self.run_in_gui_thread(lambda: self.update_status_indicators(situation, (processed_url_count, total_url_count), percentage))


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
            self.run_in_gui_thread(lambda: self.update_status_indicators("downloading", (processed_url_count + 1, total_url_count), percentage))


    def url_download_progress(self, url, processed_url_count, total_url_count):
        if self.cancel_progress:
            raise SystemExit

        if processed_url_count < total_url_count:
            percentage = 0
        else:
            percentage = None
        if processed_url_count + 1 <= total_url_count:
            self.run_in_gui_thread(lambda: self.update_status_indicators("downloading", (processed_url_count + 1, total_url_count), percentage))
        if self.ui.urlremovalCheckBox.isChecked():
            self.remove_urls_from_entry([url])
    

    def postprocess_progress(self, data, processed_url_count, total_url_count):
        if self.cancel_progress:
            raise SystemExit
        self.run_in_gui_thread(lambda: self.update_status_indicators("converting", (processed_url_count + 1, total_url_count), 100))


    def update_info(self, urls):
        try:
            urls, failed_urls1, exit_status, errors = ytdlp_helpers.extract_urls(
                urls,
                on_progress=lambda
                    processed_url_count,
                    total_url_count,
                    situation="extracting_urls":
                        self.url_extraction_progress(situation, processed_url_count, total_url_count),
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

        self.run_in_gui_thread(lambda: self.update_status_indicators("pulling_data", (1, len(urls)), 0))
        
        try:
            data, failed_urls2, exit_status, errors = ytdlp_helpers.extract_data(
                urls,
                on_progress=lambda
                    processed_url_count,
                    total_url_count,
                    situation="pulling_data":
                        self.url_extraction_progress(situation, processed_url_count, total_url_count),
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
            data = ytdlp_helpers.extract_basic_info(data)
        except BaseException as e:
            print(e)
            self.prep_thread_exit("data_pull_failed")
            return

        self.qualities = data[0]
        self.run_in_gui_thread(self.show_new_qualities)
        
        subtitles = data[1]
        if subtitles:
            self.subtitles["None"] = "none"
            self.subtitles.update(subtitles)
            utils.update_combobox_items(self.ui.subtitlesComboBox, self.subtitles.keys())
        
        self.prep_thread_exit("data_pull_finished", percentage=100)


    def download(self, urls):
        try:
            urls, failed_urls1, exit_status, errors = ytdlp_helpers.extract_urls(
                urls,
                lambda
                    processed_url_count,
                    total_url_count,
                    situation="extracting_urls":
                        self.url_extraction_progress(situation, processed_url_count, total_url_count))
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

        self.run_in_gui_thread(lambda: self.update_status_indicators("downloading", (1, len(urls)), 0))

        file_type = ui.FORMATS[self.ui.formatComboBox.currentText()]
        selected_quality = self.ui.qualityComboBox.currentText()
        if file_type == "video" and selected_quality in self.qualities["video"]:
            quality = self.qualities["video"][selected_quality]
        else:
            quality = selected_quality

        subtitles = self.ui.subtitlesComboBox.currentText()
        if subtitles == "":
            subtitles = None
        else:
            subtitles = [self.subtitles[subtitles]]

        try:
            failed_urls2, exit_status, errors = ytdlp_helpers.download(
                urls=urls,
                subtitles=subtitles,
                on_progress=self.download_progress,
                download_location=self.download_location,
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
            ui.WINDOW_TITLES["error"].replace("<pretty_tab_number>", str(self.pretty_tab_number)),
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
            sleep(0.01)

        self.parent.popup_window_running = True
        self.run_in_gui_thread(lambda: self.display_invalid_url_warning(text))

        while self.parent.popup_window_running:
            sleep(0.01)

        if self.user_answer:
            self.remove_urls_from_entry(urls)


    def remove_urls_from_entry(self, urls):
        text = self.ui.plainTextEdit.toPlainText()
        self.run_in_gui_thread(lambda: self.change_plain_text_edit(utils.remove_lines(text, urls)))
   

    def on_text_change(self):
        if not self.changing_plain_text_edit and not self.thread_running:
            utils.update_combobox_items(self.ui.qualityComboBox)
            utils.update_combobox_items(self.ui.subtitlesComboBox)
            self.update_status_indicators()
            self.subtitles = {}
            self.qualities = {"video": {}, "audio": []}


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
            self.download_location = self.file_dialog.selectedFiles()[0]
            self.update_download_directory_indicators()


    def show_new_qualities(self):
        _format = self.ui.formatComboBox.currentText()
        if ui.FORMATS[_format] == "audio":
            utils.update_combobox_items(self.ui.qualityComboBox, self.qualities["audio"])
        elif ui.FORMATS[_format] == "video":
            utils.update_combobox_items(self.ui.qualityComboBox, self.qualities["video"].keys())
    

    def change_plain_text_edit(self, text=""):
        self.changing_plain_text_edit = True
        self.ui.plainTextEdit.setPlainText(text)
        self.changing_plain_text_edit = False
