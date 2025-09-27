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


from time import sleep

from PySide6.QtWidgets import QMessageBox, QWidget, QFileDialog
from PySide6.QtCore import QCoreApplication, QSize
from PySide6.QtGui import QPixmap, QKeySequence, QShortcut

from .config import Config
from .directory_picker import DirectoryPicker
from src import ui
from src import utils
from src.downloader import Downloader


class Tab(QWidget):
    def __init__(self, parent, pretty_tab_number):
        super().__init__()
        self.setup_ui()
        self.setup_vars(parent, pretty_tab_number)
        self.directory_picker = DirectoryPicker(parent, on_select=self.update_download_directory_indicators)
        self.event_invoker = utils.Invoker()
        self.connect_signals_and_slots()
        self.downloader = Downloader(
            download_progress_func=self.download_progress,
            url_downloaded_func=self.url_download_progress,
            url_extracted_func=lambda
                processed_url_count,
                total_url_count,
                situation="extracting_urls":
                    self.url_extraction_progress(situation, processed_url_count, total_url_count),
            url_fetched_func=lambda
                processed_url_count,
                total_url_count,
                situation="pulling_data":
                    self.url_extraction_progress(situation, processed_url_count, total_url_count),
            conversion_progress_func=self.postprocess_progress
        )


    def setup_ui(self):
        self.ui = ui.Ui_Tab()
        self.ui.setupUi(self)

        QShortcut(QKeySequence("Alt+f"), self).activated.connect(lambda: self.show_combobox_popup(self.ui.formatComboBox))
        QShortcut(QKeySequence("Alt+q"), self).activated.connect(lambda: self.show_combobox_popup(self.ui.qualityComboBox))
        QShortcut(QKeySequence("Alt+s"), self).activated.connect(lambda: self.show_combobox_popup(self.ui.subtitlesComboBox))


    def setup_vars(self, parent, pretty_tab_number):
        self.parent = parent
        self.pretty_tab_number = pretty_tab_number
        self.thread_future = None
        self.cancel_progress = False
        self.thread_running = False
        self.being_destroyed = False
        self.user_answer = None
        self.changing_plain_text_edit = False
    

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
                progress_text = f" {progress[0]}/{progress[1]}"
            else:
                progress_text = ""

            self.ui.statusLabel.setText(f"{Config.STATUS_LABEL_TEXT[situation]}{progress_text}")
            if isinstance(percentage, int):
                self.ui.progressBar.setValue(percentage)
            self.parent.update_tab(tab_index, self.pretty_tab_number, situation, progress)
            self.ui.statusIconLabel.setPixmap(Config.STATUS_LABEL_ICONS[situation].pixmap(QSize(28, 28)))
        else:
            self.ui.statusLabel.setText(str())
            self.ui.progressBar.setValue(0)
            self.parent.update_tab(tab_index, self.pretty_tab_number)
            self.ui.statusIconLabel.setPixmap(QPixmap())


    def update_download_directory_indicators(self):
        self.ui.downloadFolderIndicatorLabel.setText(self.directory_picker.anchor)
        self.ui.downloadFolderIndicatorLabel.setToolTip(self.directory_picker.path)


    def prep_thread_start(self):
        self.thread_running = True

        urls = utils.plain_text_to_set(self.ui.plainTextEdit.toPlainText())
        self.change_plain_text_edit(utils.list_to_plain_text(urls))

        self.ui.plainTextEdit.setReadOnly(True)

        return urls
    

    def prep_thread_exit(self, situation=None, percentage=0):
        if not self.being_destroyed:
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
        self.ui.dataPullButton.setText(Config.BUTTON_TEXT["refresh"]["default"])
        self.ui.downloadButton.setText(Config.BUTTON_TEXT["download"]["default"])
        self.update_status_indicators(situation, percentage=percentage)
    
    
    def start_update_info(self):
        if not self.ui.plainTextEdit.toPlainText():
            return

        if self.thread_alive():
            self.cancel_thread("data_pull_cancelled")
            self.ui.dataPullButton.setEnabled(False)
            self.update_status_indicators("cancelling_data_pull")
        else:
            urls = self.prep_thread_start()
            self.update_status_indicators("pulling_data", (1, len(urls)), 0)
            self.ui.dataPullButton.setText(Config.BUTTON_TEXT["refresh"]["secondary"])
            self.ui.downloadButton.setEnabled(False)
            self.ui.qualityComboBox.setEnabled(False)
            self.ui.subtitlesComboBox.setEnabled(False)
            self.thread_future = self.parent.executor.submit(self.update_info, urls)


    def start_download(self):
        if not self.ui.plainTextEdit.toPlainText():
            return

        if self.thread_alive():
            self.cancel_thread("download_cancelled")
            self.ui.downloadButton.setEnabled(False)
            self.update_status_indicators(situation="cancelling_download")
        else:
            urls = self.prep_thread_start()
            if self.downloader.cache.available(urls):
                self.update_status_indicators("downloading", (1, self.downloader.cache.extracted_url_count), 0)
            else:
                self.update_status_indicators("extracting_urls", (1, len(urls)), 0)
            self.ui.downloadButton.setText(Config.BUTTON_TEXT["download"]["secondary"])
            self.ui.dataPullButton.setEnabled(False)
            self.thread_future = self.parent.executor.submit(self.download, urls)


    def url_extraction_progress(self, situation, processed_url_count, total_url_count):
        if self.cancel_progress:
            raise self.ForceCancel
        if processed_url_count + 1 <= total_url_count:
            processed_url_count += 1

        try:
            percentage = int(((processed_url_count - 1) / total_url_count) * 100)
        except:
            return

        self.run_in_gui_thread(lambda: self.update_status_indicators(situation, (processed_url_count, total_url_count), percentage))


    def download_progress(self, percentage, processed_url_count, total_url_count):
        if self.cancel_progress:
            raise self.ForceCancel
        if processed_url_count + 1 <= total_url_count:
            self.run_in_gui_thread(lambda: self.update_status_indicators("downloading", (processed_url_count + 1, total_url_count), percentage))


    def url_download_progress(self, processed_url_count, total_url_count, url):
        if url: self.remove_urls_from_entry([url])
        if self.cancel_progress:
            raise self.ForceCancel

        if processed_url_count < total_url_count:
            percentage = 0
        else:
            percentage = None
        if processed_url_count + 1 <= total_url_count:
            self.run_in_gui_thread(lambda: self.update_status_indicators("downloading", (processed_url_count + 1, total_url_count), percentage))
    

    def postprocess_progress(self, processed_url_count, total_url_count):
        if self.cancel_progress:
            raise self.ForceCancel
        self.run_in_gui_thread(lambda: self.update_status_indicators("converting", (processed_url_count + 1, total_url_count), 100))


    def update_info(self, urls):
        try:
            self.downloader.fetch_metadata(urls)
        except self.ForceCancel:
            self.prep_thread_exit("data_pull_cancelled")
            return
        except self.downloader.NoInternet:
            self.prep_thread_exit("no_internet")
            return
        except BaseException as e:
            print(e)
            self.prep_thread_exit("data_pull_failed")
            return
        
        if self.downloader.logs.pending_urls:
            self.handle_invalid_url_warning(self.downloader.logs.pending_urls, error_type="data_pull")

        if self.downloader.logs.all_failed():
            self.prep_thread_exit("data_pull_failed")
            return

        self.run_in_gui_thread(self.show_new_subtitles)
        self.run_in_gui_thread(self.show_new_qualities)
        
        self.prep_thread_exit("data_pull_finished", percentage=100)


    def download(self, urls):
        try:
            if not self.downloader.cache.available(urls):
                self.downloader.extract_urls(urls)
                if self.downloader.logs.all_failed():
                    self.handle_invalid_url_warning(self.downloader.logs.pending_urls, error_type="data_pull")
                    self.prep_thread_exit("download_failed")
                    return
                self.run_in_gui_thread(lambda: self.update_status_indicators("downloading", (1, self.downloader.cache.extracted_url_count), 0))
            
            self.run_in_gui_thread(lambda: self.ui.formatComboBox.setEnabled(False))
            self.run_in_gui_thread(lambda: self.ui.qualityComboBox.setEnabled(False))
            self.run_in_gui_thread(lambda: self.ui.subtitlesComboBox.setEnabled(False))
            self.run_in_gui_thread(lambda: self.ui.setDownloadFolderButton.setEnabled(False))
            self.run_in_gui_thread(lambda: self.ui.embedSubtitlesCheckBox.setEnabled(False))
            self.run_in_gui_thread(lambda: self.ui.cropThumbnailsCheckBox.setEnabled(False))
            
            if subtitles := self.ui.subtitlesComboBox.currentData():
               subtitles = [subtitles]
            else:
                subtitles = None 

            self.downloader.download(
                urls=urls,
                download_dir=self.download_location,
                file_type=Config.FORMATS[self.ui.formatComboBox.currentText()],
                subtitles=subtitles,
                quality=self.ui.qualityComboBox.currentData(),
                embed_subtitles=self.ui.embedSubtitlesCheckBox.isChecked(),
                crop_thumbnails=self.ui.cropThumbnailsCheckBox.isChecked()
            )
        except self.ForceCancel:
            self.prep_thread_exit("download_cancelled")
            return
        except self.downloader.NoInternet:
            self.prep_thread_exit("no_internet")
            return
        except BaseException as e:
            print(e)
            self.prep_thread_exit("download_failed")
            return
        if self.downloader.logs.pending_urls or self.downloader.cache.failed_urls:
            self.handle_invalid_url_warning(self.downloader.logs.pending_urls | self.downloader.cache.failed_urls, error_type="download")
        if self.downloader.logs.all_failed():
            self.prep_thread_exit("download_failed")
            return

        self.prep_thread_exit("download_finished", 100)


    def display_invalid_url_warning(self, text):
        answer = QMessageBox.warning(
            self,
            Config.WINDOW_TITLES["error"].replace("<pretty_tab_number>", str(self.pretty_tab_number)),
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
            self.downloader.metadata.clear()


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
        if Config.FORMATS[_format] == "mp3":
            utils.update_combobox_items(self.ui.qualityComboBox, self.downloader.metadata.bitrates)
        elif Config.FORMATS[_format] == "mp4":
            utils.update_combobox_items(self.ui.qualityComboBox, self.downloader.metadata.resolutions)


    def show_new_subtitles(self):
        if self.downloader.metadata.subtitles:
            subtitles = {None: "None"} | self.downloader.metadata.subtitles
        else:
            subtitles = {}
        utils.update_combobox_items(
            self.ui.subtitlesComboBox, subtitles)
    

    def change_plain_text_edit(self, text=""):
        self.changing_plain_text_edit = True
        self.ui.plainTextEdit.setPlainText(text)
        self.changing_plain_text_edit = False


    def cancel_thread(self, situation=None):
        if self.thread_future:
            if self.thread_future.cancel() and situation:
                self.prep_thread_exit(situation)
            else:
                self.cancel_progress = True


    def thread_alive(self):
        return self.thread_running or (self.thread_future and self.thread_future.running())


    def destroy(self):
        self.being_destroyed = True
        self.cancel_thread()
        self.deleteLater()


    class ForceCancel(BaseException): pass