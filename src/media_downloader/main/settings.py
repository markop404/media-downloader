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
from PySide6.QtCore import QSettings, QPoint, QSize, QStandardPaths


class Settings(QSettings):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.ICONS = {
            "emblem-downloads": QIcon(
                QIcon.fromTheme(
                    "emblem-downloads",
                    QIcon(QIcon.fromTheme("edit-download"))
                )
            ),
            "emblem-default": QIcon(
                QIcon.fromTheme(
                    "emblem-default",
                    QIcon(QIcon.fromTheme("dialog-ok"))
                )
            ),
            "dialog-error": QIcon(QIcon.fromTheme("dialog-error")),
            "view-refresh": QIcon(QIcon.fromTheme("view-refresh")),
            "network-offline": QIcon(QIcon.fromTheme("network-offline")),
            "media-playback-stop": QIcon(QIcon.fromTheme("media-playback-stop")),
        }
        self.STATIC_SETTINGS = {
            "status_label_text": {
                "download_failed": "Downloading Failed.",
                "download_cancelled": "Downloading Cancelled.",
                "download_finished": "Downloading Finished.",
                "cancelling_download": "Cancelling Download...",
                "downloading": "Downloading...",
                "extracting_urls": "Analyzing URLs...",
                "data_fetch_failed": "Loading Options Failed.",
                "data_fetch_cancelled": "Loading Options Cancelled.",
                "data_fetch_finished": "Loading Options Finished.",
                "cancelling_data_fetch": "Cancelling Option Loading...",
                "fetching_data": "Loading Options...",
                "converting": "Processing...",
                "no_internet": "No internet connection.",
            },
            "status_label_icons": {
                "download_failed": "dialog-error",
                "download_cancelled": "media-playback-stop",
                "download_finished": "emblem-default",
                "cancelling_download": "media-playback-stop",
                "downloading": "emblem-downloads",
                "extracting_urls": "view-refresh",
                "data_fetch_failed": "dialog-error",
                "data_fetch_cancelled": "media-playback-stop",
                "data_fetch_finished": "emblem-default",
                "cancelling_data_fetch": "media-playback-stop",
                "fetching_data": "view-refresh",
                "converting": "emblem-downloads",
                "no_internet": "network-offline",
            },
            "tab_text": {
                "download_failed": "Failed",
                "download_cancelled": "Cancelled",
                "download_finished": "Finished",
                "cancelling_download": "Cancelling",
                "downloading": "Downloading",
                "extracting_urls": "Analyzing",
                "data_fetch_failed": "Failed",
                "data_fetch_cancelled": "Cancelled",
                "data_fetch_finished": "Finished",
                "cancelling_data_fetch": "Cancelling",
                "fetching_data": "Loading Options",
                "converting": "Downloading",
                "no_internet": "Failed",
            },
            "tab_icons": {
                "download_failed": "dialog-error",
                "download_cancelled": "media-playback-stop",
                "download_finished": "emblem-default",
                "cancelling_download": "media-playback-stop",
                "downloading": "emblem-downloads",
                "extracting_urls": "view-refresh",
                "data_fetch_failed": "dialog-error",
                "data_fetch_cancelled": "media-playback-stop",
                "data_fetch_finished": "emblem-default",
                "cancelling_data_fetch": "media-playback-stop",
                "fetching_data": "view-refresh",
                "converting": "emblem-downloads",
                "no_internet": "dialog-error",
            },
            "window_titles": {
                "error": "Error - Tab <tab_name>",
            },
            "button_text": {
                "download": {"default": "&Download", "secondary": "Cancel &Downloading"},
                "refresh": {"default": "&Load Options", "secondary": "Cancel Option &Loading"},
            },
            "formats": {
                "mp4": "Video",
                "mp3": "Audio",
            },
            "preferred-resolutions": {
                0:  "Best",
                2160: "2160p",
                1440: "1440p",
                1920: "1920p",
                1080: "1080p",
                720: "720p",
                480: "480p",
                360: "360p",
            },
            "preferred-bitrates": {
                0:  "Best",
                320: "320 kbps",
                256: "256 kbps",
                192: "192 kbps",
                160: "160 kbps",
                128: "128 kbps",
                96: "96 kbps",
                64: "64 kbps",
            },
        }
        self.DEFAULT_SETTINGS = {
            "remember-tab-settings": {"value": True, "type": bool},
            "remove-downloaded-urls": {"value": True, "type": bool},
            "preferred-resolution": {"value": 1440, "type": int},
            "preferred-bitrate": {"value": 192, "type": int},
            "download-format": {"value": "mp4", "type": str},
            "crop-thumbnails": {"value": False, "type": bool},
            "embed-subtitles": {"value": True, "type": bool},
            "download-dir": {
                "value": QStandardPaths.writableLocation(QStandardPaths.DownloadLocation),
                "type": str
            },
            "window-geometry": {"value": None, "type": None},
            "window-state": {"value": None, "type": None},
        }


    def save_setting(self, setting, value, force=False):
        old_value = self.value(setting)
        if force or old_value != value:
            self.setValue(setting, value)


    def load_setting(self, setting):
        if setting in self.DEFAULT_SETTINGS:
            default_value = self.DEFAULT_SETTINGS[setting]["value"]
            value_type = self.DEFAULT_SETTINGS[setting]["type"]
            
            return self.value(setting, type=value_type, defaultValue=default_value)
        else:
            return self.value(setting)