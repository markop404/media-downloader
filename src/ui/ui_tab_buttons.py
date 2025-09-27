# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_buttonsKMrmro.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QPushButton,
    QSizePolicy, QWidget)

class Ui_TabButtons(object):
    def setupUi(self, TabButtons):
        if not TabButtons.objectName():
            TabButtons.setObjectName(u"TabButtons")
        self.horizontalLayout = QHBoxLayout(TabButtons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout.setContentsMargins(-1, 0, 0, 0)
        self.newTabButton = QPushButton(TabButtons)
        self.newTabButton.setObjectName(u"newTabButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newTabButton.sizePolicy().hasHeightForWidth())
        self.newTabButton.setSizePolicy(sizePolicy)
        self.newTabButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.newTabButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.newTabButton)

        self.menuButton = QPushButton(TabButtons)
        self.menuButton.setObjectName(u"menuButton")
        sizePolicy.setHeightForWidth(self.menuButton.sizePolicy().hasHeightForWidth())
        self.menuButton.setSizePolicy(sizePolicy)
        self.menuButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogQuestion))
        self.menuButton.setIcon(icon1)
        self.menuButton.setFlat(True)

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
        self.menuButton.setToolTip(QCoreApplication.translate("TabButtons", u"Help", None))
#endif // QT_CONFIG(tooltip)
        pass
    # retranslateUi

