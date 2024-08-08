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


import os
from threading import Thread
from time import sleep

from .ui import Text, Ui_MainWindow, Ui_aboutDialog
from . import utils
from . import youtubedl_helpers as yt_dlp_h

from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QDialog
from PySide6.QtCore import QEvent, QObject, QCoreApplication, QUrl


class Window(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.setup_ui()
        self.setup_vars()
        self.setup_filedialog()
        self.show_new_download_folder()

        self.event_invoker = utils.Invoker()
        self.about_window = AboutWindow(self)

        self.connect_signals_and_slots(app)


    def setup_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def setup_vars(self):
        self.download_location = os.getcwd().replace("\\", "/")
        self.thread_running = False
        self.cancel_progress = False
        self.subtitles = {}
        self.qualities = {"video": {}, "audio": []}
        self.popup_window_running = False
        self.user_answer = None
        self.changing_plain_text_edit = False
    

    def setup_filedialog(self):
        self.file_dialog = QFileDialog(self)
        self.file_dialog.setFileMode(QFileDialog.Directory)
    

    def connect_signals_and_slots(self, app):
        self.ui.refreshPushButton.clicked.connect(self.start_update_info)
        self.ui.downloadPushButton.clicked.connect(self.start_download)
        self.ui.setDownloadFolderPushButton.clicked.connect(self.set_download_location)
        self.ui.formatComboBox.currentTextChanged.connect(self.show_new_qualities)
        self.ui.actionAbout.triggered.connect(self.about_window.exec)
        self.ui.actionExit.triggered.connect(app.quit)
        self.ui.plainTextEdit.textChanged.connect(self.on_text_change)


    def prep_thread_start(self):
        self.thread_running = True

        urls = utils.plain_text_to_set(self.ui.plainTextEdit.toPlainText())
        self.change_plain_text_edit(utils.list_to_plain_text(urls))
    
        text = Text.STATUS_MESSAGES["extracting_urls"]
        text = text.replace("<repetition>", "1")
        text = text.replace("<repetitions>", str(len(urls)))
        self.ui.statusLabel.setText(text)
        self.ui.progressBar.setValue(0)

        return urls
    

    def prep_thread_exit(self, message="", percentage=0):
        self.thread_running = False
        self.cancel_progress = False

        self.ui.refreshPushButton.setEnabled(True)
        self.ui.downloadPushButton.setEnabled(True)

        self.ui.refreshPushButton.setText(Text.BUTTON_TEXT["refresh"]["default"])
        self.ui.downloadPushButton.setText(Text.BUTTON_TEXT["download"]["default"])

        self.run_in_gui_thread(lambda: self.ui.progressBar.setValue(percentage))
        self.run_in_gui_thread(lambda: self.ui.statusLabel.setText(message))

        yt_dlp_h.delete_temp_files(self.download_location)
    
    
    def start_update_info(self):
        if not self.ui.plainTextEdit.toPlainText():
            return

        if not self.thread_running:
            urls = self.prep_thread_start()
            self.ui.refreshPushButton.setText(Text.BUTTON_TEXT["refresh"]["secondary"])
            self.ui.downloadPushButton.setEnabled(False)
            Thread(target=lambda: self.update_info(urls), daemon=True).start()

        elif self.thread_running:
            self.cancel_progress = True
            self.ui.refreshPushButton.setEnabled(False)
            self.ui.statusLabel.setText(Text.STATUS_MESSAGES["cancelling_refresh"])


    def start_download(self):
        if not self.ui.plainTextEdit.toPlainText():
            return

        if not self.thread_running:
            urls = self.prep_thread_start()
            self.ui.downloadPushButton.setText(Text.BUTTON_TEXT["download"]["secondary"])
            self.ui.refreshPushButton.setEnabled(False)
            Thread(target=lambda: self.download(urls), daemon=True).start()

        else:
            self.cancel_progress = True
            self.ui.downloadPushButton.setEnabled(False)
            self.ui.statusLabel.setText(Text.STATUS_MESSAGES["cancelling_download"])


    def url_extraction_progress(self, processed_url_count, total_url_count, text):
        if self.cancel_progress:
            raise SystemExit
        if processed_url_count <= total_url_count:
            try:
                percentage = int((processed_url_count / total_url_count) * 100)
            except:
                return
            self.run_in_gui_thread(lambda: self.ui.progressBar.setValue(percentage))
        if processed_url_count + 1 <= total_url_count:
            text = text.replace("<repetition>", str(processed_url_count + 1))
            text = text.replace("<repetitions>", str(total_url_count))
            self.run_in_gui_thread(lambda: self.ui.statusLabel.setText(text))


    def download_progress(self, data, processed_url_count, total_url_count):
        if self.cancel_progress:
            raise SystemExit
    
        if data["status"] == "downloading":
            percentage = None            
            
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
            
            if isinstance(percentage, int):
                if percentage > 100:
                    percentage = 100
                self.run_in_gui_thread(lambda: self.ui.progressBar.setValue(percentage))
        
        if processed_url_count + 1 <= total_url_count:
            text = Text.STATUS_MESSAGES["downloading"]
            text = text.replace("<repetition>", str(processed_url_count + 1))
            text = text.replace("<repetitions>", str(total_url_count))
            self.run_in_gui_thread(lambda: self.ui.statusLabel.setText(text))


    def url_download_progress(self, url, processed_url_count, total_url_count):
        if self.cancel_progress:
            raise SystemExit

        if processed_url_count < total_url_count:
            self.run_in_gui_thread(lambda: self.ui.progressBar.setValue(0))
        if processed_url_count + 1 <= total_url_count:
            text = Text.STATUS_MESSAGES["downloading"]
            text = text.replace("<repetition>", str(processed_url_count + 1))
            text = text.replace("<repetitions>", str(total_url_count))
            self.run_in_gui_thread(lambda: self.ui.statusLabel.setText(text))
        if self.ui.urlremovalCheckBox.isChecked():
            self.remove_urls_from_entry([url])
    

    def postprocess_progress(self, data, processed_url_count, total_url_count):
        if self.cancel_progress:
            raise SystemExit
        self.run_in_gui_thread(lambda: self.ui.progressBar.setValue(100))
        text = Text.STATUS_MESSAGES["converting"]
        text = text.replace("<repetition>", str(processed_url_count + 1))
        text = text.replace("<repetitions>", str(total_url_count))
        self.run_in_gui_thread(lambda: self.ui.statusLabel.setText(text))


    def update_info(self, urls):
        try:
            urls, failed_urls1, exit_status = yt_dlp_h.extract_urls(
                urls,
                on_progress=lambda
                    processed_url_count,
                    total_url_count,
                    text=Text.STATUS_MESSAGES["extracting_urls"]:
                        self.url_extraction_progress(processed_url_count, total_url_count, text),
            )
        except SystemExit:
            self.prep_thread_exit(Text.STATUS_MESSAGES["refresh_cancelled"])
            return
        except BaseException as e:
            self.prep_thread_exit(Text.STATUS_MESSAGES["refresh_failed"])
            print(e)
            return
        if not exit_status or not urls:
            if not exit_status:
                self.handle_no_internet_warning()
            elif not urls and failed_urls1:
                self.handle_invalid_url_warning(failed_urls1, error_type="refresh")
            self.prep_thread_exit(Text.STATUS_MESSAGES["refresh_failed"])
            return
        
        text = Text.STATUS_MESSAGES["refreshing"]
        text = text.replace("<repetition>", "1").replace("<repetitions>", str(len(urls)))
        self.run_in_gui_thread(lambda: self.ui.statusLabel.setText(text))
        self.run_in_gui_thread(lambda: self.ui.progressBar.setValue(0))
        
        try:
            data, failed_urls2, exit_status = yt_dlp_h.extract_data(
                urls,
                on_progress=lambda
                    processed_url_count,
                    total_url_count,
                    text=Text.STATUS_MESSAGES["refreshing"]:
                        self.url_extraction_progress(processed_url_count, total_url_count, text),
            )
        except SystemExit:
            self.prep_thread_exit(Text.STATUS_MESSAGES["refresh_cancelled"])
            return
        except BaseException as e:
            print(e)
            self.prep_thread_exit(Text.STATUS_MESSAGES["refresh_failed"])
            return
        failed_urls = failed_urls1.union(failed_urls2)

        if not exit_status or not data:
            if not exit_status:
                self.handle_no_internet_warning()
            elif failed_urls and not data:
                self.handle_invalid_url_warning(failed_urls, error_type="refresh")
            self.prep_thread_exit(Text.STATUS_MESSAGES["refresh_failed"])
            return
        
        if failed_urls and data:
            self.handle_invalid_url_warning(failed_urls, error_type="refresh")

        try:
            data = yt_dlp_h.extract_basic_info(data)
        except BaseException as e:
            print(e)
            self.prep_thread_exit(Text.STATUS_MESSAGES["refresh_failed"])
            return

        self.qualities = data[0]
        self.run_in_gui_thread(self.show_new_qualities)
        
        subtitles = data[1]
        if subtitles:
            self.subtitles["None"] = "none"
            self.subtitles.update(subtitles)
            utils.update_combobox_items(self.ui.subtitlesComboBox, self.subtitles.keys())
        
        self.prep_thread_exit(Text.STATUS_MESSAGES["refresh_finished"], 100)


    def download(self, urls):
        try:
            urls, failed_urls1, exit_status = yt_dlp_h.extract_urls(
                urls,
                lambda
                    processed_url_count,
                    total_url_count,
                    text=Text.STATUS_MESSAGES["extracting_urls"]:
                        self.url_extraction_progress(processed_url_count, total_url_count, text))
        except SystemExit:
            self.prep_thread_exit(Text.STATUS_MESSAGES["download_cancelled"])
            return
        except BaseException as e:
            print(e)
            self.prep_thread_exit(Text.STATUS_MESSAGES["download_failed"])
            return
        if not exit_status or not urls:
            if not exit_status:
                self.handle_no_internet_warning()
            elif not urls and failed_urls1:
                self.handle_invalid_url_warning(failed_urls1)
            self.prep_thread_exit(Text.STATUS_MESSAGES["download_failed"])
            return
        
        text = Text.STATUS_MESSAGES["downloading"]
        text = text.replace("<repetition>", "1").replace("<repetitions>", str(len(urls)))
        self.run_in_gui_thread(lambda: self.ui.statusLabel.setText(text))
        self.run_in_gui_thread(lambda: self.ui.progressBar.setValue(0))

        file_type = Text.FORMATS[self.ui.formatComboBox.currentText()]
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
        embed_subtitles = self.ui.embedSubtitlesCheckBox.isChecked()

        try:
            failed_urls2, exit_status = yt_dlp_h.download(
                urls=urls,
                subtitles=subtitles,
                on_progress=self.download_progress,
                download_location=self.download_location,
                file_type=file_type,
                quality=quality,
                postprocessor_progress=self.postprocess_progress,
                on_url_progress=self.url_download_progress,
                embed_subtitles=embed_subtitles,
            )
        except SystemExit:
            self.prep_thread_exit(Text.STATUS_MESSAGES["download_cancelled"])
            return
        except BaseException as e:
            print(e)
            self.prep_thread_exit(Text.STATUS_MESSAGES["download_failed"])
            return
        failed_urls = failed_urls1.union(failed_urls2)
        
        if not exit_status or failed_urls == urls:
            if not exit_status:
                self.handle_no_internet_warning()
            elif failed_urls == urls:
                self.handle_invalid_url_warning(failed_urls)
            self.prep_thread_exit(Text.STATUS_MESSAGES["download_failed"])
        else:
            if failed_urls:
                self.handle_invalid_url_warning(failed_urls)
            self.prep_thread_exit(Text.STATUS_MESSAGES["download_finished"], 100)


    def display_invalid_url_warning(self, text):
        answer = QMessageBox.warning(
            self,
            Text.WINDOW_TITLES["error"],
            text,
            buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            defaultButton=QMessageBox.StandardButton.Yes,
        )
        if answer == QMessageBox.Yes:
            self.user_answer = True
        else:
            self.user_answer = False

        self.popup_window_running = False
    

    def handle_invalid_url_warning(self, urls, error_type="download"):
        if error_type == "download":
            beggining_text = f"Couldn't download the following {len(urls)} URLs:"
        else:
            beggining_text = f"The following {len(urls)} URLs are invalid:"

        url_list_text = "<ul>"
        for url in urls:
            url_list_text += f"<li><a href='{url}'>{url}</a></li>"
        url_list_text += "</ul>"

        ending_text = "Remove them from the text entry?"

        text = beggining_text + url_list_text + ending_text

        while self.popup_window_running:
            sleep(0.01)

        self.popup_window_running = True
        self.run_in_gui_thread(lambda: self.display_invalid_url_warning(text))

        while self.popup_window_running:
            sleep(0.01)

        if self.user_answer:
            self.remove_urls_from_entry(urls)
    

    def display_no_internet_warning(self):
        QMessageBox.critical(
            self,
            Text.WINDOW_TITLES["error"],
            "No internet connection.",
            defaultButton=QMessageBox.StandardButton.Ok,
        )
        self.popup_window_running = False
    

    def handle_no_internet_warning(self):
        while self.popup_window_running:
            sleep(0.01)
        
        self.popup_window_running = True
        self.run_in_gui_thread(self.display_no_internet_warning)

        while self.popup_window_running:
            sleep(0.01)


    def remove_urls_from_entry(self, urls):
        text = self.ui.plainTextEdit.toPlainText()
        self.run_in_gui_thread(lambda: self.change_plain_text_edit(utils.remove_lines(text, urls)))


    def set_download_location(self):
        if self.file_dialog.exec():
            self.download_location = self.file_dialog.selectedFiles()[0]
            self.show_new_download_folder()
   

    def on_text_change(self):
        if not self.changing_plain_text_edit and not self.thread_running:
            utils.update_combobox_items(self.ui.qualityComboBox)
            utils.update_combobox_items(self.ui.subtitlesComboBox)
            self.ui.statusLabel.setText("")
            self.ui.progressBar.setValue(0)
            self.subtitles = {}
            self.qualities = {"video": {}, "audio": []}


    def run_in_gui_thread(self, fn):
        QCoreApplication.postEvent(
            self.event_invoker,
            utils.InvokeEvent(fn)
        )
    

    def show_new_download_folder(self):
        base_name = os.path.basename(self.download_location)
        href = QUrl.fromLocalFile(self.download_location).toString()

        if base_name:
            new_text = f"<a href=\"{href}\">{base_name}</a>"
        else:
            new_text = f"<a href=\"{href}\">{self.download_location}</a>"

        self.ui.downloadFolderIndicatorLabel.setText(new_text)
        self.ui.downloadFolderIndicatorLabel.setToolTip(self.download_location)


    def show_new_qualities(self):
        _format = self.ui.formatComboBox.currentText()
        if Text.FORMATS[_format] == "audio":
            utils.update_combobox_items(self.ui.qualityComboBox, self.qualities["audio"])
        elif Text.FORMATS[_format] == "video":
            utils.update_combobox_items(self.ui.qualityComboBox, self.qualities["video"].keys())
    

    def change_plain_text_edit(self, text=""):
        self.changing_plain_text_edit = True
        self.ui.plainTextEdit.setPlainText(text)
        self.changing_plain_text_edit = False


class AboutWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_aboutDialog()
        self.ui.setupUi(self)