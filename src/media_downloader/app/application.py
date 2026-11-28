import platform
import sys
import os

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import QStandardPaths
from PySide6.QtNetwork import QLocalServer, QLocalSocket
from PySide6.QtDBus import QDBusConnection, QDBusInterface

from .main_window import MainWindow
from ..yt_dlp_update_service import YtDlpUpdateService

class Application(QApplication):
    APP_ID = "com.markopejic.downloader"

    def __init__(self):
        super().__init__([])

        socket = QLocalSocket()
        socket.connectToServer(self.APP_ID)
        if socket.waitForConnected(500):
            socket.disconnectFromServer()
            sys.exit(0)

        self.server = QLocalServer()
        self.server.newConnection.connect(self.handle_new_connection)
        self.server.listen(self.APP_ID)

        self.setOrganizationName("MarkoPejic")
        self.setOrganizationDomain("markopejic.com")
        self.setDesktopFileName(self.APP_ID)
        self.setApplicationName("MediaDownloader")
        self.setApplicationDisplayName("Media Downloader")
        self.setWindowIcon(QIcon(":icon.png"))

        self.updater = YtDlpUpdateService(
            QStandardPaths.writableLocation(
                QStandardPaths.AppLocalDataLocation
            )
        )
        self.updater.start_update()

        match platform.system():
            case "Windows":
                self.setStyle("Fusion")
            case "Darwin":
                self.setStyle("Fusion")
            case "Linux":
                if os.environ.get("XDG_CURRENT_DESKTOP", "") == "GNOME":
                    if self.get_preferred_color_scheme():
                        QIcon.setThemeName("breeze-dark")
                        self.setStyle("Adwaita-dark")
                    else:
                        QIcon.setThemeName("breeze")
                        self.setStyle("Adwaita")

        self.main_window = MainWindow()
        self.main_window.show()
    

    def handle_new_connection(self):
        self.server.nextPendingConnection()

        self.main_window.showNormal()
        self.main_window.raise_()
        self.main_window.activateWindow()


    def get_preferred_color_scheme(self):
        try:
            bus = QDBusConnection.sessionBus()
            interface = QDBusInterface(
                "org.freedesktop.portal.Desktop",
                "/org/freedesktop/portal/desktop",
                "org.freedesktop.portal.Settings",
                bus,
            )
            reply = interface.call("ReadOne", "org.freedesktop.appearance", "color-scheme")
            value = int(reply.arguments()[0].variant())
            if value > 1:
                return 0
            else:
                return value
        except Exception as e:
            print(e)
            return 0