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


from PySide6.QtWidgets import QComboBox


class ComboBox(QComboBox):
    def generate_and_set_items(self, items, prefix="", suffix="", first_item=None, sort_reverse=True):
        data = {}

        if first_item:
            data[first_item] = None
        
        for item in sorted(items, reverse=sort_reverse):
            pretty_item = prefix + str(item) + suffix
            data[pretty_item] = item
        
        self.replace_all_items(data)


    def replace_all_items(self, items={}):
        self.clear()
        for text, data in items.items():
            self.addItem(text, data)
        self.setCurrentIndex(0)