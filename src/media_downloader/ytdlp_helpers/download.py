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

import yt_dlp

from .check_internet_connection import check_internet_connection


def download(
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
    youtubedl_options = {
        "outtmpl": f"{download_location}/%(title)s.%(ext)s",
        "noplaylist": True,
        "postprocessors": [
            {"key": "FFmpegMetadata"},
            {"key": "EmbedThumbnail", "already_have_thumbnail": False}
        ],
        "writethumbnail": True,
        "postprocessor_args": {},
        "quiet": True,
    }
    errors = set()
    failed_urls = set()
    TOTAL_URL_COUNT = len(urls)
    processed_url_count = 0

    if on_progress:
        youtubedl_options["progress_hooks"] = [lambda data: on_progress(data, processed_url_count, TOTAL_URL_COUNT)]
    
    if postprocessor_progress:
        youtubedl_options["postprocessor_hooks"] = [lambda data: postprocessor_progress(data, processed_url_count, TOTAL_URL_COUNT)]

    if crop_thumbnails:
        youtubedl_options["postprocessor_args"]["thumbnailsconvertor+ffmpeg_o"] = ["-c:v", "png", "-vf", "crop=ih"]
    
    if subtitle_lang:
        youtubedl_options["writesubtitles"] = True
        youtubedl_options["subtitleslangs"] = subtitle_lang
        if embed_subtitles:
            youtubedl_options["postprocessors"].append({"key": "FFmpegEmbedSubtitle"})

    if file_type == "mp4":
        youtubedl_options["format"] = "bestvideo+bestaudio"
        youtubedl_options["merge_output_format"] = "mp4"
        if quality:
            youtubedl_options["format_sort"] = ["fps", "abr", f"res:{quality}"]
    
    elif file_type == "mp3":
        youtubedl_options["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3"
            }
        ] + youtubedl_options["postprocessors"]
        youtubedl_options["format"] = "bestaudio"
        if quality:
            youtubedl_options["format_sort"] = [f"abr:{quality}"]


    with yt_dlp.YoutubeDL(youtubedl_options) as ydl:
        for url in urls:
            try:
                ydl.download(url)
                processed_url_count += 1 
            except yt_dlp.utils.DownloadError as e:
                print(e)
                errors.add(e)
                if not check_internet_connection():
                    return failed_urls, False
                failed_urls.add(url)
            
            if on_url_progress:
                on_url_progress(url, processed_url_count, TOTAL_URL_COUNT)

    if failed_urls:
        new_youtubedl_options = {}
        if "progress_hooks" in youtubedl_options:
            new_youtubedl_options["progress_hooks"] = youtubedl_options["progress_hooks"]
        if "postprocessor_hooks" in youtubedl_options:
            new_youtubedl_options["postprocessor_hooks"] = youtubedl_options["postprocessor_hooks"]

        with yt_dlp.YoutubeDL(new_youtubedl_options) as ydl:
            for url in failed_urls:
                try:
                    ydl.download(url)
                    failed_urls.remove(url)
                    processed_url_count += 1
                except yt_dlp.utils.DownloadError as e:
                    print(e)
                    errors.add(e)
                    if not check_internet_connection():
                        return failed_urls, False

                if on_url_progress:
                    on_url_progress(url, processed_url_count, TOTAL_URL_COUNT)

    return failed_urls, True, errors
