# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_buttonsBHgecg.ui'
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
        TabButtons.resize(184, 35)
        self.horizontalLayout = QHBoxLayout(TabButtons)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, 0, 0)
        self.newTabButton = QPushButton(TabButtons)
        self.newTabButton.setObjectName(u"newTabButton")
        self.newTabButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.newTabButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.newTabButton)

        self.menuButton = QPushButton(TabButtons)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout.addWidget(self.menuButton)


        self.retranslateUi(TabButtons)

        QMetaObject.connectSlotsByName(TabButtons)
    # setupUi

    def retranslateUi(self, TabButtons):
#if QT_CONFIG(tooltip)
        self.newTabButton.setToolTip(QCoreApplication.translate("TabButtons", u"Ctrl+T", None))
#endif // QT_CONFIG(tooltip)
        self.newTabButton.setText(QCoreApplication.translate("TabButtons", u"New Tab", None))
#if QT_CONFIG(shortcut)
        self.newTabButton.setShortcut(QCoreApplication.translate("TabButtons", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.menuButton.setText(QCoreApplication.translate("TabButtons", u"Menu", None))
        pass
    # retranslateUi
