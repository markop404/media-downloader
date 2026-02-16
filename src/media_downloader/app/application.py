import platform

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from .main_window import MainWindow

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

        MainWindow().show()