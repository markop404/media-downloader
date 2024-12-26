# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabLJZzsn.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QHBoxLayout, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from ..custom_widgets.combobox import ComboBox
from media_downloader.custom_widgets.largepushbutton import LargePushButton
from media_downloader.custom_widgets.plaintextedit import PlainTextEdit

class Ui_Tab(object):
    def setupUi(self, Tab):
        if not Tab.objectName():
            Tab.setObjectName(u"Tab")
        self.verticalLayout = QVBoxLayout(Tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plainTextEdit = PlainTextEdit(Tab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.donationLinkLabel = QLabel(Tab)
        self.donationLinkLabel.setObjectName(u"donationLinkLabel")
        self.donationLinkLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)
        self.donationLinkLabel.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.donationLinkLabel)

        self.verticalSpacer = QSpacerItem(0, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.downloadOptionsLayout = QFormLayout()
        self.downloadOptionsLayout.setObjectName(u"downloadOptionsLayout")
        self.downloadOptionsLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.FieldsStayAtSizeHint)
        self.downloadOptionsLayout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapLongRows)
        self.downloadOptionsLayout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.downloadOptionsLayout.setFormAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.formatLabel = QLabel(Tab)
        self.formatLabel.setObjectName(u"formatLabel")

        self.downloadOptionsLayout.setWidget(0, QFormLayout.LabelRole, self.formatLabel)

        self.formatComboBox = ComboBox(Tab)
        self.formatComboBox.setObjectName(u"formatComboBox")
        self.formatComboBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.downloadOptionsLayout.setWidget(0, QFormLayout.FieldRole, self.formatComboBox)

        self.qualityLabel = QLabel(Tab)
        self.qualityLabel.setObjectName(u"qualityLabel")

        self.downloadOptionsLayout.setWidget(1, QFormLayout.LabelRole, self.qualityLabel)

        self.qualityComboBox = ComboBox(Tab)
        self.qualityComboBox.setObjectName(u"qualityComboBox")
        self.qualityComboBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.qualityComboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.downloadOptionsLayout.setWidget(1, QFormLayout.FieldRole, self.qualityComboBox)

        self.subtitlesLabel = QLabel(Tab)
        self.subtitlesLabel.setObjectName(u"subtitlesLabel")

        self.downloadOptionsLayout.setWidget(2, QFormLayout.LabelRole, self.subtitlesLabel)

        self.subtitlesComboBox = ComboBox(Tab)
        self.subtitlesComboBox.setObjectName(u"subtitlesComboBox")
        self.subtitlesComboBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.subtitlesComboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.downloadOptionsLayout.setWidget(2, QFormLayout.FieldRole, self.subtitlesComboBox)

        self.downloadFolderLabel = QLabel(Tab)
        self.downloadFolderLabel.setObjectName(u"downloadFolderLabel")

        self.downloadOptionsLayout.setWidget(3, QFormLayout.LabelRole, self.downloadFolderLabel)

        self.downloadFolderLayout = QHBoxLayout()
        self.downloadFolderLayout.setObjectName(u"downloadFolderLayout")
        self.downloadFolderIndicatorLabel = QLabel(Tab)
        self.downloadFolderIndicatorLabel.setObjectName(u"downloadFolderIndicatorLabel")
        self.downloadFolderIndicatorLabel.setOpenExternalLinks(True)

        self.downloadFolderLayout.addWidget(self.downloadFolderIndicatorLabel)

        self.setDownloadFolderButton = QPushButton(Tab)
        self.setDownloadFolderButton.setObjectName(u"setDownloadFolderButton")
        self.setDownloadFolderButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon = QIcon(QIcon.fromTheme(u"folder-open"))
        self.setDownloadFolderButton.setIcon(icon)

        self.downloadFolderLayout.addWidget(self.setDownloadFolderButton)


        self.downloadOptionsLayout.setLayout(3, QFormLayout.FieldRole, self.downloadFolderLayout)


        self.verticalLayout.addLayout(self.downloadOptionsLayout)

        self.horizontalSpacer2 = QSpacerItem(0, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.horizontalSpacer2)

        self.cropThumbnailsCheckBoxLayout = QHBoxLayout()
        self.cropThumbnailsCheckBoxLayout.setObjectName(u"cropThumbnailsCheckBoxLayout")
        self.horizontalSpacer3 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.cropThumbnailsCheckBoxLayout.addItem(self.horizontalSpacer3)

        self.cropThumbnailsCheckBox = QCheckBox(Tab)
        self.cropThumbnailsCheckBox.setObjectName(u"cropThumbnailsCheckBox")
        self.cropThumbnailsCheckBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.cropThumbnailsCheckBoxLayout.addWidget(self.cropThumbnailsCheckBox)

        self.horizontalSpacer4 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.cropThumbnailsCheckBoxLayout.addItem(self.horizontalSpacer4)


        self.verticalLayout.addLayout(self.cropThumbnailsCheckBoxLayout)

        self.embedSubtitlesCheckBoxLayout = QHBoxLayout()
        self.embedSubtitlesCheckBoxLayout.setObjectName(u"embedSubtitlesCheckBoxLayout")
        self.horizontalSpacer5 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.embedSubtitlesCheckBoxLayout.addItem(self.horizontalSpacer5)

        self.embedSubtitlesCheckBox = QCheckBox(Tab)
        self.embedSubtitlesCheckBox.setObjectName(u"embedSubtitlesCheckBox")
        self.embedSubtitlesCheckBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.embedSubtitlesCheckBoxLayout.addWidget(self.embedSubtitlesCheckBox)

        self.horizontalSpacer6 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.embedSubtitlesCheckBoxLayout.addItem(self.horizontalSpacer6)


        self.verticalLayout.addLayout(self.embedSubtitlesCheckBoxLayout)

        self.horizontalSpacer7 = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.horizontalSpacer7)

        self.actionButtonsLayout = QHBoxLayout()
        self.actionButtonsLayout.setObjectName(u"actionButtonsLayout")
        self.horizontalSpacer8 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.actionButtonsLayout.addItem(self.horizontalSpacer8)

        self.dataPullButton = LargePushButton(Tab)
        self.dataPullButton.setObjectName(u"dataPullButton")
        self.dataPullButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon1 = QIcon(QIcon.fromTheme(u"view-refresh"))
        self.dataPullButton.setIcon(icon1)

        self.actionButtonsLayout.addWidget(self.dataPullButton)

        self.downloadButton = LargePushButton(Tab)
        self.downloadButton.setObjectName(u"downloadButton")
        self.downloadButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon2 = QIcon(QIcon.fromTheme(u"emblem-downloads"))
        self.downloadButton.setIcon(icon2)

        self.actionButtonsLayout.addWidget(self.downloadButton)

        self.horizontalSpacer9 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.actionButtonsLayout.addItem(self.horizontalSpacer9)


        self.verticalLayout.addLayout(self.actionButtonsLayout)

        self.horizontalSpacer10 = QSpacerItem(0, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.horizontalSpacer10)

        self.statusIndicatorsLayout = QHBoxLayout()
        self.statusIndicatorsLayout.setObjectName(u"statusIndicatorsLayout")
        self.horizontalSpacer11 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.statusIndicatorsLayout.addItem(self.horizontalSpacer11)

        self.statusIconLabel = QLabel(Tab)
        self.statusIconLabel.setObjectName(u"statusIconLabel")

        self.statusIndicatorsLayout.addWidget(self.statusIconLabel)

        self.horizontalSpacer12 = QSpacerItem(3, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.statusIndicatorsLayout.addItem(self.horizontalSpacer12)

        self.statusLabel = QLabel(Tab)
        self.statusLabel.setObjectName(u"statusLabel")
        font = QFont()
        font.setPointSize(14)
        self.statusLabel.setFont(font)

        self.statusIndicatorsLayout.addWidget(self.statusLabel)

        self.horizontalSpacer13 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.statusIndicatorsLayout.addItem(self.horizontalSpacer13)


        self.verticalLayout.addLayout(self.statusIndicatorsLayout)

        self.progressBar = QProgressBar(Tab)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)


        self.retranslateUi(Tab)

        self.dataPullButton.setDefault(True)
        self.downloadButton.setDefault(True)


        QMetaObject.connectSlotsByName(Tab)
    # setupUi

    def retranslateUi(self, Tab):
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("Tab", u"Paste URLs here...", None))
#if QT_CONFIG(tooltip)
        self.donationLinkLabel.setToolTip(QCoreApplication.translate("Tab", u"This app is the result of countless hours of development by Marko Peji\u0107. If it's useful to you, please consider supporting its development with a donation.<br>Thank you!", None))
