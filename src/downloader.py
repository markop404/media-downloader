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

from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError


class Downloader:
    def __init__(
        self,
        download_progress_func=None,
        url_downloaded_func=None,
        url_extracted_func=None,
        url_fetched_func=None,
        conversion_progress_func=None
    ):
        self.logs = self.Logs()
        self.metadata = self.Metadata()
        self.cache = self.Cache()
        self.progress_func = self.ProgressFunc(
            download=download_progress_func,
            downloaded=url_downloaded_func,
            extracted=url_extracted_func,
            fetched=url_fetched_func,
            conversion=conversion_progress_func
        )

    def download(
        self,
        urls=None,
        download_dir="",
        file_type="mp4",
        subtitles=None,
        quality=None,
        embed_subtitles=True,
        crop_thumbnails=False,
    ):
        if self.cache.available(urls) or not urls:
            urls = self.cache.extracted_urls
        self.logs.__init__(pending_urls=urls.copy())
        pending_urls = urls.copy()
        processed_url_count = 0
        params = {
            "quiet": True,
            "noplaylist": True,
            "noprogress": True,
            "outtmpl": {
                "default": os.path.join(download_dir, "%(title)s.%(ext)s"),
                "pl_thumbnail": "",
            },
            "windowsfilenames": True,
            "postprocessors": [
                {
                    "key": "FFmpegMetadata",
                    "add_chapters": True,
                    "add_infojson": "if_exists",
                    "add_metadata": True,
                },
                {
                    "key": "EmbedThumbnail",
                    "already_have_thumbnail": False,
                },
            ],
            "writethumbnail": True
        }
        if self.progress_func.download:
            params["progress_hooks"] = [
                lambda data: self.progress_func.download_hook(data, processed_url_count, self.logs.total_url_count)
            ]
        if self.progress_func.conversion:
            params["postprocessor_hooks"] = [
                lambda _: self.progress_func.conversion(processed_url_count, self.logs.total_url_count)
            ]
        if crop_thumbnails:
            params["postprocessor_args"]["thumbnailsconvertor+ffmpeg_o"] = ["-vf", "crop=ih"]
        if subtitles:
            params["writesubtitles"] = True
            params["subtitleslangs"] = list(subtitles)
            if embed_subtitles:
                params["postprocessors"].append(
                    {"key": "FFmpegEmbedSubtitle", "already_have_subtitle": False}
                )
        if file_type == "mp4":
            params["format"] = "bestvideo*+bestaudio/best"
            params["merge_output_format"] = "mp4"
            if quality:
                params["format_sort"] = [f"res:{quality}"]
        elif file_type == "mp3":
            params["format"] = "bestaudio/best"
            params["final_ext"] = "mp3"
            params["postprocessors"] = [
                {
                    "key": "FFmpegExtractAudio",
                    "nopostoverwrites": False,
                    "preferredcodec": "mp3",
                    "preferredquality": "5",
                }
            ] + params["postprocessors"]
            if quality:
                params["format_sort"] = [f"abr:{quality}"]

        downloader = YoutubeDL(params)

        for attempt in range(self.DOWNLOAD_ATTEMPTS):
            for url in pending_urls:
                try:
                    downloader.download(url)
                except DownloadError as e:
                    print(e)
                    self.check_internet()
                    self.logs.errors.add(e)
                    url = None
                else:
                    processed_url_count += 1
                    self.logs.pending_urls.discard(url)
                if self.progress_func.downloaded:
                    self.progress_func.downloaded(processed_url_count, self.logs.total_url_count, url)

            if self.logs.pending_urls and attempt != self.DOWNLOAD_ATTEMPTS:
                pending_urls = self.logs.pending_urls.copy()
            else:
               break


    def extract_urls(self, urls):
        if self.cache.available(urls):
            self.logs.clear()
            return
        downloader = YoutubeDL({
            "extract_flat": "in_playlist",
            "quiet": True,
            "noplaylist": True
        })
        self.logs.__init__(pending_urls=urls.copy())
        extracted_urls = set()
        pending_urls = urls.copy()
        processed_url_count = 0

        for attempt in range(self.DOWNLOAD_ATTEMPTS):
            for url in pending_urls:
                try:
                    url_data = downloader.extract_info(url, download=False)
                except DownloadError as e:
                    print(e)
                    self.check_internet()
                    self.logs.errors.add(e)
                else:
                    if url_entries := self.get_value_if_exists("entries", url_data, list):
                        for entry in url_entries:
                            if url_entry := self.get_value_if_exists("url", entry, str):
                                extracted_urls.add(url_entry)
                    else:
                        extracted_urls.add(url)
                    processed_url_count += 1
                    self.logs.pending_urls.discard(url)
                if self.progress_func.extracted:
                    self.progress_func.extracted(processed_url_count, self.logs.total_url_count)

            if self.logs.pending_urls and attempt != self.DOWNLOAD_ATTEMPTS:
                pending_urls = self.logs.pending_urls.copy()
            else:
                break
        
        self.cache.__init__(urls=urls.copy(), extracted_urls=extracted_urls, failed_urls=self.logs.pending_urls)
            

    def fetch_metadata(self, urls):
        downloader = YoutubeDL({
            "quiet": True,
            "noplaylist": True,
            "writesubtitles": True,
            "allsubtitles": True,
            "extract_flat": "in_playlist"
        })
        self.logs.__init__(pending_urls=urls.copy())
        pending_urls = urls.copy()
        extracted_urls = set()
        processed_url_count = 0
        all_bitrates = set()
        all_resolutions = set()
        all_subtitles = {}

        for attempt in range(2):
            for url in pending_urls:
                try:
                    url_data = downloader.extract_info(url, download=False)
                except DownloadError as e:
                    print(e)
                    self.check_internet()
                    self.logs.errors.add(e)
                else:
                    if url_entries := self.get_value_if_exists("entries", url_data, list):
                        for entry in url_entries:
                            if url_entry := self.get_value_if_exists("url", entry, str):
                                self.logs.pending_urls.add(url_entry)
                                extracted_urls.add(url_entry)
                                self.logs.total_url_count += 1
                    else:
                        extracted_urls.add(url)
                        if formats := self.get_value_if_exists("formats", url_data, list):
                            bitrates = set()
                            resolutions = set()
                            
                            for _format in formats:
                                if (
                                    (format_note := self.get_value_if_exists("format_note", _format, str)) and
                                    (resolution_search := re.search(r"([0-9]+)p", format_note))
                                ):
                                    resolutions.add(int(resolution_search.group(1)))
                                if format_abr := self.get_value_if_exists("abr", _format, float):
                                    bitrates.add(int(format_abr))

                            if bitrates and not all_bitrates:
                                all_bitrates = bitrates
                            else:
                                all_bitrates.intersection_update(bitrates)
                            if resolutions and not all_resolutions:
                                all_resolutions = resolutions
                            else:
                                all_resolutions.intersection_update(resolutions)

                        if subtitles := self.get_value_if_exists("subtitles", url_data, dict):
                            for subtitle_lang, subtitle_details in subtitles.items():
                                for subtitle_detail in subtitle_details:
                                    if subtitle_name := self.get_value_if_exists("name", subtitle_detail, str):
                                        all_subtitles[subtitle_lang] = subtitle_name
                                        break

                    self.logs.pending_urls.discard(url)
                    processed_url_count += 1

                if self.progress_func.fetched:
                    self.progress_func.fetched(processed_url_count, self.logs.total_url_count)

            if self.logs.pending_urls and attempt != self.DOWNLOAD_ATTEMPTS:
                pending_urls = self.logs.pending_urls.copy()
            else:
                break

        self.cache.__init__(urls= urls.copy(), extracted_urls=extracted_urls, failed_urls=self.logs.pending_urls)

        resolutions = {}
        for resolution in sorted(all_resolutions, reverse=True):
            resolutions[resolution] = f"{resolution}p"
        bitrates = {}
        for bitrate in sorted(all_bitrates, reverse=True):
            bitrates[bitrate] = f"{bitrate} kbps"
        subtitles = dict(sorted(all_subtitles.items(), key=lambda i: i[1]))
        self.metadata.__init__(resolutions=resolutions, bitrates=bitrates, subtitles=subtitles)
        

    class Logs:
        def __init__(self, pending_urls=set(), errors=set()):
            self.pending_urls = pending_urls
            self.total_url_count = len(pending_urls)
            self.errors = errors

        def all_failed(self):
            return len(self.pending_urls) == self.total_url_count and self.errors

        def clear(self):
            self.__init__()


    class Metadata:
        def __init__(self, resolutions={}, bitrates={}, subtitles={}):
            self.resolutions = resolutions
            self.bitrates = bitrates
            self.subtitles = subtitles

        def exists(self):
            return self.resolutions or self.bitrates

        def clear(self):
            self.__init__()


    class Cache:
        def __init__(self, urls=set(), extracted_urls=set(), failed_urls=set()):
            self.urls = urls
            self.extracted_urls = extracted_urls
            self.extracted_url_count = len(extracted_urls)
            self.failed_urls = failed_urls

        def available(self, urls):
            return urls == self.urls


    class ProgressFunc:
        def __init__(self, download=None, downloaded=None, extracted=None, fetched=None, conversion=None):
            self.download = download
            self.downloaded = downloaded
            self.extracted = extracted
            self.fetched = fetched
            self.conversion = conversion

        def download_hook(self, progress_data, processed_url_count, total_url_count):
            if percentage := Downloader.get_value_if_exists("_percent", progress_data, float):
                percentage = int(round(percentage, 0))
            else:
                percentage = None       
            self.download(percentage, processed_url_count, total_url_count)


    def check_internet(self):
        try:
            socket.create_connection(self.DNS, timeout=5).close()
        except BaseException as e:
            raise self.NoInternet(e)
        

    @staticmethod
    def get_value_if_exists(value, _dict, _type=None):
        if value in _dict:
            value = _dict[value]
            if _type and isinstance(value, _type):
                return value
            elif not _type:
                return value


    class NoInternet(BaseException): pass


    DOWNLOAD_ATTEMPTS = 2
    DNS = ("1.1.1.1", 53)