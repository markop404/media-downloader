# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabLeXhCA.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QHBoxLayout, QLabel, QPlainTextEdit, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Tab(object):
    def setupUi(self, Tab):
        if not Tab.objectName():
            Tab.setObjectName(u"Tab")
        Tab.resize(609, 738)
        self.verticalLayout = QVBoxLayout(Tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plainTextEdit = QPlainTextEdit(Tab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.horizontalSpacer1 = QSpacerItem(1166, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer1)

        self.downloadOptionsFormLayout = QFormLayout()
        self.downloadOptionsFormLayout.setObjectName(u"downloadOptionsFormLayout")
        self.downloadOptionsFormLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.FieldsStayAtSizeHint)
        self.downloadOptionsFormLayout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapLongRows)
        self.downloadOptionsFormLayout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.downloadOptionsFormLayout.setFormAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.formatLabel = QLabel(Tab)
        self.formatLabel.setObjectName(u"formatLabel")

        self.downloadOptionsFormLayout.setWidget(0, QFormLayout.LabelRole, self.formatLabel)

        self.formatComboBox = QComboBox(Tab)
        self.formatComboBox.addItem("")
        self.formatComboBox.addItem("")
        self.formatComboBox.setObjectName(u"formatComboBox")

        self.downloadOptionsFormLayout.setWidget(0, QFormLayout.FieldRole, self.formatComboBox)

        self.qualityLabel = QLabel(Tab)
        self.qualityLabel.setObjectName(u"qualityLabel")

        self.downloadOptionsFormLayout.setWidget(1, QFormLayout.LabelRole, self.qualityLabel)

        self.qualityComboBox = QComboBox(Tab)
        self.qualityComboBox.setObjectName(u"qualityComboBox")
        self.qualityComboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.downloadOptionsFormLayout.setWidget(1, QFormLayout.FieldRole, self.qualityComboBox)

        self.subtitlesLabel = QLabel(Tab)
        self.subtitlesLabel.setObjectName(u"subtitlesLabel")

        self.downloadOptionsFormLayout.setWidget(2, QFormLayout.LabelRole, self.subtitlesLabel)

        self.subtitlesComboBox = QComboBox(Tab)
        self.subtitlesComboBox.setObjectName(u"subtitlesComboBox")
        self.subtitlesComboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.downloadOptionsFormLayout.setWidget(2, QFormLayout.FieldRole, self.subtitlesComboBox)

        self.downloadFolderLabel = QLabel(Tab)
        self.downloadFolderLabel.setObjectName(u"downloadFolderLabel")

        self.downloadOptionsFormLayout.setWidget(3, QFormLayout.LabelRole, self.downloadFolderLabel)

        self.downloadFolderHorizontalLayout = QHBoxLayout()
        self.downloadFolderHorizontalLayout.setSpacing(5)
        self.downloadFolderHorizontalLayout.setObjectName(u"downloadFolderHorizontalLayout")
        self.downloadFolderIndicatorLabel = QLabel(Tab)
        self.downloadFolderIndicatorLabel.setObjectName(u"downloadFolderIndicatorLabel")
        self.downloadFolderIndicatorLabel.setOpenExternalLinks(True)

        self.downloadFolderHorizontalLayout.addWidget(self.downloadFolderIndicatorLabel)

        self.setDownloadFolderPushButton = QPushButton(Tab)
        self.setDownloadFolderPushButton.setObjectName(u"setDownloadFolderPushButton")
        self.setDownloadFolderPushButton.setMaximumSize(QSize(72, 16777215))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSaveAs))
        self.setDownloadFolderPushButton.setIcon(icon)
        self.setDownloadFolderPushButton.setIconSize(QSize(18, 12))

        self.downloadFolderHorizontalLayout.addWidget(self.setDownloadFolderPushButton)


        self.downloadOptionsFormLayout.setLayout(3, QFormLayout.FieldRole, self.downloadFolderHorizontalLayout)


        self.verticalLayout.addLayout(self.downloadOptionsFormLayout)

        self.horizontalSpacer2 = QSpacerItem(697, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer2)

        self.cropthumbnailsCheckBox = QCheckBox(Tab)
        self.cropthumbnailsCheckBox.setObjectName(u"cropthumbnailsCheckBox")

        self.verticalLayout.addWidget(self.cropthumbnailsCheckBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.urlremovalCheckBox = QCheckBox(Tab)
        self.urlremovalCheckBox.setObjectName(u"urlremovalCheckBox")
        self.urlremovalCheckBox.setChecked(True)

        self.verticalLayout.addWidget(self.urlremovalCheckBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.embedSubtitlesCheckBox = QCheckBox(Tab)
        self.embedSubtitlesCheckBox.setObjectName(u"embedSubtitlesCheckBox")
        self.embedSubtitlesCheckBox.setChecked(True)

        self.verticalLayout.addWidget(self.embedSubtitlesCheckBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer3 = QSpacerItem(697, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer3)

        self.actionButtonsHorizontalLayout = QHBoxLayout()
        self.actionButtonsHorizontalLayout.setObjectName(u"actionButtonsHorizontalLayout")
        self.refreshPushButton = QPushButton(Tab)
        self.refreshPushButton.setObjectName(u"refreshPushButton")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.refreshPushButton.setIcon(icon1)
        self.refreshPushButton.setIconSize(QSize(18, 12))

        self.actionButtonsHorizontalLayout.addWidget(self.refreshPushButton, 0, Qt.AlignmentFlag.AlignRight)

        self.downloadPushButton = QPushButton(Tab)
        self.downloadPushButton.setObjectName(u"downloadPushButton")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoDown))
        self.downloadPushButton.setIcon(icon2)
        self.downloadPushButton.setIconSize(QSize(18, 12))

        self.actionButtonsHorizontalLayout.addWidget(self.downloadPushButton, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout.addLayout(self.actionButtonsHorizontalLayout)

        self.horizontalSpacer4 = QSpacerItem(697, 60, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer4)

        self.statusLabel = QLabel(Tab)
        self.statusLabel.setObjectName(u"statusLabel")
        font = QFont()
        font.setPointSize(14)
        self.statusLabel.setFont(font)
        self.statusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.statusLabel)

        self.progressBar = QProgressBar(Tab)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)


        self.retranslateUi(Tab)

        QMetaObject.connectSlotsByName(Tab)
    # setupUi

    def retranslateUi(self, Tab):
        Tab.setWindowTitle(QCoreApplication.translate("Tab", u"Form", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("Tab", u"Paste URLs here...", None))
        self.formatLabel.setText(QCoreApplication.translate("Tab", u"Format:", None))
        self.formatComboBox.setItemText(0, QCoreApplication.translate("Tab", u"Video", None))
        self.formatComboBox.setItemText(1, QCoreApplication.translate("Tab", u"Audio", None))

        self.qualityLabel.setText(QCoreApplication.translate("Tab", u"Quality:", None))
        self.qualityComboBox.setPlaceholderText(QCoreApplication.translate("Tab", u"Best", None))
        self.subtitlesLabel.setText(QCoreApplication.translate("Tab", u"Subtitles:", None))
        self.subtitlesComboBox.setPlaceholderText(QCoreApplication.translate("Tab", u"None", None))
#if QT_CONFIG(tooltip)
        self.downloadFolderLabel.setToolTip(QCoreApplication.translate("Tab", u"The folder where everything will be saved.", None))
#endif // QT_CONFIG(tooltip)
        self.downloadFolderLabel.setText(QCoreApplication.translate("Tab", u"Download Folder:", None))
        self.downloadFolderIndicatorLabel.setText(QCoreApplication.translate("Tab", u"None", None))
        self.setDownloadFolderPushButton.setText(QCoreApplication.translate("Tab", u"Change", None))
#if QT_CONFIG(tooltip)
        self.cropthumbnailsCheckBox.setToolTip(QCoreApplication.translate("Tab", u"Useful when downloading music.", None))
#endif // QT_CONFIG(tooltip)
        self.cropthumbnailsCheckBox.setText(QCoreApplication.translate("Tab", u"Crop thumbnails / album arts to square shape", None))
#if QT_CONFIG(tooltip)
        self.urlremovalCheckBox.setToolTip(QCoreApplication.translate("Tab", u"Removes each URL from the text entry when it finishes downloading.", None))
#endif // QT_CONFIG(tooltip)
        self.urlremovalCheckBox.setText(QCoreApplication.translate("Tab", u"Remove URLs as they are downloaded", None))
#if QT_CONFIG(tooltip)
        self.embedSubtitlesCheckBox.setToolTip(QCoreApplication.translate("Tab", u"Embeds subtitles into downloaded videos.", None))
#endif // QT_CONFIG(tooltip)
        self.embedSubtitlesCheckBox.setText(QCoreApplication.translate("Tab", u"Embed subtitles", None))
#if QT_CONFIG(tooltip)
        self.refreshPushButton.setToolTip(QCoreApplication.translate("Tab", u"Pulls data from the URLs, allowing you to set a custom quality and subtitle language to download.", None))
#endif // QT_CONFIG(tooltip)
        self.refreshPushButton.setText(QCoreApplication.translate("Tab", u"Pull Data", None))
        self.downloadPushButton.setText(QCoreApplication.translate("Tab", u"Download", None))
        self.statusLabel.setText("")
    # retranslateUi
