# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowfhCqbn.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(840, 710)
        MainWindow.setMinimumSize(QSize(500, 650))
        icon = QIcon()
        icon.addFile(u"icons/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionNewWindow = QAction(MainWindow)
        self.actionNewWindow.setObjectName(u"actionNewWindow")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WindowNew))
        self.actionNewWindow.setIcon(icon1)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout))
        self.actionAbout.setIcon(icon2)
        self.actionKeyboardShortcuts = QAction(MainWindow)
        self.actionKeyboardShortcuts.setObjectName(u"actionKeyboardShortcuts")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.InputKeyboard))
        self.actionKeyboardShortcuts.setIcon(icon3)
        self.actionKeyboardShortcuts.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Media Downloader", None))
        self.actionNewWindow.setText(QCoreApplication.translate("MainWindow", u"New Window", None))
#if QT_CONFIG(shortcut)
        self.actionNewWindow.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionKeyboardShortcuts.setText(QCoreApplication.translate("MainWindow", u"Keyboard Shortcuts", None))
#if QT_CONFIG(shortcut)
        self.actionKeyboardShortcuts.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+?", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi