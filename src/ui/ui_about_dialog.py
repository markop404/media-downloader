# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_dialogEMfFnt.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        self.verticalLayout = QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName(u"headerLayout")
        self.appIconLabel = QLabel(AboutDialog)
        self.appIconLabel.setObjectName(u"appIconLabel")
        self.appIconLabel.setMaximumSize(QSize(65, 65))
        self.appIconLabel.setPixmap(QPixmap(u"icons/icon.png"))
        self.appIconLabel.setScaledContents(True)

        self.headerLayout.addWidget(self.appIconLabel)

        self.appNameLabel = QLabel(AboutDialog)
        self.appNameLabel.setObjectName(u"appNameLabel")
        font = QFont()
        font.setPointSize(16)
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
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.aboutLabel = QLabel(self.aboutTab)
        self.aboutLabel.setObjectName(u"aboutLabel")
        self.aboutLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.aboutLabel.setWordWrap(True)
        self.aboutLabel.setOpenExternalLinks(True)
        self.aboutLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.aboutLabel)

        self.tabWidget.addTab(self.aboutTab, "")
        self.linksTab = QWidget()
        self.linksTab.setObjectName(u"linksTab")
        self.horizontalLayout = QHBoxLayout(self.linksTab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftColumnButtonLayout = QVBoxLayout()
        self.leftColumnButtonLayout.setObjectName(u"leftColumnButtonLayout")
        self.donateButton = QPushButton(self.linksTab)
        self.donateButton.setObjectName(u"donateButton")
        self.donateButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.leftColumnButtonLayout.addWidget(self.donateButton)

        self.supportedWebsitesButton = QPushButton(self.linksTab)
        self.supportedWebsitesButton.setObjectName(u"supportedWebsitesButton")
        self.supportedWebsitesButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.leftColumnButtonLayout.addWidget(self.supportedWebsitesButton)

        self.websiteButton = QPushButton(self.linksTab)
        self.websiteButton.setObjectName(u"websiteButton")
        self.websiteButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.leftColumnButtonLayout.addWidget(self.websiteButton)


        self.horizontalLayout.addLayout(self.leftColumnButtonLayout)

        self.rightColumnButtonLayout = QVBoxLayout()
        self.rightColumnButtonLayout.setObjectName(u"rightColumnButtonLayout")
        self.whatsNewButton = QPushButton(self.linksTab)
        self.whatsNewButton.setObjectName(u"whatsNewButton")
        self.whatsNewButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.rightColumnButtonLayout.addWidget(self.whatsNewButton)

        self.issueReportButton = QPushButton(self.linksTab)
        self.issueReportButton.setObjectName(u"issueReportButton")
        self.issueReportButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.rightColumnButtonLayout.addWidget(self.issueReportButton)

        self.sourceCodeButton = QPushButton(self.linksTab)
        self.sourceCodeButton.setObjectName(u"sourceCodeButton")
        self.sourceCodeButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.rightColumnButtonLayout.addWidget(self.sourceCodeButton)


        self.horizontalLayout.addLayout(self.rightColumnButtonLayout)

        self.tabWidget.addTab(self.linksTab, "")
        self.legalTab = QWidget()
        self.legalTab.setObjectName(u"legalTab")
        self.verticalLayout_4 = QVBoxLayout(self.legalTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.copyrightLabel = QLabel(self.legalTab)
        self.copyrightLabel.setObjectName(u"copyrightLabel")
        self.copyrightLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.copyrightLabel.setWordWrap(True)
        self.copyrightLabel.setIndent(1)
        self.copyrightLabel.setOpenExternalLinks(True)

        self.verticalLayout_4.addWidget(self.copyrightLabel)

        self.tabWidget.addTab(self.legalTab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(AboutDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(AboutDialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"About", None))
        self.appIconLabel.setText("")
        self.appNameLabel.setText(QCoreApplication.translate("AboutDialog", u"Media Downloader", None))
        self.aboutLabel.setText(QCoreApplication.translate("AboutDialog", u"<span style=\" font-weight:700;\">Web video / audio downloader</span><br>v5.0.0<br><br>This app is the result of countless hours of development by <a href=\"https://markopejic.com\">Marko Peji\u0107</a>. If it's useful to you, please consider supporting its development with a <a href=\"https://downloader.markopejic.com/donate\">donation</a>. Thank you!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aboutTab), QCoreApplication.translate("AboutDialog", u"About", None))
        self.donateButton.setText(QCoreApplication.translate("AboutDialog", u"Donate", None))
        self.supportedWebsitesButton.setText(QCoreApplication.translate("AboutDialog", u"Supported Websites", None))
        self.websiteButton.setText(QCoreApplication.translate("AboutDialog", u"Website", None))
        self.whatsNewButton.setText(QCoreApplication.translate("AboutDialog", u"What's New", None))
        self.issueReportButton.setText(QCoreApplication.translate("AboutDialog", u"Report an Issue", None))
        self.sourceCodeButton.setText(QCoreApplication.translate("AboutDialog", u"Source Code", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.linksTab), QCoreApplication.translate("AboutDialog", u"Details", None))
        self.copyrightLabel.setText(QCoreApplication.translate("AboutDialog", u"Copyright \u00a9 2024 Marko Peji\u0107<br><br>This application comes with absolutely no warranty. See the <a href=\"https://www.gnu.org/licenses/gpl-3.0.html\">GNU General Public License, version 3</a> or later for details.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.legalTab), QCoreApplication.translate("AboutDialog", u"Legal", None))
    # retranslateUi

