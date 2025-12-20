# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowNlSrGz.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
        MainWindow.resize(600, 600)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout))
        self.actionAbout.setIcon(icon)
        self.actionKeyboardShortcuts = QAction(MainWindow)
        self.actionKeyboardShortcuts.setObjectName(u"actionKeyboardShortcuts")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.InputKeyboard))
        self.actionKeyboardShortcuts.setIcon(icon1)
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
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About Media Downloader", None))
        self.actionKeyboardShortcuts.setText(QCoreApplication.translate("MainWindow", u"Keyboard Shortcuts", None))
#if QT_CONFIG(shortcut)
        self.actionKeyboardShortcuts.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+?", None))
#endif // QT_CONFIG(shortcut)
        pass
    # retranslateUi

