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
from .check_internet_connection import check_internet_connection

def extract_urls(urls, on_progress=None):
    processed_url_count = 0
    total_url_count = len(urls)
    extracted_urls = set()
    failed_urls = set()
    errors = set()
    options = {
        "extract_flat": True,
        "noplaylist": True,
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        for url in urls:
            try:
                extracted_urls = extracted_urls.union(_extract_urls(url, ydl))
                processed_url_count += 1
                if on_progress:
                    on_progress(processed_url_count, total_url_count)
            except yt_dlp.utils.DownloadError as e:
                print(e)
                errors.add(e)
                if not check_internet_connection():
                    return extracted_urls, failed_urls, False, errors
                failed_urls.add(url)

    if failed_urls:
        with yt_dlp.YoutubeDL(options) as ydl:
            for url in failed_urls:
                try:
                    extracted_urls = extracted_urls.union(_extract_urls(url, ydl))
                    processed_url_count += 1
                    if on_progress:
                        on_progress(processed_url_count, total_url_count)
                    failed_urls.discard(url)
                except yt_dlp.utils.DownloadError as e:
                    print(e)
                    errors.add(e)
                    if not check_internet_connection():
                        return extracted_urls, failed_urls, False, errors

    return extracted_urls, failed_urls, True, errors


def _extract_urls(url, ydl):
    urls = set()

    info = ydl.extract_info(url, download=False)
    if "entries" in info:
        for entry in info["entries"]:
            urls.add(entry["url"])
    else:
        urls.add(url)
    
    return urls
