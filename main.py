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
import os
import platform

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon, QStyleHints
from PySide6.QtCore import QProcessEnvironment, Qt

from src.main import MainWindow


app = QApplication([])

app.setApplicationName("MediaDownloader")
app.setOrganizationName("MarkoPejic")
app.setDesktopFileName("com.markopejic.downloader")
app.setApplicationDisplayName("Media Downloader")

match platform.system():
    case "Windows":
        app.setStyle("Fusion")
    case "Linux":
        env = QProcessEnvironment.systemEnvironment()
        if not "kde" in env.value("XDG_CURRENT_DESKTOP").casefold():
            app.setStyle("Breeze")
            QIcon.setThemeName("breeze")

window = MainWindow()
window.show()

sys.exit(app.exec())
