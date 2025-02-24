# Media Downloader - Web video/audio downloader
# Copyright (C) 2024-2025  Marko Pejić

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
from dataclasses import dataclass

import yt_dlp

from ..utils import get_value_if_exists


class Downloader(yt_dlp.YoutubeDL):
    def __init__(self):
        super().__init__()


    def _download(
        self,
        urls,
        download_dir="",
        download_progress_func=None,
        url_progress_func=None,
        conversion_progress_func=None,
        file_type="mp4",
        subtitles=None,
        quality=None,
        embed_subtitles=True,
        crop_thumbnails=False,
    ):
        self.params = {
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
            "writethumbnail": True,
        }
        pending_urls = set(urls)
        processed_url_count = 0
        total_url_count = len(pending_urls)
        logs = self.Logs(pending_urls=pending_urls)

        if download_progress_func:
            self.params["progress_hooks"] = [
                lambda data, progress_func=download_progress_func: 
                    self.download_progress_hook(data, progress_func, processed_url_count, total_url_count)
            ]
        if conversion_progress_func:
            self.params["postprocessor_hooks"] = [
                lambda data: conversion_progress_func(processed_url_count, total_url_count)
            ]
        if crop_thumbnails:
            self.params["postprocessor_args"]["thumbnailsconvertor+ffmpeg_o"] = ["-vf", "crop=ih"]
        if subtitles:
            self.params["writesubtitles"] = True
            self.params["subtitleslangs"] = ",".join(set(subtitles))
            if embed_subtitles:
                self.params["postprocessors"].append(
                    {"key": "FFmpegEmbedSubtitle", "already_have_subtitle": False}
                )
        if file_type == "mp4":
            self.params["format"] = "bestvideo*+bestaudio/best"
            self.params["merge_output_format"] = "mp4"
            if quality:
                self.params["format_sort"] = [f"res:{quality}"]
        elif file_type == "mp3":
            self.params["format"] = "bestaudio/best"
            self.params["final_ext"] = "mp3"
            self.params["postprocessors"] = [
                {
                    "key": "FFmpegExtractAudio",
                    "nopostoverwrites": False,
                    "preferredcodec": "mp3",
                    "preferredquality": "5",
                }
            ] + self.params["postprocessors"]
            if quality:
                self.params["format_sort"] = [f"abr:{quality}"]

        for attempt in range(self.DOWNLOAD_ATTEMPTS):
            for url in pending_urls:
                try:
                    self.download(url)
                except yt_dlp.utils.DownloadError as e:
                    print(e)
                    self.internet_connection()
                    logs.errors.add(e)
                    url = ""
                else:
                    processed_url_count += 1
                    logs.pending_urls.discard(url)
                if url_progress_func:
                    url_progress_func(processed_url_count, total_url_count, url)

            if logs.pending_urls and attempt != self.DOWNLOAD_ATTEMPTS:
                pending_urls = logs.pending_urls
            else:
                break

        return logs


    def extract_urls(self, urls, url_progress_func=None):
        self.params = {
            "extract_flat": "in_playlist",
            "quiet": True,
            "noplaylist": True,
        }
        pending_urls = set(urls)
        extracted_urls = set()
        processed_url_count = 0
        total_url_count = len(urls)
        logs = self.Logs(pending_urls=pending_urls)

        for attempt in range(self.DOWNLOAD_ATTEMPTS):
            for url in pending_urls:
                try:
                    url_data = self.extract_info(url, download=False)
                except yt_dlp.utils.DownloadError as e:
                    print(e)
                    self.internet_connection()
                    logs.errors.add(e)
                    url = ""
                else:
                    if url_data_entries := get_value_if_exists("entries", url_data):
                        for entry in url_data_entries:
                            if entry_url := get_value_if_exists("url", entry):
                                extracted_urls.add(entry_url)
                    else:
                        extracted_urls.add(url)
                    processed_url_count += 1
                    logs.pending_urls.discard(url)
                if url_progress_func:
                    url_progress_func(processed_url_count, total_url_count, url)

            if logs.pending_urls and attempt != self.DOWNLOAD_ATTEMPTS:
                pending_urls = logs.pending_urls
            else:
                break
        
        return logs, extracted_urls
            

    def fetch_media_metadata(self, urls, url_progress_func=None):
        self.params = {
            "quiet": True,
            "noplaylist": True,
            "writesubtitles": True,
            "allsubtitles": True,
            "extract_flat": "in_playlist",
        }
        pending_urls = set(urls)
        processed_url_count = 0
        total_url_count = len(pending_urls)
        media_metadata = self.MediaMetadata()
        logs = self.Logs(pending_urls=pending_urls)

        for attempt in range(self.DOWNLOAD_ATTEMPTS + 1):
            for url in pending_urls:
                try:
                    url_data = self.extract_info(url, download=False)
                except yt_dlp.utils.DownloadError as e:
                    print(e)
                    logs.errors.add(e)
                    self.internet_connection()
                    url = ""
                else:
                    if url_data_entries := get_value_if_exists("entries", url_data):
                        for entry in url_data_entries:
                            if entry_url := get_value_if_exists("url", entry):
                                logs.pending_urls.add(entry_url)
                                total_url_count += 1
                    else:
                        if url_data_formats := get_value_if_exists("formats", url_data):
                            bitrates = set()
                            resolutions = set()
                            
                            for _format in url_data_formats:
                                if(
                                    (_format_format_note := get_value_if_exists("format_note", _format, str)) and
                                    (resolution_search := re.search(r"([0-9]+)p", _format_format_note))
                                ):
                                    resolutions.add(int(resolution_search.group(1)))
                                if (
                                    (_format_abr := get_value_if_exists("abr", _format, str)) and
                                    (_format_abr := int(_format_abr))
                                ):
                                    bitrates.add(_format_abr)

                            if not media_metadata.bitrates:
                                media_metadata.bitrates = bitrates
                            else:
                                media_metadata.bitrates.intersection_update(bitrates)
                            if not media_metadata.resolutions:
                                media_metadata.resolutions = resolutions
                            else:
                                media_metadata.resolutions.intersection_update(resolutions)

                        if url_data_subtitles := get_value_if_exists("subtitles", url_data):
                            for subtitle_lang, subtitle_details in url_data_subtitles.items():
                                if subtitle_details_name := get_value_if_exists("name", subtitle_details):
                                    media_metadata.subtitles[subtitle_lang] = subtitle_details_name

                    logs.pending_urls.discard(url)
                    processed_url_count += 1
                if url_progress_func:
                    url_progress_func(processed_url_count, total_url_count, url)

            if logs.pending_urls and attempt != self.DOWNLOAD_ATTEMPTS:
                pending_urls = logs.pending_urls
            else:
                break

        return logs, media_metadata


    def download_progress_hook(self, progress_data, progress_func, processed_url_count, total_url_count):
        percentage = None
        if str_percentage := get_value_if_exists("_percent_str", progress_data, str):
            percentage = int(round(float(str_percentage.replace("%", "")), 0))
        
        progress_func(percentage, processed_url_count, total_url_count)


    def internet_connection(self):
        try:
            socket.create_connection(self.DNS).close()
        except socket.error as e:
            print(e)
            raise self.NoInternet(e)


    @dataclass
    class Logs:
        pending_urls: set = set()
        errors: set = set()


    @dataclass
    class MediaMetadata:
        resolutions: set = set()
        bitrates: set = set()
        subtitles: dict = {}


    class NoInternet(BaseException):
        pass


    class ForceExit(BaseException):
        pass


    DOWNLOAD_ATTEMPTS = 2
    DNS = ("1.1.1.1", 53)