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


from .extract_data import extract_data
from re import search
from yt_dlp import YoutubeDL

def extract_basic_info(data_list):
    final_qualities = {"audio": [], "video": {}}
    all_audio_qualities = []
    all_video_qualities = []
    raw_mp4_qualities = {}
    all_subtitles = set()
    subtitle_data = {}

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
                        raw_mp4_qualities[resolution] = _format["height"]

                elif _format["vcodec"] == "none" and "abr" in _format:
                    bitrate = _format["abr"]
                    if bitrate and bitrate != "0":
                        bitrate = int(bitrate)
                        audio_qualities.add(bitrate)

            if not all_audio_qualities:
                all_audio_qualities = audio_qualities
            else:
                all_audio_qualities.intersection_update(audio_qualities)
            if not all_video_qualities:
                all_video_qualities = video_qualities
            else:
                all_video_qualities.intersection_update(video_qualities)

        if "subtitles" in data:
            subtitles = data["subtitles"]
            if subtitles:
                subtitle_data.update(subtitles)

    final_qualities["audio"].append("Best")
    for quality in sorted(list(all_audio_qualities), reverse=True):
        final_qualities["audio"].append(f"{quality} kbps")

    final_qualities["video"]["Best"] = "best"
    for quality in sorted(list(all_video_qualities), reverse=True):
        final_qualities["video"][f"{quality}p"] = str(raw_mp4_qualities[quality])

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

    return final_qualities, subtitles
