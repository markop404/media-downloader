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


from PySide6.QtWidgets import QDialog, QLabel
from PySide6.QtGui import QDesktopServices

from ..ui import Ui_AboutDialog
from ..__init__ import VERSION

class AboutDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
        self.connect_signals_and_slots()
        self.ui.tabWidget.widget(0).findChild(QLabel, "versionLabel").setText(VERSION)


    def connect_signals_and_slots(self):
        self.ui.closeDialogButton.clicked.connect(self.close)
        self.ui.donateButton.clicked.connect(lambda: QDesktopServices.openUrl("https://downloader.markopejic.com/donate"))
        self.ui.websiteButton.clicked.connect(lambda: QDesktopServices.openUrl("https://downloader.markopejic.com/"))
        self.ui.supportedWebsitesButton.clicked.connect(lambda: QDesktopServices.openUrl("https://downloader.markopejic.com/supported-websites"))
        self.ui.whatsNewButton.clicked.connect(lambda: QDesktopServices.openUrl("https://downloader.markopejic.com/whats-new"))
        self.ui.sourceCodeButton.clicked.connect(lambda: QDesktopServices.openUrl("https://downloader.markopejic.com/source-code"))
        self.ui.issueReportButton.clicked.connect(lambda: QDesktopServices.openUrl("https://downloader.markopejic.com/report-an-issue"))
    

    def showEvent(self, event):
        self.ui.tabWidget.setCurrentIndex(0)
        return super().showEvent(event)
