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
            "urls": {
                "original": set(),
                "extracted": set()
            },
        }


    def download(
        self,
        urls,
        download_dir="",
        download_progress_hook=None,
        url_progress_hook=None,
        postprocessor_progress_hook=None,
        file_type="mp4",
        subtitle_lang=None,
        quality=None,
        embed_subtitles=True,
        crop_thumbnails=False,
    ):
        ydl_config = self.ydl_config
        ydl_config.update({
            "outtmpl": f"{download_dir}/%(title)s.%(ext)s",
            "windowsfilenames": True,
            "postprocessors": [
                {"key": "FFmpegMetadata"},
                {"key": "EmbedThumbnail", "already_have_thumbnail": False}
            ],
            "writethumbnail": True,
        })
        urls = set(urls)
        failed_urls = set()
        processed_url_count = 0
        total_url_count = len(urls)
        errors = set()

        if self.cache_available(urls):
            urls = self.cache["urls"]["extracted"]

        if download_progress_hook:
            ydl_config["progress_hooks"] = [
                lambda data, progress_hook=download_progress_hook: 
                    self.download_progress_hook(data, progress_hook, processed_url_count, total_url_count)
            ]
        
        if postprocessor_progress_hook:
            ydl_config["postprocessor_hooks"] = [
                lambda data: postprocessor_progress_hook(processed_url_count, total_url_count)
            ]

        if crop_thumbnails:
            ydl_config["postprocessor_args"]["thumbnailsconvertor+ffmpeg_o"] = [
                "-c:v", "png", "-vf", "crop=ih"
            ]
        
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

        for iteration in range(2):
            with yt_dlp.YoutubeDL(ydl_config) as ydl:
                for url in urls:
                    try:
                        ydl.download(url)
                        processed_url_count += 1
                        failed_urls.discard(url)
                        if url_progress_hook:
                            url_progress_hook(processed_url_count, total_url_count, url)
                    except yt_dlp.utils.DownloadError as e:
                        print(e)
                        errors.add(e)
                        failed_urls.add(url)
                        if not self.internet_connection():
                            return failed_urls, errors, False
                        if url_progress_hook:
                            url_progress_hook(processed_url_count, total_url_count)

            if failed_urls and iteration == 1:
                new_ydl_config = {}
                if "progress_hooks" in ydl_config:
                    new_ydl_config["progress_hooks"] = ydl_config["progress_hooks"]
                if "postprocessor_hooks" in ydl_config:
                    new_ydl_config["postprocessor_hooks"] = ydl_config["postprocessor_hooks"]
                ydl_config = new_ydl_config
                urls = failed_urls
            else:
                break

        return failed_urls, errors, True


    def extract_urls(self, urls, url_progress_hook=None, force=False):
        urls = set(urls)
        if self.cache_available(urls) and not force:
            return self.cache["urls"]["extracted"], set(), set(), True
        else:
            failed_urls = set()
            extracted_urls = set()
            processed_url_count = 0
            total_url_count = len(urls)
            data = {}
            errors = set()
            ydl_config = self.ydl_config
            ydl_config.update({"extract_flat": "in_playlist"})

            for _ in range(2):
                with yt_dlp.YoutubeDL(ydl_config) as ydl:
                    for url in urls:
                        try:
                            new_data = ydl.extract_info(url, download=False)
                            if "entries" in new_data:
                                for entry in new_data["entries"]:
                                    extracted_urls.add(entry["url"])
                            else:
                                data[url] = new_data
                                extracted_urls.add(url)
                            processed_url_count += 1
                            failed_urls.discard(url)
                        except yt_dlp.utils.DownloadError as e:
                            print(e)
                            errors.add(e)
                            failed_urls.add(url)
                            if not self.internet_connection():
                                return extracted_urls, failed_urls, errors, False

                        if url_progress_hook:
                            url_progress_hook(processed_url_count, total_url_count)

                if failed_urls:
                    urls = failed_urls
                else:
                    break
            
            self.cache["urls"]["original"] = urls
            self.cache["urls"]["extracted"] = extracted_urls
            return extracted_urls, failed_urls, errors, True
            

    def fetch_pretty_data(self, urls, url_progress_hook=None):
        urls = set(urls)
        self.cache["urls"]["original"] = urls
        failed_urls = set()
        extracted_urls = set()
        data = []
        i = 0
        errors = set()
        total_url_count = len(urls)
        ydl_config = self.ydl_config
        ydl_config.update({
            "writesubtitles": True,
            "allsubtitles": True,
            "extract_flat": "in_playlist",
        })
        
        with yt_dlp.YoutubeDL(ydl_config) as ydl:
            while i < len(remaining_urls):
                try:
                    url = remaining_urls[i]
                    new_data = ydl.extract_info(url, download=False)
                    if "entries" in new_data:
                        for entry in new_data["entries"]:
                            urls.add(entry["url"])
                        urls.remove(url)
                    else:
                        data.append(new_data)
                    i += 1
                    failed_urls.discard(url)
                except yt_dlp.utils.DownloadError as e:
                    print(e)
                    errors.add(e)
                    failed_urls.add(url)
                    if not self.internet_connection():
                        return {}, {}, failed_urls, errors, False
            
                if url_progress_hook:
                    url_progress_hook(i, len(remaining_urls))
        
        self.cache["urls"]["extracted"] = extracted_urls
                
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


    def download_progress_hook(self, data, progress_hook, processed_url_count, total_url_count):
        percentage = None
        if data["status"] == "downloading":            
            if "downloaded_bytes" in data and "total_bytes" in data:
                if data["downloaded_bytes"] and data["total_bytes"]:
                    try:
                        percentage = int((data["downloaded_bytes"] / data["total_bytes"]) * 100)
                    except:
                        pass
            elif "fragment_index" in data and "fragment_count" in data:
                if data["fragment_index"] and data["fragment_count"]:
                    try:
                        percentage = int((data["fragment_index"] / data["fragment_count"]) * 100)
                    except:
                        pass
        progress_hook(percentage, processed_url_count, total_url_count)


    def internet_connection(self):
        try:
            socket.create_connection(("1.1.1.1", 53)).close()
            return True
        except BaseException as e:
            print(e)
            return False
    

    def cache_available(self, urls):
        if set(urls) == self.cache["urls"]["original"]:
            return True
        else:
            return False