# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)
from . import icons_rc

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        self.verticalLayout = QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName(u"headerLayout")
        self.appIconLabel = QLabel(AboutDialog)
        self.appIconLabel.setObjectName(u"appIconLabel")
        self.appIconLabel.setMaximumSize(QSize(65, 65))
        self.appIconLabel.setPixmap(QPixmap(u":icon.png"))
        self.appIconLabel.setScaledContents(True)

        self.headerLayout.addWidget(self.appIconLabel)

        self.appNameLabel = QLabel(AboutDialog)
        self.appNameLabel.setObjectName(u"appNameLabel")
        font = QFont()
        font.setPointSize(18)
        font.setWeight(QFont.ExtraBold)
        self.appNameLabel.setFont(font)
        self.appNameLabel.setMargin(4)

        self.headerLayout.addWidget(self.appNameLabel)


        self.verticalLayout.addLayout(self.headerLayout)

        self.horizontalSpacer1 = QSpacerItem(40, 2, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer1)

        self.tabWidget = QTabWidget(AboutDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.aboutTab = QWidget()
        self.aboutTab.setObjectName(u"aboutTab")
        self.verticalLayout_3 = QVBoxLayout(self.aboutTab)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.descriptionLabel = QLabel(self.aboutTab)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        font1 = QFont()
        font1.setBold(True)
        self.descriptionLabel.setFont(font1)
        self.descriptionLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.descriptionLabel)

        self.versionLabel = QLabel(self.aboutTab)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.versionLabel)

        self.verticalSpacer = QSpacerItem(0, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.creditsLabel = QLabel(self.aboutTab)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setOpenExternalLinks(True)
        self.creditsLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.creditsLabel)

        self.verticalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.aboutTab, "")
        self.linksTab = QWidget()
        self.linksTab.setObjectName(u"linksTab")
        self.gridLayout = QGridLayout(self.linksTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.donateButton = QPushButton(self.linksTab)
        self.donateButton.setObjectName(u"donateButton")
        self.donateButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.donateButton, 1, 0, 1, 1)

        self.supportedWebsitesButton = QPushButton(self.linksTab)
        self.supportedWebsitesButton.setObjectName(u"supportedWebsitesButton")
        self.supportedWebsitesButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.supportedWebsitesButton, 3, 0, 1, 1)

        self.websiteButton = QPushButton(self.linksTab)
        self.websiteButton.setObjectName(u"websiteButton")
        self.websiteButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.websiteButton, 1, 1, 1, 1)

        self.whatsNewButton = QPushButton(self.linksTab)
        self.whatsNewButton.setObjectName(u"whatsNewButton")
        self.whatsNewButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.whatsNewButton, 2, 0, 1, 1)

        self.issueReportButton = QPushButton(self.linksTab)
        self.issueReportButton.setObjectName(u"issueReportButton")
        self.issueReportButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.issueReportButton, 2, 1, 1, 1)

        self.sourceCodeButton = QPushButton(self.linksTab)
        self.sourceCodeButton.setObjectName(u"sourceCodeButton")
        self.sourceCodeButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.sourceCodeButton, 3, 1, 1, 1)

        self.tabWidget.addTab(self.linksTab, "")
        self.legalTab = QWidget()
        self.legalTab.setObjectName(u"legalTab")
        self.horizontalLayout_3 = QHBoxLayout(self.legalTab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.disclaimerLabel = QLabel(self.legalTab)
        self.disclaimerLabel.setObjectName(u"disclaimerLabel")
        self.disclaimerLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.disclaimerLabel.setWordWrap(True)
        self.disclaimerLabel.setOpenExternalLinks(True)
        self.disclaimerLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_3.addWidget(self.disclaimerLabel)

        self.tabWidget.addTab(self.legalTab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.closeDialogButton = QPushButton(AboutDialog)
        self.closeDialogButton.setObjectName(u"closeDialogButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WindowClose))
        self.closeDialogButton.setIcon(icon)

        self.verticalLayout.addWidget(self.closeDialogButton, 0, Qt.AlignmentFlag.AlignRight)


        self.retranslateUi(AboutDialog)

        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"About", None))
        self.appNameLabel.setText(QCoreApplication.translate("AboutDialog", u"Media Downloader", None))
        self.descriptionLabel.setText(QCoreApplication.translate("AboutDialog", u"Web video/audio downloader", None))
        self.versionLabel.setText(QCoreApplication.translate("AboutDialog", u"Unspecified version", None))
        self.creditsLabel.setText(QCoreApplication.translate("AboutDialog", u"Made by <a href=\"https://markopejic.com\">Marko Peji\u0107</a>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aboutTab), QCoreApplication.translate("AboutDialog", u"About", None))
        self.donateButton.setText(QCoreApplication.translate("AboutDialog", u"Donate", None))
        self.supportedWebsitesButton.setText(QCoreApplication.translate("AboutDialog", u"Supported Websites", None))
        self.websiteButton.setText(QCoreApplication.translate("AboutDialog", u"Website", None))
        self.whatsNewButton.setText(QCoreApplication.translate("AboutDialog", u"What's New", None))
        self.issueReportButton.setText(QCoreApplication.translate("AboutDialog", u"Report an Issue", None))
        self.sourceCodeButton.setText(QCoreApplication.translate("AboutDialog", u"Source Code", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.linksTab), QCoreApplication.translate("AboutDialog", u"Links", None))
        self.disclaimerLabel.setText(QCoreApplication.translate("AboutDialog", u"<p>Copyright \u00a9 2024-2026 Marko Peji\u0107</p><p>Videos on YouTube and other sites may be subject to DMCA protection. The authors of Media Downloader do not endorse, and are not responsible for, the use of this application in means that will violate these laws. </p><p>This application comes with absolutely no warranty. See the <a href=\"https://www.gnu.org/licenses/gpl-3.0.html\">GNU General Public License, version 3</a> or later for details.</p>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.legalTab), QCoreApplication.translate("AboutDialog", u"Legal", None))
        self.closeDialogButton.setText(QCoreApplication.translate("AboutDialog", u"Close", None))
    # retranslateUi

