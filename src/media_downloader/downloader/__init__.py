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
        self.clear_cache()
        self.ydl_config = {
            "quiet": True,
            "noplaylist": True,
        }
    

    def clear_cache(self):
        self.cache = {
            "original_urls": set(),
            "converted_urls": set(),
            "data": {},
        }


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
            "windowsfilenames": True,
            "postprocessors": [
                {"key": "FFmpegMetadata"},
                {"key": "EmbedThumbnail", "already_have_thumbnail": False}
            ],
            "postprocessor_args": {},
            "writethumbnail": True,
        })
        urls = set(urls)
        remaining_urls = urls.copy()
        failed_urls = set()
        processed_url_count = 0
        total_url_count = len(urls)
        errors = set()

        if on_progress:
            ydl_config["progress_hooks"] = [lambda data: on_progress(data, processed_url_count, total_url_count)]
        
        if postprocessor_progress:
            ydl_config["postprocessor_hooks"] = [lambda data: postprocessor_progress(data, processed_url_count, total_url_count)]

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
                for url in remaining_urls:
                    try:
                        ydl.download(url)
                        processed_url_count += 1
                        failed_urls.discard(url)
                    except yt_dlp.utils.DownloadError as e:
                        print(e)
                        errors.add(e)
                        failed_urls.add(url)
                        if not self.check_internet_connection():
                            return failed_urls, errors, False
                    
                    if on_url_progress:
                        on_url_progress(url, processed_url_count, total_url_count)

            if remaining_urls:
                new_ydl_config = {}
                if "progress_hooks" in ydl_config:
                    new_ydl_config["progress_hooks"] = ydl_config["progress_hooks"]
                if "postprocessor_hooks" in ydl_config:
                    new_ydl_config["postprocessor_hooks"] = ydl_config["postprocessor_hooks"]
                ydl_config = new_ydl_config
                remaining_urls = failed_urls

        return failed_urls, errors, True


    def extract_urls(self, urls, on_progress=None, force=False):
        urls = set(urls)
        if urls != self.cache["original_urls"] or force:
            remaining_urls = urls.copy()
            failed_urls = set()
            extracted_urls = set()
            processed_url_count = 0
            total_url_count = len(urls)
            self.cache["original_urls"] = urls
            data = {}
            errors = set()
            ydl_config = self.ydl_config
            ydl_config.update({"extract_flat": "in_playlist"})

            for _ in range(2):
                with yt_dlp.YoutubeDL(ydl_config) as ydl:
                    for url in remaining_urls:
                        try:
                            new_data = ydl.extract_info(url, download=False)
                            if "entries" in new_data:
                                for entry in new_data["entries"]:
                                    extracted_urls.add(entry["url"])
                            else:
                                self.cache["data"][url] = new_data
                                extracted_urls.add(url)
                            processed_url_count += 1
                            failed_urls.discard(url)
                        except yt_dlp.utils.DownloadError as e:
                            print(e)
                            errors.add(e)
                            failed_urls.add(url)
                            if not self.check_internet_connection():
                                return extracted_urls, failed_urls, errors, False 

                        if on_progress:
                            on_progress(processed_url_count, total_url_count)

                if failed_urls:
                    remaining_urls = failed_urls
            
            self.cache["extracted_urls"] = extracted_urls
            return extracted_urls, failed_urls, errors, True
        else:
            return self.cache["extracted_urls"], set(), set(), True


    def fetch_pretty_data(self, urls, on_progress=None):
        urls = set(urls)
        remaining_urls = urls.copy()
        failed_urls = set()
        processed_url_count = 0
        total_url_count = len(urls)
        data = []
        errors = set()
        ydl_config = self.ydl_config
        ydl_config.update({
            "writesubtitles": True,
            "allsubtitles": True,
        })

        for _ in range(2):
            with yt_dlp.YoutubeDL(ydl_config) as ydl:
                for url in remaining_urls:
                    if url in self.cache["data"] and self.cache["data"][url]:
                        data.append(self.cache["data"][url])
                    else:
                        try:
                            new_data = ydl.extract_info(url, download=False)
                            if "entries" in new_data:
                                data += new_data["entries"]
                            else:
                                data.append(new_data)
                            processed_url_count += 1
                            failed_urls.discard(url)
                        except yt_dlp.utils.DownloadError as e:
                            print(e)
                            errors.add(e)
                            failed_urls.add(url)
                            if not self.check_internet_connection():
                                return {}, {}, failed_urls, errors, False

                    if on_progress:
                        on_progress(processed_url_count, total_url_count)
            if failed_urls:
                remaining_urls = failed_urls
                
        all_bitrates = set()
        all_resolutions = set()
        subtitles = {}

        for url_data in data:
            if "formats" in url_data:
                formats = url_data["formats"]
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

            if "subtitles" in url_data:
                if subtitle_data := url_data["subtitles"]:
                    for subtitle_lang, subtitle_details in subtitle_data.items():
                        if isinstance(subtitle_details, dict) and "name" in subtitle_details:
                            subtitles[subtitle_lang] = subtitle_details["name"]

        all_bitrates = sorted(all_bitrates, reverse=True)
        all_resolutions = sorted(all_resolutions, reverse=True)
        qualities = {"bitrates": all_bitrates, "resolutions": all_resolutions}
        subtitles = dict(sorted(subtitles.items(), key=lambda item: item[1]))

        return qualities, subtitles, failed_urls, errors, True


    def check_internet_connection(self):
        try:
            requests.get("https://markopejic.com", timeout=10)
            return True
        except BaseException as e:
            print(e)
            return False