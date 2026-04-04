import platform

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import QStandardPaths

from .main_window import MainWindow
from ..yt_dlp_updater import YtDlpUpdater

class Application(QApplication):
    def __init__(self):
        super().__init__([])

        self.setOrganizationName("MarkoPejic")
        self.setOrganizationDomain("markopejic.com")
        self.setDesktopFileName("com.markopejic.downloader")
        self.setApplicationName("MediaDownloader")
        self.setApplicationDisplayName("Media Downloader")
        self.setWindowIcon(QIcon(":icon.png"))

        match platform.system():
            case "Windows":
                self.setStyle("Fusion")
            case "Darwin":
                self.setStyle("Fusion")

        self.updater = YtDlpUpdater(
            QStandardPaths.writableLocation(
                QStandardPaths.AppLocalDataLocation
            )
        )
        self.updater.start_update()

        MainWindow().show()