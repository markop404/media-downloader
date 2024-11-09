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


from PySide6.QtWidgets import QDialog
from ui import Ui_KeyboardShortcutsDialog

class KeyboardShortcutsDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_KeyboardShortcutsDialog()
        self.ui.setupUi(self)
        self.connect_signals_and_slots()
        self.setFixedSize(self.sizeHint())
    

    def connect_signals_and_slots(self):
        self.ui.buttonBox.buttons()[0].clicked.connect(self.close)