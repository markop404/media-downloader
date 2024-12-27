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
        self.config = {
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
        youtubedl_config = {
            "outtmpl": f"{download_location}/%(title)s.%(ext)s",
            "postprocessors": [
                {"key": "FFmpegMetadata"},
                {"key": "EmbedThumbnail", "already_have_thumbnail": False}
            ],
            "writethumbnail": True,
            "postprocessor_args": {},
        }.update(self.config)
        errors = set()
        failed_urls = set()
        TOTAL_URL_COUNT = len(urls)
        processed_url_count = 0

        if on_progress:
            youtubedl_config["progress_hooks"] = [lambda data: on_progress(data, processed_url_count, TOTAL_URL_COUNT)]
        
        if postprocessor_progress:
            youtubedl_config["postprocessor_hooks"] = [lambda data: postprocessor_progress(data, processed_url_count, TOTAL_URL_COUNT)]

        if crop_thumbnails:
            youtubedl_config["postprocessor_args"]["thumbnailsconvertor+ffmpeg_o"] = ["-c:v", "png", "-vf", "crop=ih"]
        
        if subtitle_lang:
            youtubedl_config["writesubtitles"] = True
            youtubedl_config["subtitleslangs"] = subtitle_lang
            if embed_subtitles:
                youtubedl_config["postprocessors"].append({"key": "FFmpegEmbedSubtitle"})

        if file_type == "mp4":
            youtubedl_config["format"] = "bestvideo+bestaudio"
            youtubedl_config["merge_output_format"] = "mp4"
            if quality:
                youtubedl_config["format_sort"] = ["fps", "abr", f"res:{quality}"]
        
        elif file_type == "mp3":
            youtubedl_config["postprocessors"] = [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3"
                }
            ] + youtubedl_config["postprocessors"]
            youtubedl_config["format"] = "bestaudio"
            if quality:
                youtubedl_config["format_sort"] = [f"abr:{quality}"]


        with yt_dlp.YoutubeDL(youtubedl_config) as ydl:
            for url in urls:
                try:
                    ydl.download(url)
                    processed_url_count += 1 
                except yt_dlp.utils.DownloadError as e:
                    print(e)
                    errors.add(e)
                    if not self.check_internet_connection():
                        return failed_urls, False
                    failed_urls.add(url)
                
                if on_url_progress:
                    on_url_progress(url, processed_url_count, TOTAL_URL_COUNT)

        if failed_urls:
            new_youtubedl_config = {}
            if "progress_hooks" in youtubedl_config:
                new_youtubedl_config["progress_hooks"] = youtubedl_config["progress_hooks"]
            if "postprocessor_hooks" in youtubedl_config:
                new_youtubedl_config["postprocessor_hooks"] = youtubedl_config["postprocessor_hooks"]

            with yt_dlp.YoutubeDL(new_youtubedl_config) as ydl:
                for url in failed_urls:
                    try:
                        ydl.download(url)
                        failed_urls.remove(url)
                        processed_url_count += 1
                    except yt_dlp.utils.DownloadError as e:
                        print(e)
                        errors.add(e)
                        if not self.check_internet_connection():
                            return failed_urls, False

                    if on_url_progress:
                        on_url_progress(url, processed_url_count, TOTAL_URL_COUNT)

        return failed_urls, True, errors


    def extract_urls(self, urls, on_progress=None):
        if urls != self.cache["original_urls"]:
            processed_url_count = 0
            data = {}
            total_url_count = len(urls)
            extracted_urls = set()
            failed_urls = set()
            errors = set()
            config = self.config
            config.update({
                "extract_flat": True,
            })

            with yt_dlp.YoutubeDL(config) as ydl:
                for url in urls:
                    try:
                        temp_urls, temp_data = _extract_urls(url, ydl)
                        extracted_urls.update(temp_urls)
                        if temp_data:
                            data.update(temp_data)
                        processed_url_count += 1
                    except yt_dlp.utils.DownloadError as e:
                        print(e)
                        errors.add(e)
                        if not self.check_internet_connection():
                            return extracted_urls, failed_urls, False, errors
                        failed_urls.add(url)

                    if on_progress:
                        on_progress(processed_url_count, total_url_count)

            if failed_urls:
                with yt_dlp.YoutubeDL(config) as ydl:
                    for url in failed_urls:
                        try:
                            extracted_urls.update(self._extract_urls(url, ydl))
                            processed_url_count += 1
                            failed_urls.discard(url)
                        except yt_dlp.utils.DownloadError as e:
                            print(e)
                            errors.add(e)
                            if not self.check_internet_connection():
                                return extracted_urls, failed_urls, False, errors

                        if on_progress:
                            on_progress(processed_url_count, total_url_count)

            self.cache["original_urls"] = urls
            self.cache["extracted_urls"] = extracted_urls
            self.cache["data"] = data

            return extracted_urls, failed_urls, True, errors
        else:
            return self.cache["extracted_urls"], set(), True, list()


    def _extract_urls(self, url, ydl):
        urls = set()

        data = ydl.extract_data(url, download=False)
        if "entries" in data:
            for entry in data["entries"]:
                urls.add(entry["url"])
            data = None
        else:
            data = {data["webpage_url"]: data}
            urls.add(url)
        
        return urls, data


    def fetch_data(self, urls, on_progress=None):
        data = []
        failed_urls = []
        config = self.config
        config.update({
            "writesubtitles": True,
            "allsubtitles": True,
        })

        TOTAL_URL_COUNT = len(urls)
        processed_url_count = 0
        errors = set()

        with yt_dlp.YoutubeDL(config) as ydl:
            for url in urls:
                if url not in self.cache["data"]
                try:
                    data += self._extract_data(ydl, url)
                    processed_url_count += 1
                except yt_dlp.utils.DownloadError as e:
                    print(e)
                    errors.add(e)
                    if not self.check_internet_connection():
                        return data, failed_urls, False
                    failed_urls.append(url)

                if on_progress:
                    on_progress(processed_url_count, TOTAL_URL_COUNT)

        if failed_urls:
            with yt_dlp.YoutubeDL(config) as ydl:
                for url in failed_urls:
                    try:
                        data += self._extract_data(ydl, url)
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
                        if resolution_search := search(r"([0-9]+)p", _format["format_note"]):
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