#endif // QT_CONFIG(tooltip)
        self.donationLinkLabel.setText(QCoreApplication.translate("Tab", u"<a href=\"https://downloader.markopejic.com/donate\">Donate</a>", None))
        self.formatLabel.setText(QCoreApplication.translate("Tab", u"Format:", None))
#if QT_CONFIG(tooltip)
        self.formatComboBox.setToolTip(QCoreApplication.translate("Tab", u"Format Options<br>(Alt+F)", None))
#endif // QT_CONFIG(tooltip)
        self.formatComboBox.setPlaceholderText(QCoreApplication.translate("Tab", u"Unknown", None))
        self.qualityLabel.setText(QCoreApplication.translate("Tab", u"Quality:", None))
#if QT_CONFIG(tooltip)
        self.qualityComboBox.setToolTip(QCoreApplication.translate("Tab", u"Quality Options<br>(Alt+Q)", None))
#endif // QT_CONFIG(tooltip)
        self.qualityComboBox.setPlaceholderText(QCoreApplication.translate("Tab", u"Unknown", None))
        self.subtitlesLabel.setText(QCoreApplication.translate("Tab", u"Subtitles:", None))
#if QT_CONFIG(tooltip)
        self.subtitlesComboBox.setToolTip(QCoreApplication.translate("Tab", u"Subtitle Options<br>(Alt+S)", None))
