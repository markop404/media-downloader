# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keyboard_shortcuts_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_KeyboardShortcutsDialog(object):
    def setupUi(self, KeyboardShortcutsDialog):
        if not KeyboardShortcutsDialog.objectName():
            KeyboardShortcutsDialog.setObjectName(u"KeyboardShortcutsDialog")
        self.verticalLayout = QVBoxLayout(KeyboardShortcutsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.verticalSpacer = QSpacerItem(0, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.sectionLabel3 = QLabel(KeyboardShortcutsDialog)
        self.sectionLabel3.setObjectName(u"sectionLabel3")
        font = QFont()
        font.setBold(True)
        self.sectionLabel3.setFont(font)

        self.verticalLayout.addWidget(self.sectionLabel3)

        self.shortcutLayout13 = QHBoxLayout()
        self.shortcutLayout13.setObjectName(u"shortcutLayout13")
        self.keyButton11 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton11.setObjectName(u"keyButton11")
        self.keyButton11.setMaximumSize(QSize(55, 16777215))
        self.keyButton11.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton11.setAutoDefault(False)

        self.shortcutLayout13.addWidget(self.keyButton11)

        self.keySeparator6 = QLabel(KeyboardShortcutsDialog)
        self.keySeparator6.setObjectName(u"keySeparator6")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setWeight(QFont.Light)
        self.keySeparator6.setFont(font1)

        self.shortcutLayout13.addWidget(self.keySeparator6)

        self.keyButton10 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton10.setObjectName(u"keyButton10")
        self.keyButton10.setMaximumSize(QSize(35, 16777215))
        self.keyButton10.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton10.setAutoDefault(False)

        self.shortcutLayout13.addWidget(self.keyButton10)

        self.horizontalSpacer5 = QSpacerItem(80, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.shortcutLayout13.addItem(self.horizontalSpacer5)

        self.shortcutDescriptionLabel5 = QLabel(KeyboardShortcutsDialog)
        self.shortcutDescriptionLabel5.setObjectName(u"shortcutDescriptionLabel5")
        self.shortcutDescriptionLabel5.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.shortcutLayout13.addWidget(self.shortcutDescriptionLabel5)


        self.verticalLayout.addLayout(self.shortcutLayout13)

        self.shortcutLayout14 = QHBoxLayout()
        self.shortcutLayout14.setObjectName(u"shortcutLayout14")
        self.keyButton12 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton12.setObjectName(u"keyButton12")
        self.keyButton12.setMaximumSize(QSize(55, 16777215))
        self.keyButton12.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton12.setAutoDefault(False)

        self.shortcutLayout14.addWidget(self.keyButton12)

        self.keySeparator7 = QLabel(KeyboardShortcutsDialog)
        self.keySeparator7.setObjectName(u"keySeparator7")
        self.keySeparator7.setFont(font1)

        self.shortcutLayout14.addWidget(self.keySeparator7)

        self.keyButton13 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton13.setObjectName(u"keyButton13")
        self.keyButton13.setMaximumSize(QSize(35, 16777215))
        self.keyButton13.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton13.setAutoDefault(False)

        self.shortcutLayout14.addWidget(self.keyButton13)

        self.horizontalSpacer6 = QSpacerItem(80, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.shortcutLayout14.addItem(self.horizontalSpacer6)

        self.shortcutDescriptionLabel6 = QLabel(KeyboardShortcutsDialog)
        self.shortcutDescriptionLabel6.setObjectName(u"shortcutDescriptionLabel6")
        self.shortcutDescriptionLabel6.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.shortcutLayout14.addWidget(self.shortcutDescriptionLabel6)


        self.verticalLayout.addLayout(self.shortcutLayout14)

        self.verticalSpacer_2 = QSpacerItem(0, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.sectionLabel2 = QLabel(KeyboardShortcutsDialog)
        self.sectionLabel2.setObjectName(u"sectionLabel2")
        self.sectionLabel2.setFont(font)

        self.verticalLayout.addWidget(self.sectionLabel2)

        self.shortcutLayout9 = QHBoxLayout()
        self.shortcutLayout9.setObjectName(u"shortcutLayout9")
        self.keyButton32 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton32.setObjectName(u"keyButton32")
        self.keyButton32.setMaximumSize(QSize(55, 16777215))
        self.keyButton32.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton32.setAutoDefault(False)

        self.shortcutLayout9.addWidget(self.keyButton32)

        self.keySeparator17 = QLabel(KeyboardShortcutsDialog)
        self.keySeparator17.setObjectName(u"keySeparator17")
        self.keySeparator17.setFont(font1)

        self.shortcutLayout9.addWidget(self.keySeparator17)

        self.keyButton33 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton33.setObjectName(u"keyButton33")
        self.keyButton33.setMaximumSize(QSize(35, 16777215))
        self.keyButton33.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton33.setAutoDefault(False)

        self.shortcutLayout9.addWidget(self.keyButton33)

        self.horizontalSpacer16 = QSpacerItem(80, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.shortcutLayout9.addItem(self.horizontalSpacer16)

        self.shortcutDescriptionLabel16 = QLabel(KeyboardShortcutsDialog)
        self.shortcutDescriptionLabel16.setObjectName(u"shortcutDescriptionLabel16")
        self.shortcutDescriptionLabel16.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.shortcutLayout9.addWidget(self.shortcutDescriptionLabel16)


        self.verticalLayout.addLayout(self.shortcutLayout9)

        self.shortcutLayout10 = QHBoxLayout()
        self.shortcutLayout10.setObjectName(u"shortcutLayout10")
        self.keyButton3 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton3.setObjectName(u"keyButton3")
        self.keyButton3.setMaximumSize(QSize(55, 16777215))
        self.keyButton3.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton3.setAutoDefault(False)

        self.shortcutLayout10.addWidget(self.keyButton3)

        self.keySeparator2 = QLabel(KeyboardShortcutsDialog)
        self.keySeparator2.setObjectName(u"keySeparator2")
        self.keySeparator2.setFont(font1)

        self.shortcutLayout10.addWidget(self.keySeparator2)

        self.keyButton4 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton4.setObjectName(u"keyButton4")
        self.keyButton4.setMaximumSize(QSize(35, 16777215))
        self.keyButton4.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton4.setAutoDefault(False)

        self.shortcutLayout10.addWidget(self.keyButton4)

        self.horizontalSpacer2 = QSpacerItem(80, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.shortcutLayout10.addItem(self.horizontalSpacer2)

        self.shortcutDescriptionLabel2 = QLabel(KeyboardShortcutsDialog)
        self.shortcutDescriptionLabel2.setObjectName(u"shortcutDescriptionLabel2")
        self.shortcutDescriptionLabel2.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.shortcutLayout10.addWidget(self.shortcutDescriptionLabel2)


        self.verticalLayout.addLayout(self.shortcutLayout10)

        self.shortcutLayout2 = QHBoxLayout()
        self.shortcutLayout2.setObjectName(u"shortcutLayout2")
        self.keyButton18 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton18.setObjectName(u"keyButton18")
        self.keyButton18.setMaximumSize(QSize(55, 16777215))
        self.keyButton18.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton18.setAutoDefault(False)

        self.shortcutLayout2.addWidget(self.keyButton18)

        self.keySeparator10 = QLabel(KeyboardShortcutsDialog)
        self.keySeparator10.setObjectName(u"keySeparator10")
        self.keySeparator10.setFont(font1)

        self.shortcutLayout2.addWidget(self.keySeparator10)

        self.keyButton19 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton19.setObjectName(u"keyButton19")
        self.keyButton19.setMaximumSize(QSize(35, 16777215))
        self.keyButton19.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton19.setAutoDefault(False)

        self.shortcutLayout2.addWidget(self.keyButton19)

        self.horizontalSpacer9 = QSpacerItem(80, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.shortcutLayout2.addItem(self.horizontalSpacer9)

        self.shortcutDescriptionLabel9 = QLabel(KeyboardShortcutsDialog)
        self.shortcutDescriptionLabel9.setObjectName(u"shortcutDescriptionLabel9")
        self.shortcutDescriptionLabel9.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.shortcutLayout2.addWidget(self.shortcutDescriptionLabel9)


        self.verticalLayout.addLayout(self.shortcutLayout2)

        self.shortcutLayout11 = QHBoxLayout()
        self.shortcutLayout11.setObjectName(u"shortcutLayout11")
        self.keyButton5 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton5.setObjectName(u"keyButton5")
        self.keyButton5.setMaximumSize(QSize(55, 16777215))
        self.keyButton5.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton5.setAutoDefault(False)

        self.shortcutLayout11.addWidget(self.keyButton5)

        self.keySeparator3 = QLabel(KeyboardShortcutsDialog)
        self.keySeparator3.setObjectName(u"keySeparator3")
        self.keySeparator3.setFont(font1)

        self.shortcutLayout11.addWidget(self.keySeparator3)

        self.keyButton6 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton6.setObjectName(u"keyButton6")
        self.keyButton6.setMaximumSize(QSize(35, 16777215))
        self.keyButton6.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton6.setAutoDefault(False)

        self.shortcutLayout11.addWidget(self.keyButton6)

        self.horizontalSpacer3 = QSpacerItem(80, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.shortcutLayout11.addItem(self.horizontalSpacer3)

        self.shortcutDescriptionLabel3 = QLabel(KeyboardShortcutsDialog)
        self.shortcutDescriptionLabel3.setObjectName(u"shortcutDescriptionLabel3")
        self.shortcutDescriptionLabel3.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.shortcutLayout11.addWidget(self.shortcutDescriptionLabel3)


        self.verticalLayout.addLayout(self.shortcutLayout11)

        self.shortcutLayout4 = QHBoxLayout()
        self.shortcutLayout4.setObjectName(u"shortcutLayout4")
        self.keyButton22 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton22.setObjectName(u"keyButton22")
        self.keyButton22.setMaximumSize(QSize(55, 16777215))
        self.keyButton22.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton22.setAutoDefault(False)

        self.shortcutLayout4.addWidget(self.keyButton22)

        self.keySeparator12 = QLabel(KeyboardShortcutsDialog)
        self.keySeparator12.setObjectName(u"keySeparator12")
        self.keySeparator12.setFont(font1)

        self.shortcutLayout4.addWidget(self.keySeparator12)

        self.keyButton23 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton23.setObjectName(u"keyButton23")
        self.keyButton23.setMaximumSize(QSize(35, 16777215))
        self.keyButton23.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton23.setAutoDefault(False)

        self.shortcutLayout4.addWidget(self.keyButton23)

        self.horizontalSpacer11 = QSpacerItem(80, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.shortcutLayout4.addItem(self.horizontalSpacer11)

        self.shortcutDescriptionLabel11 = QLabel(KeyboardShortcutsDialog)
        self.shortcutDescriptionLabel11.setObjectName(u"shortcutDescriptionLabel11")
        self.shortcutDescriptionLabel11.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.shortcutLayout4.addWidget(self.shortcutDescriptionLabel11)


        self.verticalLayout.addLayout(self.shortcutLayout4)

        self.shortcutLayout3 = QHBoxLayout()
        self.shortcutLayout3.setObjectName(u"shortcutLayout3")
        self.keyButton20 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton20.setObjectName(u"keyButton20")
        self.keyButton20.setMaximumSize(QSize(55, 16777215))
        self.keyButton20.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton20.setAutoDefault(False)

        self.shortcutLayout3.addWidget(self.keyButton20)

        self.keySeparator11 = QLabel(KeyboardShortcutsDialog)
        self.keySeparator11.setObjectName(u"keySeparator11")
        self.keySeparator11.setFont(font1)

        self.shortcutLayout3.addWidget(self.keySeparator11)

        self.keyButton21 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton21.setObjectName(u"keyButton21")
        self.keyButton21.setMaximumSize(QSize(35, 16777215))
        self.keyButton21.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton21.setAutoDefault(False)

        self.shortcutLayout3.addWidget(self.keyButton21)

        self.horizontalSpacer10 = QSpacerItem(80, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.shortcutLayout3.addItem(self.horizontalSpacer10)

        self.shortcutDescriptionLabel10 = QLabel(KeyboardShortcutsDialog)
        self.shortcutDescriptionLabel10.setObjectName(u"shortcutDescriptionLabel10")
        self.shortcutDescriptionLabel10.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.shortcutLayout3.addWidget(self.shortcutDescriptionLabel10)


        self.verticalLayout.addLayout(self.shortcutLayout3)

        self.verticalSpacer_3 = QSpacerItem(0, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.sectionLabel1 = QLabel(KeyboardShortcutsDialog)
        self.sectionLabel1.setObjectName(u"sectionLabel1")
        self.sectionLabel1.setFont(font)

        self.verticalLayout.addWidget(self.sectionLabel1)

        self.shortcutLayout16 = QHBoxLayout()
        self.shortcutLayout16.setObjectName(u"shortcutLayout16")
        self.keyButton16 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton16.setObjectName(u"keyButton16")
        self.keyButton16.setMaximumSize(QSize(55, 16777215))
        self.keyButton16.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton16.setAutoDefault(False)

        self.shortcutLayout16.addWidget(self.keyButton16)

        self.keySeparator9 = QLabel(KeyboardShortcutsDialog)
        self.keySeparator9.setObjectName(u"keySeparator9")
        self.keySeparator9.setFont(font1)

        self.shortcutLayout16.addWidget(self.keySeparator9)

        self.keyButton17 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton17.setObjectName(u"keyButton17")
        self.keyButton17.setMaximumSize(QSize(35, 16777215))
        self.keyButton17.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton17.setAutoDefault(False)

        self.shortcutLayout16.addWidget(self.keyButton17)

        self.horizontalSpacer8 = QSpacerItem(80, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.shortcutLayout16.addItem(self.horizontalSpacer8)

        self.shortcutDescriptionLabel8 = QLabel(KeyboardShortcutsDialog)
        self.shortcutDescriptionLabel8.setObjectName(u"shortcutDescriptionLabel8")
        self.shortcutDescriptionLabel8.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.shortcutLayout16.addWidget(self.shortcutDescriptionLabel8)


        self.verticalLayout.addLayout(self.shortcutLayout16)

        self.shortcutLayout8 = QHBoxLayout()
        self.shortcutLayout8.setObjectName(u"shortcutLayout8")
        self.keyButton30 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton30.setObjectName(u"keyButton30")
        self.keyButton30.setMaximumSize(QSize(55, 16777215))
        self.keyButton30.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton30.setAutoDefault(False)

        self.shortcutLayout8.addWidget(self.keyButton30)

        self.keySeparator16 = QLabel(KeyboardShortcutsDialog)
        self.keySeparator16.setObjectName(u"keySeparator16")
        self.keySeparator16.setFont(font1)

        self.shortcutLayout8.addWidget(self.keySeparator16)

        self.keyButton31 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton31.setObjectName(u"keyButton31")
        self.keyButton31.setMaximumSize(QSize(35, 16777215))
        self.keyButton31.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton31.setAutoDefault(False)

        self.shortcutLayout8.addWidget(self.keyButton31)

        self.horizontalSpacer15 = QSpacerItem(80, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.shortcutLayout8.addItem(self.horizontalSpacer15)

        self.shortcutDescriptionLabel15 = QLabel(KeyboardShortcutsDialog)
        self.shortcutDescriptionLabel15.setObjectName(u"shortcutDescriptionLabel15")
        self.shortcutDescriptionLabel15.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.shortcutLayout8.addWidget(self.shortcutDescriptionLabel15)


        self.verticalLayout.addLayout(self.shortcutLayout8)

        self.shortcutLayout6 = QHBoxLayout()
        self.shortcutLayout6.setObjectName(u"shortcutLayout6")
        self.keyButton26 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton26.setObjectName(u"keyButton26")
        self.keyButton26.setMaximumSize(QSize(55, 16777215))
        self.keyButton26.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton26.setAutoDefault(False)

        self.shortcutLayout6.addWidget(self.keyButton26)

        self.keySeparator14 = QLabel(KeyboardShortcutsDialog)
        self.keySeparator14.setObjectName(u"keySeparator14")
        self.keySeparator14.setFont(font1)

        self.shortcutLayout6.addWidget(self.keySeparator14)

        self.keyButton27 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton27.setObjectName(u"keyButton27")
        self.keyButton27.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton27.setAutoDefault(False)

        self.shortcutLayout6.addWidget(self.keyButton27)

        self.horizontalSpacer13 = QSpacerItem(80, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.shortcutLayout6.addItem(self.horizontalSpacer13)

        self.shortcutDescriptionLabel13 = QLabel(KeyboardShortcutsDialog)
        self.shortcutDescriptionLabel13.setObjectName(u"shortcutDescriptionLabel13")
        self.shortcutDescriptionLabel13.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.shortcutLayout6.addWidget(self.shortcutDescriptionLabel13)


        self.verticalLayout.addLayout(self.shortcutLayout6)

        self.shortcutLayout7 = QHBoxLayout()
        self.shortcutLayout7.setObjectName(u"shortcutLayout7")
        self.keyButton28 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton28.setObjectName(u"keyButton28")
        self.keyButton28.setMaximumSize(QSize(55, 16777215))
        self.keyButton28.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton28.setAutoDefault(False)

        self.shortcutLayout7.addWidget(self.keyButton28)

        self.keySeparator15 = QLabel(KeyboardShortcutsDialog)
        self.keySeparator15.setObjectName(u"keySeparator15")
        self.keySeparator15.setFont(font1)

        self.shortcutLayout7.addWidget(self.keySeparator15)

        self.keyButton29 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton29.setObjectName(u"keyButton29")
        self.keyButton29.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton29.setAutoDefault(False)

        self.shortcutLayout7.addWidget(self.keyButton29)

        self.horizontalSpacer14 = QSpacerItem(80, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.shortcutLayout7.addItem(self.horizontalSpacer14)

        self.shortcutDescriptionLabel14 = QLabel(KeyboardShortcutsDialog)
        self.shortcutDescriptionLabel14.setObjectName(u"shortcutDescriptionLabel14")
        self.shortcutDescriptionLabel14.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.shortcutLayout7.addWidget(self.shortcutDescriptionLabel14)


        self.verticalLayout.addLayout(self.shortcutLayout7)

        self.shortcutLayout12 = QHBoxLayout()
        self.shortcutLayout12.setObjectName(u"shortcutLayout12")
        self.keyButton8 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton8.setObjectName(u"keyButton8")
        self.keyButton8.setMaximumSize(QSize(55, 16777215))
        self.keyButton8.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton8.setAutoDefault(False)

        self.shortcutLayout12.addWidget(self.keyButton8)

        self.keySeparator5 = QLabel(KeyboardShortcutsDialog)
        self.keySeparator5.setObjectName(u"keySeparator5")
        self.keySeparator5.setFont(font1)

        self.shortcutLayout12.addWidget(self.keySeparator5)

        self.keyButton9 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton9.setObjectName(u"keyButton9")
        self.keyButton9.setMaximumSize(QSize(35, 16777215))
        self.keyButton9.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton9.setAutoDefault(False)

        self.shortcutLayout12.addWidget(self.keyButton9)

        self.keySeparator4 = QLabel(KeyboardShortcutsDialog)
        self.keySeparator4.setObjectName(u"keySeparator4")

        self.shortcutLayout12.addWidget(self.keySeparator4)

        self.keyButton7 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton7.setObjectName(u"keyButton7")
        self.keyButton7.setMaximumSize(QSize(35, 16777215))
        self.keyButton7.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton7.setAutoDefault(False)

        self.shortcutLayout12.addWidget(self.keyButton7)

        self.horizontalSpacer4 = QSpacerItem(80, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.shortcutLayout12.addItem(self.horizontalSpacer4)

        self.shortcutDescriptionLabel4 = QLabel(KeyboardShortcutsDialog)
        self.shortcutDescriptionLabel4.setObjectName(u"shortcutDescriptionLabel4")
        self.shortcutDescriptionLabel4.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.shortcutLayout12.addWidget(self.shortcutDescriptionLabel4)


        self.verticalLayout.addLayout(self.shortcutLayout12)

        self.verticalSpacer_4 = QSpacerItem(0, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.sectionLabel4 = QLabel(KeyboardShortcutsDialog)
        self.sectionLabel4.setObjectName(u"sectionLabel4")
        self.sectionLabel4.setFont(font)

        self.verticalLayout.addWidget(self.sectionLabel4)

        self.shortcutLayout15 = QHBoxLayout()
        self.shortcutLayout15.setObjectName(u"shortcutLayout15")
        self.keyButton14 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton14.setObjectName(u"keyButton14")
        self.keyButton14.setMaximumSize(QSize(55, 16777215))
        self.keyButton14.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton14.setAutoDefault(False)

        self.shortcutLayout15.addWidget(self.keyButton14)

        self.keySeparator8 = QLabel(KeyboardShortcutsDialog)
        self.keySeparator8.setObjectName(u"keySeparator8")
        self.keySeparator8.setFont(font1)

        self.shortcutLayout15.addWidget(self.keySeparator8)

        self.keyButton15 = QPushButton(KeyboardShortcutsDialog)
        self.keyButton15.setObjectName(u"keyButton15")
        self.keyButton15.setMaximumSize(QSize(35, 16777215))
        self.keyButton15.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.keyButton15.setAutoDefault(False)

        self.shortcutLayout15.addWidget(self.keyButton15)

        self.horizontalSpacer7 = QSpacerItem(80, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.shortcutLayout15.addItem(self.horizontalSpacer7)

        self.shortcutDescriptionLabel7 = QLabel(KeyboardShortcutsDialog)
        self.shortcutDescriptionLabel7.setObjectName(u"shortcutDescriptionLabel7")
        self.shortcutDescriptionLabel7.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.shortcutLayout15.addWidget(self.shortcutDescriptionLabel7)


        self.verticalLayout.addLayout(self.shortcutLayout15)

        self.verticalSpacer_5 = QSpacerItem(0, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.closeDialogButton = QPushButton(KeyboardShortcutsDialog)
        self.closeDialogButton.setObjectName(u"closeDialogButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WindowClose))
        self.closeDialogButton.setIcon(icon)
        self.closeDialogButton.setAutoDefault(False)

        self.verticalLayout.addWidget(self.closeDialogButton, 0, Qt.AlignmentFlag.AlignRight)


        self.retranslateUi(KeyboardShortcutsDialog)

        self.closeDialogButton.setDefault(True)


        QMetaObject.connectSlotsByName(KeyboardShortcutsDialog)
    # setupUi

    def retranslateUi(self, KeyboardShortcutsDialog):
        KeyboardShortcutsDialog.setWindowTitle(QCoreApplication.translate("KeyboardShortcutsDialog", u"Keyboard Shortcuts", None))
        self.sectionLabel3.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"General", None))
        self.keyButton11.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Alt", None))
        self.keySeparator6.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.keyButton10.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"D", None))
        self.shortcutDescriptionLabel5.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Download", None))
        self.keyButton12.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Alt", None))
        self.keySeparator7.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.keyButton13.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"L", None))
        self.shortcutDescriptionLabel6.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Load options", None))
        self.sectionLabel2.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Controls", None))
        self.keyButton32.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Alt", None))
        self.keySeparator17.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.keyButton33.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"F", None))
        self.shortcutDescriptionLabel16.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Show format options", None))
        self.keyButton3.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Alt", None))
        self.keySeparator2.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.keyButton4.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Q", None))
        self.shortcutDescriptionLabel2.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Show quality options", None))
        self.keyButton18.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Alt", None))
        self.keySeparator10.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.keyButton19.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"S", None))
        self.shortcutDescriptionLabel9.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Show subtitle options", None))
        self.keyButton5.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Alt", None))
        self.keySeparator3.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.keyButton6.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"C", None))
        self.shortcutDescriptionLabel3.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Change download folder", None))
        self.keyButton22.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Alt", None))
        self.keySeparator12.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.keyButton23.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"T", None))
        self.shortcutDescriptionLabel11.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Toggle thumbnail cropping", None))
        self.keyButton20.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Alt", None))
        self.keySeparator11.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.keyButton21.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"E", None))
        self.shortcutDescriptionLabel10.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Toggle subtitle embedding", None))
        self.sectionLabel1.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Tabs", None))
        self.keyButton16.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Ctrl", None))
        self.keySeparator9.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.keyButton17.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"T", None))
        self.shortcutDescriptionLabel8.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"New tab", None))
        self.keyButton30.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Ctrl", None))
        self.keySeparator16.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.keyButton31.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"W", None))
        self.shortcutDescriptionLabel15.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Close tab", None))
        self.keyButton26.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Ctrl", None))
        self.keySeparator14.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.keyButton27.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Page Up", None))
        self.shortcutDescriptionLabel13.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Switch to tab on the left", None))
        self.keyButton28.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Ctrl", None))
        self.keySeparator15.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.keyButton29.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Page Down", None))
        self.shortcutDescriptionLabel14.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Switch to tab on the right", None))
        self.keyButton8.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Alt", None))
        self.keySeparator5.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.keyButton9.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"0", None))
        self.keySeparator4.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"...", None))
        self.keyButton7.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"9", None))
        self.shortcutDescriptionLabel4.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Switch to tab directly", None))
        self.sectionLabel4.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Other", None))
        self.keyButton14.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Ctrl", None))
        self.keySeparator8.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"+", None))
        self.keyButton15.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"?", None))
        self.shortcutDescriptionLabel7.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"View shortcuts", None))
        self.closeDialogButton.setText(QCoreApplication.translate("KeyboardShortcutsDialog", u"Close", None))
    # retranslateUi

