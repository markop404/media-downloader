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


APP_NAME = "Media Downloader"

STATUS_LABEL_TEXT = {
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
    "pulling_data": "Pulling Data",
    "converting": "Downloading",
    "no_internet": "Failed",
}

TAB_ICONS = {
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
}

WINDOW_TITLES = {
    "error": "Error - Tab <pretty_tab_number>",
}

BUTTON_TEXT = {
    "download": {"default": "&Download", "secondary": "Cancel &Download"},
    "refresh": {"default": "&Pull Data", "secondary": "Cancel Data &Pull"},
}

FORMATS = {
    "Audio": "audio",
    "Video": "video",
}