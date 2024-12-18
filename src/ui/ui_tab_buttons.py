# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_buttonsRmuPrp.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_TabButtons(object):
    def setupUi(self, TabButtons):
        if not TabButtons.objectName():
            TabButtons.setObjectName(u"TabButtons")
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        font.setHintingPreference(QFont.PreferFullHinting)
        TabButtons.setFont(font)
        self.horizontalLayout = QHBoxLayout(TabButtons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, 0, 3)
        self.newTabButton = QPushButton(TabButtons)
        self.newTabButton.setObjectName(u"newTabButton")
        self.newTabButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon = QIcon(QIcon.fromTheme(u"list-add"))
        self.newTabButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.newTabButton)

        self.menuButton = QPushButton(TabButtons)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon1 = QIcon(QIcon.fromTheme(u"preferences-other"))
        self.menuButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.menuButton)


        self.retranslateUi(TabButtons)

        QMetaObject.connectSlotsByName(TabButtons)
    # setupUi

    def retranslateUi(self, TabButtons):
#if QT_CONFIG(tooltip)
        self.newTabButton.setToolTip(QCoreApplication.translate("TabButtons", u"New Tab<br>(Ctrl+T)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.newTabButton.setShortcut(QCoreApplication.translate("TabButtons", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.menuButton.setToolTip(QCoreApplication.translate("TabButtons", u"Menu<br>(Alt+M)", None))
#endif // QT_CONFIG(tooltip)
        pass
    # retranslateUi

