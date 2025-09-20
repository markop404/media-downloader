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

class Config:
    APP_NAME = "Media Downloader"
    STATUS_LABEL_TEXT = {
        "download_failed": "Downloading failed",
        "download_cancelled": "Downloading cancelled",
        "download_finished": "Downloading finished",
        "cancelling_download": "Cancelling downloading...",
        "downloading": "Downloading...",
        "extracting_urls": "Analyzing URLs...",
        "data_pull_failed": "Loading options failed",
        "data_pull_cancelled": "Loading options cancelled",
        "data_pull_finished": "Loading options finished",
        "cancelling_data_pull": "Cancelling option loading...",
        "pulling_data": "Loading options...",
        "converting": "Processing...",
        "no_internet": "No internet connection",
    }
    STATUS_LABEL_ICONS = {
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
    }
    TAB_TEXT = {
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
        "pulling_data": "Loading options",
        "converting": "Downloading",
        "no_internet": "Failed",
    }
    WINDOW_TITLES = {
        "error": "Error - Tab <pretty_tab_number>",
    }
    BUTTON_TEXT = {
        "download": {"default": "&Download", "secondary": "Cancel &Download"},
        "refresh": {"default": "&Load Options", "secondary": "Cancel Option &Load"},
    }
    FORMATS = {
        "Audio": "mp3",
        "Video": "mp4",
    }
