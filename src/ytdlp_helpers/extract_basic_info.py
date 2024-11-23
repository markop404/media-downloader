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

from utils import str_to_int


def extract_basic_info(data_list):
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
                        subtitles[subtitle_details["name"]] = subtitle_lang

    all_bitrates = sorted(all_bitrates, reverse=True)
    all_resolutions = sorted(all_resolutions, reverse=True)
    qualities = {"bitrates": all_bitrates, "resolutions": all_resolutions}
    subtitles = dict(sorted(subtitles.items(), key=lambda item: item[1]))

    return qualities, subtitles