# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_buttonsFIUyUW.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
        self.horizontalLayout = QHBoxLayout(TabButtons)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, 0, 0)
        self.newTabPushButton = QPushButton(TabButtons)
        self.newTabPushButton.setObjectName(u"newTabPushButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ContactNew))
        self.newTabPushButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.newTabPushButton, 0, Qt.AlignmentFlag.AlignTop)

        self.menuPushButton = QPushButton(TabButtons)
        self.menuPushButton.setObjectName(u"menuPushButton")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FormatJustifyFill))
        self.menuPushButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.menuPushButton, 0, Qt.AlignmentFlag.AlignTop)


        self.retranslateUi(TabButtons)

        self.newTabPushButton.setDefault(True)


        QMetaObject.connectSlotsByName(TabButtons)
    # setupUi

    def retranslateUi(self, TabButtons):
#if QT_CONFIG(tooltip)
        self.newTabPushButton.setToolTip(QCoreApplication.translate("TabButtons", u"New Tab (Ctrl+T)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.newTabPushButton.setShortcut(QCoreApplication.translate("TabButtons", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.menuPushButton.setText("")
        pass
    # retranslateUi

