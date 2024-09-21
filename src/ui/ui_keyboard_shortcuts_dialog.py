# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keyboard_shortcuts_dialogFmpdiR.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_KeyboardShortcutsDialog(object):
    def setupUi(self, KeyboardShortcutsDialog):
        if not KeyboardShortcutsDialog.objectName():
            KeyboardShortcutsDialog.setObjectName(u"KeyboardShortcutsDialog")
        KeyboardShortcutsDialog.resize(450, 715)
        KeyboardShortcutsDialog.setMinimumSize(QSize(450, 715))
        KeyboardShortcutsDialog.setMaximumSize(QSize(650, 860))
        icon = QIcon()
        icon.addFile(u"icons/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        KeyboardShortcutsDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(KeyboardShortcutsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_21 = QLabel(KeyboardShortcutsDialog)
        self.label_21.setObjectName(u"label_21")
        font = QFont()
        font.setBold(True)
        self.label_21.setFont(font)
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.label_21.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.label_21)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_9 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(55, 16777215))
        self.pushButton_9.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_9.setAutoDefault(False)

        self.horizontalLayout_6.addWidget(self.pushButton_9, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_10 = QLabel(KeyboardShortcutsDialog)
        self.label_10.setObjectName(u"label_10")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setWeight(QFont.Light)
        self.label_10.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_10, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_10 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(35, 16777215))
        self.pushButton_10.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_10.setAutoDefault(False)

        self.horizontalLayout_6.addWidget(self.pushButton_10)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.label_11 = QLabel(KeyboardShortcutsDialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_6.addWidget(self.label_11)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_11 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMaximumSize(QSize(55, 16777215))
        self.pushButton_11.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_11.setAutoDefault(False)

        self.horizontalLayout_7.addWidget(self.pushButton_11, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_12 = QLabel(KeyboardShortcutsDialog)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_12, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_12 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMaximumSize(QSize(35, 16777215))
        self.pushButton_12.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_12.setAutoDefault(False)

        self.horizontalLayout_7.addWidget(self.pushButton_12)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.label_13 = QLabel(KeyboardShortcutsDialog)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_7.addWidget(self.label_13)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.label_37 = QLabel(KeyboardShortcutsDialog)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font)
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.label_37.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.label_37)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pushButton_32 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setMaximumSize(QSize(55, 16777215))
        self.pushButton_32.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_32.setAutoDefault(False)

        self.horizontalLayout_17.addWidget(self.pushButton_32, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_35 = QLabel(KeyboardShortcutsDialog)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font1)

        self.horizontalLayout_17.addWidget(self.label_35, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_33 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setMaximumSize(QSize(35, 16777215))
        self.pushButton_33.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_33.setAutoDefault(False)

        self.horizontalLayout_17.addWidget(self.pushButton_33)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_16)

        self.label_36 = QLabel(KeyboardShortcutsDialog)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_17.addWidget(self.label_36)


        self.verticalLayout.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pushButton_34 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setMaximumSize(QSize(55, 16777215))
        self.pushButton_34.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_34.setAutoDefault(False)

        self.horizontalLayout_18.addWidget(self.pushButton_34, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_38 = QLabel(KeyboardShortcutsDialog)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font1)

        self.horizontalLayout_18.addWidget(self.label_38, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_35 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setMaximumSize(QSize(35, 16777215))
        self.pushButton_35.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_35.setAutoDefault(False)

        self.horizontalLayout_18.addWidget(self.pushButton_35)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_17)

        self.label_39 = QLabel(KeyboardShortcutsDialog)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_18.addWidget(self.label_39)


        self.verticalLayout.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_17 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMaximumSize(QSize(55, 16777215))
        self.pushButton_17.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_17.setAutoDefault(False)

        self.horizontalLayout_10.addWidget(self.pushButton_17, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_18 = QLabel(KeyboardShortcutsDialog)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.horizontalLayout_10.addWidget(self.label_18, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_18 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMaximumSize(QSize(35, 16777215))
        self.pushButton_18.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_18.setAutoDefault(False)

        self.horizontalLayout_10.addWidget(self.pushButton_18)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.label_19 = QLabel(KeyboardShortcutsDialog)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_10.addWidget(self.label_19)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushButton_36 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setMaximumSize(QSize(55, 16777215))
        self.pushButton_36.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_36.setAutoDefault(False)

        self.horizontalLayout_19.addWidget(self.pushButton_36, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_40 = QLabel(KeyboardShortcutsDialog)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font1)

        self.horizontalLayout_19.addWidget(self.label_40, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_37 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setMaximumSize(QSize(35, 16777215))
        self.pushButton_37.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_37.setAutoDefault(False)

        self.horizontalLayout_19.addWidget(self.pushButton_37)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_18)

        self.label_41 = QLabel(KeyboardShortcutsDialog)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_19.addWidget(self.label_41)


        self.verticalLayout.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_22 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMaximumSize(QSize(55, 16777215))
        self.pushButton_22.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_22.setAutoDefault(False)

        self.horizontalLayout_12.addWidget(self.pushButton_22, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_25 = QLabel(KeyboardShortcutsDialog)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_25, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_23 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMaximumSize(QSize(35, 16777215))
        self.pushButton_23.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_23.setAutoDefault(False)

        self.horizontalLayout_12.addWidget(self.pushButton_23)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_11)

        self.label_26 = QLabel(KeyboardShortcutsDialog)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_12.addWidget(self.label_26)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_24 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMaximumSize(QSize(55, 16777215))
        self.pushButton_24.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_24.setAutoDefault(False)

        self.horizontalLayout_13.addWidget(self.pushButton_24, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_27 = QLabel(KeyboardShortcutsDialog)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)

        self.horizontalLayout_13.addWidget(self.label_27, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_25 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMaximumSize(QSize(35, 16777215))
        self.pushButton_25.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_25.setAutoDefault(False)

        self.horizontalLayout_13.addWidget(self.pushButton_25)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_12)

        self.label_28 = QLabel(KeyboardShortcutsDialog)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_13.addWidget(self.label_28)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_20 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMaximumSize(QSize(55, 16777215))
        self.pushButton_20.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_20.setAutoDefault(False)

        self.horizontalLayout_11.addWidget(self.pushButton_20, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_23 = QLabel(KeyboardShortcutsDialog)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label_23, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_21 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMaximumSize(QSize(35, 16777215))
        self.pushButton_21.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_21.setAutoDefault(False)

        self.horizontalLayout_11.addWidget(self.pushButton_21)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)

        self.label_24 = QLabel(KeyboardShortcutsDialog)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_11.addWidget(self.label_24)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.label = QLabel(KeyboardShortcutsDialog)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_15 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMaximumSize(QSize(55, 16777215))
        self.pushButton_15.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_15.setAutoDefault(False)

        self.horizontalLayout_9.addWidget(self.pushButton_15, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_16 = QLabel(KeyboardShortcutsDialog)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_16, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_16 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMaximumSize(QSize(35, 16777215))
        self.pushButton_16.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_16.setAutoDefault(False)

        self.horizontalLayout_9.addWidget(self.pushButton_16)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)

        self.label_17 = QLabel(KeyboardShortcutsDialog)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_9.addWidget(self.label_17)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pushButton_30 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setMaximumSize(QSize(55, 16777215))
        self.pushButton_30.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_30.setAutoDefault(False)

        self.horizontalLayout_16.addWidget(self.pushButton_30, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_33 = QLabel(KeyboardShortcutsDialog)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font1)

        self.horizontalLayout_16.addWidget(self.label_33, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_31 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setMaximumSize(QSize(35, 16777215))
        self.pushButton_31.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_31.setAutoDefault(False)

        self.horizontalLayout_16.addWidget(self.pushButton_31)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_15)

        self.label_34 = QLabel(KeyboardShortcutsDialog)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_16.addWidget(self.label_34)


        self.verticalLayout.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton_26 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMaximumSize(QSize(55, 16777215))
        self.pushButton_26.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_26.setAutoDefault(False)

        self.horizontalLayout_14.addWidget(self.pushButton_26, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_29 = QLabel(KeyboardShortcutsDialog)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)

        self.horizontalLayout_14.addWidget(self.label_29, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_27 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_27.setAutoDefault(False)

        self.horizontalLayout_14.addWidget(self.pushButton_27)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_13)

        self.label_30 = QLabel(KeyboardShortcutsDialog)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_14.addWidget(self.label_30)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_28 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMaximumSize(QSize(55, 16777215))
        self.pushButton_28.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_28.setAutoDefault(False)

        self.horizontalLayout_15.addWidget(self.pushButton_28, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_31 = QLabel(KeyboardShortcutsDialog)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_31, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_29 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_29.setAutoDefault(False)

        self.horizontalLayout_15.addWidget(self.pushButton_29)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_14)

        self.label_32 = QLabel(KeyboardShortcutsDialog)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_15.addWidget(self.label_32)


        self.verticalLayout.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_5 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(55, 16777215))
        self.pushButton_5.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_5.setAutoDefault(False)

        self.horizontalLayout_4.addWidget(self.pushButton_5, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_6 = QLabel(KeyboardShortcutsDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_6 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(35, 16777215))
        self.pushButton_6.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_6.setAutoDefault(False)

        self.horizontalLayout_4.addWidget(self.pushButton_6)

        self.label_20 = QLabel(KeyboardShortcutsDialog)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_4.addWidget(self.label_20)

        self.pushButton_19 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMaximumSize(QSize(35, 16777215))
        self.pushButton_19.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_19.setAutoDefault(False)

        self.horizontalLayout_4.addWidget(self.pushButton_19)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.label_7 = QLabel(KeyboardShortcutsDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_4.addWidget(self.label_7)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label_22 = QLabel(KeyboardShortcutsDialog)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.label_22.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.label_22)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(KeyboardShortcutsDialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(55, 16777215))
        self.pushButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_2 = QLabel(KeyboardShortcutsDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_2 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(35, 16777215))
        self.pushButton_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_2.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(KeyboardShortcutsDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_13 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMaximumSize(QSize(55, 16777215))
        self.pushButton_13.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_13.setAutoDefault(False)

        self.horizontalLayout_8.addWidget(self.pushButton_13, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_14 = QLabel(KeyboardShortcutsDialog)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_14, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_14 = QPushButton(KeyboardShortcutsDialog)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMaximumSize(QSize(35, 16777215))
        self.pushButton_14.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_14.setAutoDefault(False)

        self.horizontalLayout_8.addWidget(self.pushButton_14)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.label_15 = QLabel(KeyboardShortcutsDialog)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_8.addWidget(self.label_15)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.retranslateUi(KeyboardShortcutsDialog)

        QMetaObject.connectSlotsByName(KeyboardShortcutsDialog)
    # setupUi

    def retranslateUi(self, KeyboardShortcutsDialog):
        KeyboardShortcutsDialog.setWindowTitle(QCoreApplication.translate("KeyboardShortcutsDialog", u"Keyboard Shortcuts", None))
        self.label_21.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"General", None))
        self.pushButton_9.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Alt", None))
        self.label_10.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.pushButton_10.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"D", None))
        self.label_11.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Download", None))
        self.pushButton_11.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Alt", None))
        self.label_12.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.pushButton_12.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"P", None))
        self.label_13.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Pull Data", None))
        self.label_37.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Controls", None))
        self.pushButton_32.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Alt", None))
        self.label_35.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.pushButton_33.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"F", None))
        self.label_36.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Show Format Options", None))
        self.pushButton_34.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Alt", None))
        self.label_38.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.pushButton_35.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Q", None))
        self.label_39.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Show Quality Options", None))
        self.pushButton_17.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Alt", None))
        self.label_18.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.pushButton_18.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"S", None))
        self.label_19.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Show Subtitle Options", None))
        self.pushButton_36.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Alt", None))
        self.label_40.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.pushButton_37.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"C", None))
        self.label_41.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Change Download Folder", None))
        self.pushButton_22.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Alt", None))
        self.label_25.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.pushButton_23.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"T", None))
        self.label_26.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Toggle Thumbnail Cropping", None))
        self.pushButton_24.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Alt", None))
        self.label_27.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.pushButton_25.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"U", None))
        self.label_28.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Toggle URL Removal", None))
        self.pushButton_20.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Alt", None))
        self.label_23.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.pushButton_21.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"E", None))
        self.label_24.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Toggle Subtitle Embedding", None))
        self.label.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Tabs", None))
        self.pushButton_15.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Ctrl", None))
        self.label_16.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.pushButton_16.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"T", None))
        self.label_17.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"New Tab", None))
        self.pushButton_30.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Ctrl", None))
        self.label_33.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.pushButton_31.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"W", None))
        self.label_34.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Close Tab", None))
        self.pushButton_26.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Ctrl", None))
        self.label_29.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.pushButton_27.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Page Up", None))
        self.label_30.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Switch to Tab on the Left", None))
        self.pushButton_28.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Ctrl", None))
        self.label_31.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.pushButton_29.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Page Down", None))
        self.label_32.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Switch to Tab on the Right", None))
        self.pushButton_5.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Ctrl", None))
        self.label_6.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.pushButton_6.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"0", None))
        self.label_20.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"....", None))
        self.pushButton_19.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"9", None))
        self.label_7.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Switch to Tab Directly", None))
        self.label_22.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Other", None))
        self.pushButton.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Ctrl", None))
        self.label_2.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.pushButton_2.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"N", None))
        self.label_3.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"New Window", None))
        self.pushButton_13.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Ctrl", None))
        self.label_14.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.pushButton_14.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"?", None))
        self.label_15.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"View Shortcuts", None))
    # retranslateUi
