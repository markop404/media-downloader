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


import socket
import re
import os

import yt_dlp

from ..utils import get_value_if_exists


class Downloader(yt_dlp.YoutubeDL):
    def __init__(self):
        super().__init__()

        self.DOWNLOAD_ATTEMPTS = 2
        self.DNS = ("1.1.1.1", 53)


    def _download(
        self,
        urls,
        download_dest="",
        download_progress_func=None,
        url_progress_func=None,
        postprocessor_progress_func=None,
        file_type="mp4",
        subtitle_lang=None,
        quality=None,
        embed_subtitles=True,
        crop_thumbnails=False,
    ):
        self.params = {
            "quiet": True,
            "noplaylist": True,
            "outtmpl": os.path.join(download_dest, "%(title)s.%(ext)s"),
            "windowsfilenames": True,
            "postprocessors": [
                {"key": "FFmpegMetadata"},
                {"key": "EmbedThumbnail", "already_have_thumbnail": False}
            ],
            "writethumbnail": True,
        }
        pending_urls = set(urls)
        failed_urls = set()
        processed_url_count = 0
        total_url_count = len(urls)
        errors = set()

        if download_progress_func:
            self.params["progress_hooks"] = [
                lambda data, progress_hook=download_progress_hook: 
                    self.download_progress_hook(data, progress_hook, processed_url_count, total_url_count)
            ]
        
        if postprocessor_progress_func:
            self.params["postprocessor_hooks"] = [
                lambda data: postprocessor_progress_hook(processed_url_count, total_url_count)
            ]

        if crop_thumbnails:
            self.params["postprocessor_args"]["thumbnailsconvertor+ffmpeg_o"] = [
                "-c:v", "png", "-vf", "crop=ih"
            ]
        
        if subtitle_lang:
            self.params["writesubtitles"] = True
            self.params["subtitleslangs"] = subtitle_lang
            if embed_subtitles:
                self.params["postprocessors"].append({"key": "FFmpegEmbedSubtitle"})

        if file_type == "mp4":
            self.params["format"] = "bestvideo+bestaudio"
            self.params["merge_output_format"] = "mp4"
            if quality:
                self.params["format_sort"] = ["fps", "abr", f"res:{quality}"]
        
        elif file_type == "mp3":
            self.params["postprocessors"] = [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3"
                }
            ] + self.params["postprocessors"]
            self.params["format"] = "bestaudio"
            if quality:
                self.params["format_sort"] = [f"abr:{quality}"]

        for attempt in range(self.DOWNLOAD_ATTEMPTS):
            for url in pending_urls:
                try:
                    ydl.download(url)
                    processed_url_count += 1
                    failed_urls.discard(url)
                except yt_dlp.utils.DownloadError as e:
                    print(e)
                    errors.add(e)
                    if not self.internet_connection():
                        return failed_urls, errors, False
                    failed_urls.add(url)
                    url = ""

                if url_progress_func:
                    url_progress_func(processed_url_count, total_url_count, url)

            if failed_urls:
                if attempt == 1:
                    basic_ydl_config = {}
                    if "progress_hooks" in self.params:
                        basic_ydl_config["progress_hooks"] = self.params["progress_hooks"]
                    if "postprocessor_hooks" in self.params:
                        basic_ydl_config["postprocessor_hooks"] = self.params["postprocessor_hooks"]
                    self.params = basic_ydl_config
                pending_urls = failed_urls

        return failed_urls, errors, True


    def extract_urls(self, urls, url_progress_func=None):
        self.params = {
            "extract_flat": "in_playlist",
            "quiet": True,
            "noplaylist": True,
        }
        pending_urls = set(urls)
        failed_urls = set()
        extracted_urls = set()
        processed_url_count = 0
        total_url_count = len(urls)
        errors = set()

        for attempt in range(self.DOWNLOAD_ATTEMPTS):
            for url in pending_urls:
                try:
                    url_data = self.extract_info(url, download=False)
                    if entries := get_value_if_exists("entries", url_data):
                        for entry in entries:
                            if entry_url := get_value_if_exists("url", entry):
                                extracted_urls.add(entry["url"])
                    else:
                        extracted_urls.add(url)
                    processed_url_count += 1
                    failed_urls.discard(url)
                except yt_dlp.utils.DownloadError as e:
                    print(e)
                    errors.add(e)
                    if not self.internet_connection():
                        return extracted_urls, failed_urls, errors, False
                    failed_urls.add(url)
                    url = ""

                if url_progress_func:
                    url_progress_func(processed_url_count, total_url_count, url)

            if failed_urls:
                pending_urls = failed_urls
        
        return extracted_urls, failed_urls, errors, True
            

    def fetch_pretty_data(self, urls, url_progress_func=None):
        self.params = {
            "quiet": True,
            "noplaylist": True,
            "writesubtitles": True,
            "allsubtitles": True,
            "extract_flat": "in_playlist",
        }
        current_urls = set(urls)
        pending_urls = set()
        total_url_count = len(current_urls)
        processed_url_count = 0
        errors = set()
        all_bitrates = set()
        all_resolutions = set()
        subtitles = {}

        for attempt in range(self.DOWNLOAD_ATTEMPTS + 1):
            for url in current_urls:
                try:
                    url_data = self.extract_info(url, download=False)
                    if entries := get_value_if_exists(url_data, "entries"):
                        for entry in entries:
                            if entry_url := get_value_if_exists(entry, "url"):
                                pending_urls.add(entry_url)
                                total_url_count += 1
                    else:
                        if get_value_if_exists(url_data, "formats"):
                            bitrates = set()
                            resolutions = set()

                            for _format in url_data["formats"]:
                                if get_value_if_exists(_format, "vcodec"):
                                    if _format["vcodec"] == "none":
                                        if get_value_if_exists(_format, "abr"):
                                            bitrate = _format["abr"]
                                            if bitrate and bitrate != "0":
                                                bitrates.add(int(bitrate))
                                    elif get_value_if_exists(_format, "format_note"):
                                        if resolution_search := re.search(r"([0-9]+)p", _format["format_note"]):
                                            resolutions.add(int(resolution_search.group(1)))

                            if not all_bitrates:
                                all_bitrates = bitrates
                            else:
                                all_bitrates.intersection_update(bitrates)
                            if not all_resolutions:
                                all_resolutions = resolutions
                            else:
                                all_resolutions.intersection_update(resolutions)

                        if subtitle_data := get_value_if_exists(url_data, "subtitles"):
                            for subtitle_lang, subtitle_details in subtitle_data.items():
                                if get_value_if_exists(subtitle_details, "name"):
                                    subtitles[subtitle_lang] = subtitle_details["name"]

                    pending_urls.remove(url)
                    processed_url_count += 1
                except yt_dlp.utils.DownloadError as e:
                    print(e)
                    errors.add(e)
                    if not self.internet_connection():
                        return {}, {}, failed_urls, errors, False
                    url = ""
            
                if url_progress_func:
                    url_progress_func(processed_url_count, total_url_count, url)

            current_urls = pending_urls

        pretty_data = {
            "bitrates": sorted(all_bitrates, reverse=True),
            "resolutions": sorted(all_resolutions, reverse=True),
            "subtitles": dict(sorted(subtitles.items(), key=lambda item: item[1])),
        }

        return pretty_data, failed_urls, errors, True


    def download_progress_hook(self, progress_data, progress_func, processed_url_count, total_url_count):
        percentage = None
        if progress_data["status"] == "downloading":            
            if "downloaded_bytes" in progress_data and "total_bytes" in progress_data:
                if isinstance(progress_data["downloaded_bytes"], int) and isinstance(progress_data["total_bytes"], int):
                    percentage = int((progress_data["downloaded_bytes"] / progress_data["total_bytes"]) * 100)
            elif "fragment_index" in progress_data and "fragment_count" in progress_data:
                if isinstance(progress_data["fragment_index"], int) and isinstance(progress_data["fragment_count"], int):
                    percentage = int((progress_data["fragment_index"] / progress_data["fragment_count"]) * 100)
                    
        progress_func(percentage, processed_url_count, total_url_count)


    def internet_connection(self):
        try:
            socket.create_connection(self.DNS).close()
            return True
        except BaseException as e:
            print(e)
            return False