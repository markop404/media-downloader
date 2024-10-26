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


from PySide6.QtGui import QIcon
from PySide6.QtCore import QSettings, QPoint, QSize

class Settings(QSettings):
    def __init__(self):
        super().__init__()
    

    def save_setting(self, setting, value):
        old_value = self.value(setting)
        if old_value != value:
            self.setValue(setting, value)


    def load_setting(self, setting):
        saved_value = self.value(setting, type=self.DEFAULT_SETTINGS[setting]["type"])
        if saved_value != None:
            return saved_value
        else:
            return self.DEFAULT_SETTINGS[setting]["value"]


    APP_NAME = "Media Downloader"
    CONSTANT_SETTTINGS = {
        "status_label_text": {
            "download_failed": "Downloading Failed.",
            "download_cancelled": "Downloading Cancelled.",
            "download_finished": "Downloading Finished.",
            "cancelling_download": "Cancelling Download...",
            "downloading": "Downloading...",
            "extracting_urls": "Analyzing URLs...",
            "data_pull_failed": "Data Pull Failed.",
            "data_pull_cancelled": "Data Pull Cancelled.",
            "data_pull_finished": "Data Pull Finished.",
            "cancelling_data_pull": "Cancelling Data Pull...",
            "pulling_data": "Pulling Data...",
            "converting": "Processing...",
            "no_internet": "No internet connection.",
        },

        "status_label_icons": {
            "download_failed": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogWarning)),
            "download_cancelled": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogWarning)),
            "download_finished": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart)),
            "cancelling_download": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogWarning)),
            "downloading": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoDown)),
            "extracting_urls": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh)),
            "data_pull_failed": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogWarning)),
            "data_pull_cancelled": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogWarning)),
            "data_pull_finished": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogInformation)),
            "cancelling_data_pull": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogWarning)),
            "pulling_data": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh)),
            "converting": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoDown)),
            "no_internet": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.NetworkOffline)),
        },

        "tab_text": {
            "download_failed": "Failed",
            "download_cancelled": "Cancelled",
            "download_finished": "Finished",
            "cancelling_download": "Cancelling",
            "downloading": "Downloading",
            "extracting_urls": "Analyzing",
            "data_pull_failed": "Failed",
            "data_pull_cancelled": "Cancelled",
            "data_pull_finished": "Finished",
            "cancelling_data_pull": "Cancelling",
            "pulling_data": "Pulling Data",
            "converting": "Downloading",
            "no_internet": "Failed",
        },

        "tab_icons": {
            "download_failed": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogWarning)),
            "download_cancelled": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogWarning)),
            "download_finished": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart)),
            "cancelling_download": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogWarning)),
            "downloading": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoDown)),
            "extracting_urls": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh)),
            "data_pull_failed": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogWarning)),
            "data_pull_cancelled": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogWarning)),
            "data_pull_finished": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogInformation)),
            "cancelling_data_pull": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogWarning)),
            "pulling_data": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh)),
            "converting": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoDown)),
            "no_internet": QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogWarning)),
        },

        "window_titles": {
            "error": "Error - Tab <pretty_tab_number>",
        },

        "button_text": {
            "download": {"default": "&Download", "secondary": "Cancel &Download"},
            "refresh": {"default": "&Pull Data", "secondary": "Cancel Data &Pull"},
        },

        "formats": {
            "Audio": "mp3",
            "Video": "mp4",
        },
    }
    DEFAULT_SETTINGS = {
        "remember-tab-settings": {"value": True, "type": bool},
        "remove-downloaded-urls": {"value": True, "type": bool},
        "preferred-resolution": {"value": 1440, "type": int},
        "preferred-bitrate": {"value": 192, "type": int},
        "download-format": {"value": "mp4", "type": str},
        "crop-thumbnails": {"value": False, "type": bool},
        "embed-subtitles": {"value": True, "type": bool},
        "download-dir": {"value": None, "type": str},
        "window-position": {"value": None, "type": QPoint},
        "window-size": {"value": None, "type": QSize},
    }