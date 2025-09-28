#!/usr/bin/env python

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


import sys
import platform

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from src.main import MainWindow

app = QApplication([])

app.setOrganizationName("MarkoPejic")
app.setOrganizationDomain("markopejic.com")
app.setDesktopFileName("com.markopejic.downloader")
app.setApplicationName("MediaDownloader")
app.setApplicationDisplayName("Media Downloader")
app.setWindowIcon(QIcon(":/icons/icon.png"))

match platform.system():
    case "Windows":
        app.setStyle("Fusion")
    case "Darwin":
        app.setStyle("Fusion")

window = MainWindow()
window.show()

if __name__ == "__main__":
    sys.exit(app.exec())
