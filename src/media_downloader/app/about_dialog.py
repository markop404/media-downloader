from PySide6.QtWidgets import QDialog, QLabel
from PySide6.QtGui import QDesktopServices

from ..ui import Ui_AboutDialog
from .. import VERSION

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
