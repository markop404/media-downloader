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


import yt_dlp
import os
from .check_internet_connection import check_internet_connection


def download(urls, download_location="", on_progress=None, on_url_progress=None, file_type="video", subtitles=None, quality=None, postprocessor_progress=None, embed_subtitles=True):
    options = {
        "outtmpl": f"{download_location}/%(title)s.%(ext)s",
        "noplaylist": True,
        "postprocessors": [{"key": "FFmpegMetadata"}, {"key": "EmbedThumbnail"}],
        "writethumbnail": True,
    }
    failed_urls = []
    TOTAL_URL_COUNT = len(urls)
    processed_url_count = 0

    if on_progress:
        options["progress_hooks"] = [lambda data: on_progress(data, processed_url_count, TOTAL_URL_COUNT)]
    
    if postprocessor_progress:
        options["postprocessor_hooks"] = [lambda data: postprocessor_progress(data, processed_url_count, TOTAL_URL_COUNT)]

    if quality:
        quality_int = ""
        for char in quality:
            if char.isdigit():
                quality_int += char
    
    if subtitles:
        options["writesubtitles"] = True
        options["subtitleslangs"] = subtitles

    if file_type == "video":
        options["format"] = "bestvideo+bestaudio"
        options["merge_output_format"] = "mp4"
        if quality:
            options["format_sort"] = ["fps", "abr", f"res:{quality_int}"]
        if subtitles and embed_subtitles:
            options["postprocessors"].append({"key": "FFmpegEmbedSubtitle"})
    
    elif file_type == "audio":
        options["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3"
            }
        ] + options["postprocessors"]
        options["format"] = "bestaudio"
        if quality:
            options["format_sort"] = [f"abr:{quality_int}"]

    with yt_dlp.YoutubeDL(options) as ydl:
        for url in urls:
            try:
                ydl.download(url)
                processed_url_count += 1
                if on_url_progress:
                    on_url_progress(url, processed_url_count, TOTAL_URL_COUNT) 
            except yt_dlp.utils.DownloadError as e:
                print(e)
                if not check_internet_connection():
                    return failed_urls, False
                failed_urls.append(url)

    if failed_urls:
        with yt_dlp.YoutubeDL(options) as ydl:
            for url in failed_urls:
                try:
                    ydl.download(failed_urls)
                    failed_urls.remove(url)
                    if on_url_progress:
                        on_url_progress(url, processed_url_count, TOTAL_URL_COUNT)
                    processed_url_count += 1
                except yt_dlp.utils.DownloadError as e:
                    print(e)
                    if not check_internet_connection():
                        return failed_urls, False

    if failed_urls:
        new_options = {}
        if "progress_hooks" in options:
            new_options["progress_hooks"] = options["progress_hooks"]
        if "postprocessor_hooks" in options:
            new_options["postprocessor_hooks"] = options["postprocessor_hooks"]

        with yt_dlp.YoutubeDL(new_options) as ydl:
            for url in failed_urls:
                try:
                    ydl.download(url)
                    failed_urls.remove(url)
                    if on_url_progress:
                        on_url_progress(url, processed_url_count, TOTAL_URL_COUNT)
                    processed_url_count += 1
                except yt_dlp.utils.DownloadError as e:
                    print(e)
                    if not check_internet_connection():
                        return failed_urls, False

    return failed_urls, True
