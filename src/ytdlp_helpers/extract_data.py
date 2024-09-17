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

def extract_data(urls, on_progress=None, options={}):
    data = []
    failed_urls = []
    if "noplaylist" not in options:
        options["noplaylist"] = True
    if "writesubtitles" not in options:
        options["writesubtitles"] = True
    if "allsubtitles" not in options:
        options["allsubtitles"] = True

    TOTAL_URL_COUNT = len(urls)
    processed_url_count = 0
    errors = set()

    with yt_dlp.YoutubeDL(options) as ydl:
        for url in urls:
            try:
                data += _extract_data(ydl, url)
                processed_url_count += 1
                if on_progress:
                    on_progress(processed_url_count, TOTAL_URL_COUNT)
            except yt_dlp.utils.DownloadError as e:
                print(e)
                errors.add(e)
                if not check_internet_connection():
                    return data, failed_urls, False
                failed_urls.append(url)

    if failed_urls:
        with yt_dlp.YoutubeDL(options) as ydl:
            for url in failed_urls:
                try:
                    data += _extract_data(ydl, url)
                    processed_url_count += 1
                    if on_progress:
                        on_progress(processed_url_count, TOTAL_URL_COUNT)
                    failed_urls.discard(url)
                except yt_dlp.utils.DownloadError as e:
                    print(e)
                    errors.add(e)
                    if not check_internet_connection():
                        return data, failed_urls, False

    return data, failed_urls, True, errors


def _extract_data(ydl, url):
    data = []

    temp_data = ydl.extract_info(url, download=False)
    
    if "entries" in temp_data:
        data += temp_data["entries"]
    else:
        data.append(temp_data)

    return data
