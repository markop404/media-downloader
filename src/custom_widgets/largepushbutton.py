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


from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize


class LargePushButton(QPushButton):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        current_size = self.sizeHint()
        new_width = current_size.width() + 70
        new_height = current_size.height() + 8
        self.setMinimumSize(QSize(new_width, new_height))