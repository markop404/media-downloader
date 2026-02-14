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
        self.parent = parent
        self.on_select = on_select
        self.update_paths()


    def open(self):
        self.update_paths(
            QFileDialog.getExistingDirectory(
                self.parent,
                caption="Choose a Folder",
                dir=self.path,
                options=QFileDialog.ShowDirsOnly
            )
        )


    def update_paths(self, path=QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)):
        if path:
            path = Path(path)
            self.path = str(path.resolve())
            
            if path.name:
                name = path.name
            else:
                name = self.path
            
            anchor = f"<a href=\"{path.as_uri()}\">{name}</a>"

            if self.on_select:
                self.on_select(self.path, anchor)