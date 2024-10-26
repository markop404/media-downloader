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


from re import search

from yt_dlp import YoutubeDL

from .extract_data import extract_data
from src.utils import str_to_int


def extract_basic_info(data_list, preferred_qualities=None):
    final_qualities = {"mp3": [], "mp4": {}}
    all_bitrates = []
    all_resolutions = []
    raw_resolutions = {}
    all_subtitles = set()
    subtitle_data = {}
    preferred_resolution = str_to_int(preferred_qualities["resolution"])
    preferred_bitrate = str_to_int(preferred_qualities["bitrate"])

    for data in data_list:
        if "formats" in data:
            audio_qualities = set()
            video_qualities = set()
            formats = data["formats"]
            
            for _format in formats:
                if _format["vcodec"] != "none" and "format_note" in _format and "height" in _format:
                    if resolution_search := search(r"([0-9]+)p", _format["format_note"]):
                        resolution = int(resolution_search.group(1))
                        video_qualities.add(resolution)
                        raw_resolutions[resolution] = _format["height"]

                elif _format["vcodec"] == "none" and "abr" in _format:
                    bitrate = _format["abr"]
                    if bitrate and bitrate != "0":
                        bitrate = int(bitrate)
                        audio_qualities.add(bitrate)

            if not all_bitrates:
                all_bitrates = audio_qualities
            else:
                all_bitrates.intersection_update(audio_qualities)
            if not all_resolutions:
                all_resolutions = video_qualities
            else:
                all_resolutions.intersection_update(video_qualities)

        if "subtitles" in data:
            subtitles = data["subtitles"]
            if subtitles:
                subtitle_data.update(subtitles)

    if not preferred_bitrate:
        preferred_bitrate = 0
    preferred_qualities["bitrate"] = None
    all_bitrates = sorted(list(all_bitrates), reverse=True)
    iteration = 0
    for bitrate in all_bitrates:
        pretty_bitrate = f"{bitrate} kbps"
        if iteration == 0:
            pretty_bitrate += " (Best)"
        final_qualities["mp3"].append(pretty_bitrate)
        if not preferred_qualities["bitrate"] and bitrate <= preferred_bitrate:
            preferred_qualities["bitrate"] = pretty_bitrate
        iteration += 1

    all_resolutions = sorted(list(all_resolutions), reverse=True)
    if not preferred_resolution:
        preferred_resolution = 0
    preferred_qualities["resolution"] = None
    iteration = 0
    for resolution in all_resolutions:
        pretty_resolution = f"{resolution}p"
        if iteration == 0:
            pretty_resolution += " (Best)"
        final_qualities["mp4"][pretty_resolution] = str(raw_resolutions[resolution])
        if not preferred_qualities["resolution"] and resolution <= preferred_resolution:
            preferred_qualities["resolution"] = pretty_resolution
        iteration += 1

    subtitles = {}
    if subtitle_data and isinstance(subtitle_data, dict):
        for item in subtitle_data.keys():
            if item:
                all_subtitles.add(item)
    
        if all_subtitles:
            for subtitle in all_subtitles:
                if len(subtitle_data[subtitle]) > 0 and "name" in subtitle_data[subtitle][0]:
                    subtitles[subtitle_data[subtitle][0]["name"]] = subtitle

            subtitles = sorted(subtitles.items())

    return final_qualities, subtitles, preferred_qualities