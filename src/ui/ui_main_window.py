# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowbjpKxq.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
        MainWindow.resize(700, 675)
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        font.setHintingPreference(QFont.PreferFullHinting)
        MainWindow.setFont(font)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon = QIcon(QIcon.fromTheme(u"help-about"))
        self.actionAbout.setIcon(icon)
        self.actionKeyboardShortcuts = QAction(MainWindow)
        self.actionKeyboardShortcuts.setObjectName(u"actionKeyboardShortcuts")
        icon1 = QIcon(QIcon.fromTheme(u"input-keyboard"))
        self.actionKeyboardShortcuts.setIcon(icon1)
        self.actionKeyboardShortcuts.setMenuRole(QAction.MenuRole.NoRole)
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        icon2 = QIcon(QIcon.fromTheme(u"document-properties"))
        self.actionPreferences.setIcon(icon2)
        self.actionPreferences.setMenuRole(QAction.MenuRole.NoRole)
        self.actionRetryAll = QAction(MainWindow)
        self.actionRetryAll.setObjectName(u"actionRetryAll")
        icon3 = QIcon(QIcon.fromTheme(u"view-refresh"))
        self.actionRetryAll.setIcon(icon3)
        self.actionRetryAll.setMenuRole(QAction.MenuRole.NoRole)
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
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About Media Downloader", None))
        self.actionKeyboardShortcuts.setText(QCoreApplication.translate("MainWindow", u"Keyboard Shortcuts", None))
#if QT_CONFIG(shortcut)
        self.actionKeyboardShortcuts.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+?", None))
#endif // QT_CONFIG(shortcut)
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
#if QT_CONFIG(shortcut)
        self.actionPreferences.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+,", None))
#endif // QT_CONFIG(shortcut)
        self.actionRetryAll.setText(QCoreApplication.translate("MainWindow", u"Retry All", None))
#if QT_CONFIG(tooltip)
        self.actionRetryAll.setToolTip(QCoreApplication.translate("MainWindow", u"Retry All", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionRetryAll.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

