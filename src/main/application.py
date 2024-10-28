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


from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from .main_window import MainWindow


class Application(QApplication):
    def __init__(self):
        super().__init__()

        self.setStyle("Fusion")
        self.setApplicationName("MediaDownloader")
        self.setOrganizationName("MarkoPejic")
        self.setDesktopFileName("com.markopejic.downloader")
        self.setApplicationDisplayName("Media Downloader")
        
        icon = QIcon()
        icon.addFile("icons/icon.png")
        self.setWindowIcon(icon)

        self.window = MainWindow()
        self.window.show()