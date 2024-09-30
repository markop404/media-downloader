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
from PySide6.QtWidgets import QApplication
from src.main import MainWindow

app = QApplication([])
app.setStyle("Fusion")
app.setApplicationName("Media Downloader")
app.setOrganizationDomain("markopejic.com")
app.setOrganizationName("Marko Pejić")

window = MainWindow()
window.show()

sys.exit(app.exec())
