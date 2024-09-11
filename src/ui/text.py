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


class Text:
    APP_NAME = "Media Downloader"

    STATUS_MESSAGES = {
        "download_failed": "Downloading Failed.",
        "download_cancelled": "Downloading Cancelled.",
        "download_finished": "Downloading Finished.",
        "cancelling_download": "Cancelling Download...",
        "downloading": "Downloading... (<current>/<total>)",
        
        "extracting_urls": "Analyzing URLs... (<current>/<total>)",
        
        "refresh_failed": "Data Refresh Failed.",
        "refresh_cancelled": "Data Refresh Cancelled.",
        "refresh_finished": "Data Refresh Finished.",
        "refreshing": "Refreshing Data... (<current>/<total>)",
        "cancelling_refresh": "Cancelling Data Refresh...",

        "converting": "Processing... (<current>/<total>)",

        "tab_name": "<tab_number>",
        # "tab_downloading": f"{STATUS_MESSAGES['tab_name']} - Downloading <current>/<total>",
        # "tab_refreshing": f"{STATUS_MESSAGES['tab_name']} - Refreshing <current>/<total>",
        # "tab_extracting_urls": f"{STATUS_MESSAGES['tab_name']} - Analyzing <current>/<total>",
    }

    TAB_TITLE_TEXT = {
        "downloading"
    }

    WINDOW_TITLES = {
        "root": APP_NAME,
        "error": f"Error - {APP_NAME}",
    }

    BUTTON_TEXT = {
        "download": {"default": "Download", "secondary": "Cancel Download"},
        "refresh": {"default": "Refresh", "secondary": "Cancel Refresh"},
    }

    FORMATS = {
        "Audio": "audio",
        "Video": "video",
    }