#endif // QT_CONFIG(tooltip)
        self.subtitlesComboBox.setPlaceholderText(QCoreApplication.translate("Tab", u"None", None))
        self.downloadFolderLabel.setText(QCoreApplication.translate("Tab", u"Download Folder:", None))
        self.downloadFolderIndicatorLabel.setText(QCoreApplication.translate("Tab", u"None", None))
#if QT_CONFIG(tooltip)
        self.setDownloadFolderButton.setToolTip(QCoreApplication.translate("Tab", u"Change download folder<br>(Alt+C)", None))
#endif // QT_CONFIG(tooltip)
        self.setDownloadFolderButton.setText(QCoreApplication.translate("Tab", u"&Change...", None))
#if QT_CONFIG(tooltip)
        self.cropThumbnailsCheckBox.setToolTip(QCoreApplication.translate("Tab", u"Crop thumbnails / album arts square<br>(Alt+T)", None))
#endif // QT_CONFIG(tooltip)
        self.cropThumbnailsCheckBox.setText(QCoreApplication.translate("Tab", u"Crop &thumbnails square", None))
#if QT_CONFIG(tooltip)
        self.embedSubtitlesCheckBox.setToolTip(QCoreApplication.translate("Tab", u"Embed subtitles directly into audio/video files<br>(Alt+E)", None))
#endif // QT_CONFIG(tooltip)
        self.embedSubtitlesCheckBox.setText(QCoreApplication.translate("Tab", u"&Embed subtitles", None))
#if QT_CONFIG(tooltip)
        self.dataPullButton.setToolTip(QCoreApplication.translate("Tab", u"Fetch subtitle and quality options<br>(Alt+P)", None))
#endif // QT_CONFIG(tooltip)
        self.dataPullButton.setText(QCoreApplication.translate("Tab", u"Get Options", None))
#if QT_CONFIG(tooltip)
        self.downloadButton.setToolTip(QCoreApplication.translate("Tab", u"Download<br>(Alt+D)", None))
#endif // QT_CONFIG(tooltip)
        self.downloadButton.setText(QCoreApplication.translate("Tab", u"&Download", None))
        self.statusIconLabel.setText("")
        self.statusLabel.setText("")
        pass
    # retranslateUi

