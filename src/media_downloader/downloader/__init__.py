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
import requests
import re

import yt_dlp


class Downloader():
    def __init__(self):
        self.cache = {
            "original_urls": None,
            "converted_urls": None,
            "data": None,
        }
        self.ydl_config = {
            "quiet": True,
            "noplaylist": True,
        }
    

    def clear_cache(self):
        for key in self.cache:
            self.cache[key] = None


    def download(
        self,
        urls,
        download_location="",
        on_progress=None,
        on_url_progress=None,
        file_type="mp4",
        subtitle_lang=None,
        quality=None,
        postprocessor_progress=None,
        embed_subtitles=True,
        crop_thumbnails=False,
    ):
        ydl_config = self.ydl_config
        ydl_config.update({
            "outtmpl": f"{download_location}/%(title)s.%(ext)s",
            "postprocessors": [
                {"key": "FFmpegMetadata"},
                {"key": "EmbedThumbnail", "already_have_thumbnail": False}
            ],
            "writethumbnail": True,
            "postprocessor_args": {},
        })
        urls = set(urls)
        remaining_urls = urls
        TOTAL_URL_COUNT = len(urls)
        processed_url_count = 0
        errors = set()

        if on_progress:
            ydl_config["progress_hooks"] = [lambda data: on_progress(data, processed_url_count, TOTAL_URL_COUNT)]
        
        if postprocessor_progress:
            ydl_config["postprocessor_hooks"] = [lambda data: postprocessor_progress(data, processed_url_count, TOTAL_URL_COUNT)]

        if crop_thumbnails:
            ydl_config["postprocessor_args"]["thumbnailsconvertor+ffmpeg_o"] = ["-c:v", "png", "-vf", "crop=ih"]
        
        if subtitle_lang:
            ydl_config["writesubtitles"] = True
            ydl_config["subtitleslangs"] = subtitle_lang
            if embed_subtitles:
                ydl_config["postprocessors"].append({"key": "FFmpegEmbedSubtitle"})

        if file_type == "mp4":
            ydl_config["format"] = "bestvideo+bestaudio"
            ydl_config["merge_output_format"] = "mp4"
            if quality:
                ydl_config["format_sort"] = ["fps", "abr", f"res:{quality}"]
        
        elif file_type == "mp3":
            ydl_config["postprocessors"] = [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3"
                }
            ] + ydl_config["postprocessors"]
            ydl_config["format"] = "bestaudio"
            if quality:
                ydl_config["format_sort"] = [f"abr:{quality}"]

        for _ in range(2):
            with yt_dlp.YoutubeDL(ydl_config) as ydl:
                for url in urls:
                    try:
                        ydl.download(url)
                        processed_url_count += 1
                        remaining_urls.discard(url)
                    except yt_dlp.utils.DownloadError as e:
                        print(e)
                        errors.add(e)
                        if not self.check_internet_connection():
                            return remaining_urls, False
                    
                    if on_url_progress:
                        on_url_progress(url, processed_url_count, TOTAL_URL_COUNT)

            if remaining_urls:
                new_ydl_config = {}
                if "progress_hooks" in ydl_config:
                    new_ydl_config["progress_hooks"] = ydl_config["progress_hooks"]
                if "postprocessor_hooks" in ydl_config:
                    new_ydl_config["postprocessor_hooks"] = ydl_config["postprocessor_hooks"]
                ydl_config = new_ydl_config

        return invalid_urls, True, errors


    def extract_urls(self, urls, on_progress=None, force=False):
        urls = set(urls)
        if urls != self.cache["original_urls"] or force:
            processed_url_count = 0
            TOTAL_URL_COUNT = len(urls)
            data = {}
            extracted_urls = set()
            remaining_urls = urls
            errors = set()
            ydl_config = self.ydl_config
            ydl_config.update({
                "extract_flat": True,
            })

            for _ in range(2):
                with yt_dlp.YoutubeDL(ydl_config) as ydl:
                    for url in urls:
                        try:
                            temp_urls, temp_data = self._extract_urls(url, ydl)
                            extracted_urls.update(temp_urls)
                            data.update(temp_data)
                            processed_url_count += 1
                            remaining_urls.discard(url)
                        except yt_dlp.utils.DownloadError as e:
                            print(e)
                            errors.add(e)
                            if not self.check_internet_connection():
                                return extracted_urls, remaining_urls, False, errors

                        if on_progress:
                            on_progress(processed_url_count, TOTAL_URL_COUNT)

                    urls = remaining_urls

            self.cache["original_urls"] = urls
            self.cache["extracted_urls"] = extracted_urls
            self.cache["data"] = data

            return extracted_urls, remaining_urls, True, errors
        else:
            return self.cache["extracted_urls"], set(), True, list()


    def _extract_urls(self, url, ydl):
        urls = set()

        data = ydl.extract_info(url, download=False)
        if "entries" in data:
            for entry in data["entries"]:
                urls.add(entry["url"])
            data = {}
        else:
            data = {data["webpage_url"]: data}
            urls.add(url)
        
        return urls, data


    def fetch_data(self, urls, on_progress=None):
        data = []
        failed_urls = set()
        ydl_config = self.ydl_config
        ydl_config.update({
            "writesubtitles": True,
            "allsubtitles": True,
        })
        TOTAL_URL_COUNT = len(urls)
        processed_url_count = 0
        errors = set()

        with yt_dlp.YoutubeDL(ydl_config) as ydl:
            for url in urls:
                if url not in self.cache["data"]:
                    try:
                        temp_data = self._fetch_data(ydl, url)
                        data.append(temp_data)
                        processed_url_count += 1
                    except yt_dlp.utils.DownloadError as e:
                        print(e)
                        errors.add(e)
                        if not self.check_internet_connection():
                            return data, failed_urls, False
                        failed_urls.add(url)
                else:
                    data.append(self.cache["data"][url])

                if on_progress:
                    on_progress(processed_url_count, TOTAL_URL_COUNT)

        if failed_urls:
            with yt_dlp.YoutubeDL(ydl_config) as ydl:
                for url in failed_urls:
                    try:
                        data.append(self._fetch_data(ydl, url))
                        processed_url_count += 1
                        failed_urls.discard(url)
                    except yt_dlp.utils.DownloadError as e:
                        print(e)
                        errors.add(e)
                        if not self.check_internet_connection():
                            return data, failed_urls, False

                    if on_progress:
                        on_progress(processed_url_count, TOTAL_URL_COUNT)

        return data, failed_urls, True, errors


    def _fetch_data(self, ydl, url):
        data = []
        temp_data = ydl.extract_info(url, download=False)
        
        if "entries" in temp_data:
            data += temp_data["entries"]
        else:
            data.append(temp_data)

        return data


    def extract_pretty_info(self, data_list):
        all_bitrates = set()
        all_resolutions = set()
        subtitles = {}

        for data in data_list:
            if "formats" in data:
                formats = data["formats"]
                bitrates = set()
                resolutions = set()
                
                for _format in formats:
                    if _format["vcodec"] != "none" and "format_note" in _format and "height" in _format:
                        if resolution_search := re.search(r"([0-9]+)p", _format["format_note"]):
                            resolution = int(resolution_search.group(1))
                            resolutions.add(resolution)

                    elif _format["vcodec"] == "none" and "abr" in _format:
                        bitrate = _format["abr"]
                        if bitrate and bitrate != "0":
                            bitrates.add(int(bitrate))

                if not all_bitrates:
                    all_bitrates = bitrates
                else:
                    all_bitrates.intersection_update(bitrates)
                if not all_resolutions:
                    all_resolutions = resolutions
                else:
                    all_resolutions.intersection_update(resolutions)

            if "subtitles" in data:
                if subtitle_data := data["subtitles"]:
                    for subtitle_lang, subtitle_details in subtitle_data.items():
                        if isinstance(subtitle_details, dict) and "name" in subtitle_details:
                            subtitles[subtitle_lang] = subtitle_details["name"]

        all_bitrates = sorted(all_bitrates, reverse=True)
        all_resolutions = sorted(all_resolutions, reverse=True)
        qualities = {"bitrates": all_bitrates, "resolutions": all_resolutions}
        subtitles = dict(sorted(subtitles.items(), key=lambda item: item[1]))

        return qualities, subtitles


    def check_internet_connection(self):
        try:
            requests.get("https://markopejic.com", timeout=10)
            return True
        except BaseException as e:
            print(e)
            return False
    

    def fetch_pretty_data(self, urls, on_progress=None):
        data, failed_urls, exit_status, errors = self.fetch_data(urls, on_progress=on_progress)
        if data:
            qualities, subtitles = self.extract_pretty_info(data)
        
        return qualities, subtitles, failed_urls, exit_status, errors