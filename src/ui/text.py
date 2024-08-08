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
        "downloading": "Downloading... (<repetition>/<repetitions>)",
        
        "extracting_urls": "Analyzing URLs... (<repetition>/<repetitions>)",
        
        "refresh_failed": "Data Refresh Failed.",
        "refresh_cancelled": "Data Refresh Cancelled.",
        "refresh_finished": "Data Refresh Finished.",
        "refreshing": "Refreshing Data... (<repetition>/<repetitions>)",
        "cancelling_refresh": "Cancelling Data Refresh...",

        "converting": "Processing... (<repetition>/<repetitions>)",
    }

    WINDOW_TITLES = {
        "root": APP_NAME,
        "error": f"Error - {APP_NAME}",
        "about": f"About {APP_NAME}",
    }

    BUTTON_TEXT = {
        "download": {"default": "Download", "secondary": "Cancel Download"},
        "refresh": {"default": "Refresh", "secondary": "Cancel Refresh"},
    }

    FORMATS = {
        "Audio": "audio",
        "Video": "video",
    }