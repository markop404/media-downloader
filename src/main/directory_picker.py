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


from pathlib import Path

from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QStandardPaths


class DirectoryPicker:
    def __init__(self, parent, on_select=None):
        self.update_paths()
        self.parent = parent
        self.on_select = on_select


    def open(self):
        self.update_paths(
            QFileDialog.getExistingDirectory(self.parent, "Select a Download Folder", self.path)
        )


    def update_paths(self, path=QStandardPaths.DownloadLocation):
        if path:
            path = Path(path)
            str_path = str(path.resolve())
            if path.name:
                name = path.name
            else:
                name = str_path
            
            self.path = str_path
            self.anchor = f"<a href=\"{path.as_uri()}\">{name}</a>"

            if self.on_select:
                self.on_select()