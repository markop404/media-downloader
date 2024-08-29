# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_windowIlTcBo.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        if not aboutDialog.objectName():
            aboutDialog.setObjectName(u"aboutDialog")
        aboutDialog.resize(350, 335)
        aboutDialog.setMinimumSize(QSize(350, 335))
        aboutDialog.setMaximumSize(QSize(350, 335))
        icon = QIcon()
        icon.addFile("icons/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        aboutDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(aboutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalSpacer1 = QSpacerItem(40, 80, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer1)

        self.titleLabel = QLabel(aboutDialog)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setFamilies([u"Cantarell Extra Bold"])
        font.setPointSize(20)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.titleLabel)

        self.versionLabel = QLabel(aboutDialog)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.versionLabel.setOpenExternalLinks(True)
        self.versionLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.versionLabel)

        self.horizontalSpacer2 = QSpacerItem(40, 30, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer2)

        self.descriptionLabel = QLabel(aboutDialog)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.descriptionLabel)

        self.horizontalSpacer3 = QSpacerItem(40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer3)

        self.licenseLabel = QLabel(aboutDialog)
        self.licenseLabel.setObjectName(u"licenseLabel")
        self.licenseLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.licenseLabel.setWordWrap(True)
        self.licenseLabel.setOpenExternalLinks(True)
        self.licenseLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.licenseLabel)

        self.horizontalSpacer4 = QSpacerItem(40, 22, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer4)

        self.copyrightLabel = QLabel(aboutDialog)
        self.copyrightLabel.setObjectName(u"copyrightLabel")
        self.copyrightLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.copyrightLabel)


        self.retranslateUi(aboutDialog)

        QMetaObject.connectSlotsByName(aboutDialog)
    # setupUi

    def retranslateUi(self, aboutDialog):
        aboutDialog.setWindowTitle(QCoreApplication.translate("aboutDialog", u"About Media Downloader", None))
        self.titleLabel.setText(QCoreApplication.translate("aboutDialog", u"Media Downloader", None))
        self.versionLabel.setText(QCoreApplication.translate("aboutDialog", u"v3.3.1 &nbsp;|&nbsp; <a href=\"https://downloader.markopejic.com/\" style=\"text-decoration: none;\">Website</a>", None))
        self.descriptionLabel.setText(QCoreApplication.translate("aboutDialog", u"A simple and lightweight program for downloading media from <a href=\"https://downloader.markopejic.com/supported-websites\">hundreds of websites</a>.", None))
        self.licenseLabel.setText(QCoreApplication.translate("aboutDialog", u"This program comes with absolutely no warranty. See the <a href=\"https://www.gnu.org/licenses/gpl-3.0.html\">GNU General Public License, version 3 or later</a> for details.", None))
        self.copyrightLabel.setText(QCoreApplication.translate("aboutDialog", u"Copyright \u00a9 2024 Marko Peji\u0107", None))
    # retranslateUi
