# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabPoaYDJ.ui'
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
        Tab.resize(636, 682)
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
        self.formatComboBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.downloadOptionsFormLayout.setWidget(0, QFormLayout.FieldRole, self.formatComboBox)

        self.qualityLabel = QLabel(Tab)
        self.qualityLabel.setObjectName(u"qualityLabel")

        self.downloadOptionsFormLayout.setWidget(1, QFormLayout.LabelRole, self.qualityLabel)

        self.qualityComboBox = QComboBox(Tab)
        self.qualityComboBox.setObjectName(u"qualityComboBox")
        self.qualityComboBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.qualityComboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.downloadOptionsFormLayout.setWidget(1, QFormLayout.FieldRole, self.qualityComboBox)

        self.subtitlesLabel = QLabel(Tab)
        self.subtitlesLabel.setObjectName(u"subtitlesLabel")

        self.downloadOptionsFormLayout.setWidget(2, QFormLayout.LabelRole, self.subtitlesLabel)

        self.subtitlesComboBox = QComboBox(Tab)
        self.subtitlesComboBox.setObjectName(u"subtitlesComboBox")
        self.subtitlesComboBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.subtitlesComboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.downloadOptionsFormLayout.setWidget(2, QFormLayout.FieldRole, self.subtitlesComboBox)

        self.downloadFolderLabel = QLabel(Tab)
        self.downloadFolderLabel.setObjectName(u"downloadFolderLabel")

        self.downloadOptionsFormLayout.setWidget(3, QFormLayout.LabelRole, self.downloadFolderLabel)

        self.downloadFolderLayout = QHBoxLayout()
        self.downloadFolderLayout.setObjectName(u"downloadFolderLayout")
        self.downloadFolderIndicatorLabel = QLabel(Tab)
        self.downloadFolderIndicatorLabel.setObjectName(u"downloadFolderIndicatorLabel")
        self.downloadFolderIndicatorLabel.setOpenExternalLinks(True)

        self.downloadFolderLayout.addWidget(self.downloadFolderIndicatorLabel)

        self.setDownloadFolderButton = QPushButton(Tab)
        self.setDownloadFolderButton.setObjectName(u"setDownloadFolderButton")
        self.setDownloadFolderButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSaveAs))
        self.setDownloadFolderButton.setIcon(icon)

        self.downloadFolderLayout.addWidget(self.setDownloadFolderButton)


        self.downloadOptionsFormLayout.setLayout(3, QFormLayout.FieldRole, self.downloadFolderLayout)


        self.verticalLayout.addLayout(self.downloadOptionsFormLayout)

        self.horizontalSpacer2 = QSpacerItem(697, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer2)

        self.cropThumbnailsCheckBox = QCheckBox(Tab)
        self.cropThumbnailsCheckBox.setObjectName(u"cropThumbnailsCheckBox")
        self.cropThumbnailsCheckBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.verticalLayout.addWidget(self.cropThumbnailsCheckBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.urlremovalCheckBox = QCheckBox(Tab)
        self.urlremovalCheckBox.setObjectName(u"urlremovalCheckBox")
        self.urlremovalCheckBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.urlremovalCheckBox.setChecked(True)

        self.verticalLayout.addWidget(self.urlremovalCheckBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.embedSubtitlesCheckBox = QCheckBox(Tab)
        self.embedSubtitlesCheckBox.setObjectName(u"embedSubtitlesCheckBox")
        self.embedSubtitlesCheckBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.embedSubtitlesCheckBox.setChecked(True)

        self.verticalLayout.addWidget(self.embedSubtitlesCheckBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer3 = QSpacerItem(697, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer3)

        self.actionButtonsLayout = QHBoxLayout()
        self.actionButtonsLayout.setObjectName(u"actionButtonsLayout")
        self.horizontalSpacer4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.actionButtonsLayout.addItem(self.horizontalSpacer4)

        self.dataPullButton = QPushButton(Tab)
        self.dataPullButton.setObjectName(u"dataPullButton")
        self.dataPullButton.setMinimumSize(QSize(110, 32))
        self.dataPullButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.dataPullButton.setIcon(icon1)

        self.actionButtonsLayout.addWidget(self.dataPullButton)

        self.downloadButton = QPushButton(Tab)
        self.downloadButton.setObjectName(u"downloadButton")
        self.downloadButton.setMinimumSize(QSize(110, 32))
        self.downloadButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoDown))
        self.downloadButton.setIcon(icon2)

        self.actionButtonsLayout.addWidget(self.downloadButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.actionButtonsLayout.addItem(self.horizontalSpacer5)


        self.verticalLayout.addLayout(self.actionButtonsLayout)

        self.horizontalSpacer6 = QSpacerItem(697, 60, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer6)

        self.statusIndicatorsLayout = QHBoxLayout()
        self.statusIndicatorsLayout.setObjectName(u"statusIndicatorsLayout")
        self.horizontalSpacer7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.statusIndicatorsLayout.addItem(self.horizontalSpacer7)

        self.statusIconLabel = QLabel(Tab)
        self.statusIconLabel.setObjectName(u"statusIconLabel")

        self.statusIndicatorsLayout.addWidget(self.statusIconLabel)

        self.statusLabel = QLabel(Tab)
        self.statusLabel.setObjectName(u"statusLabel")
        font = QFont()
        font.setFamilies([u"Cantarell"])
        font.setPointSize(14)
        self.statusLabel.setFont(font)

        self.statusIndicatorsLayout.addWidget(self.statusLabel)

        self.horizontalSpacer8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.statusIndicatorsLayout.addItem(self.horizontalSpacer8)


        self.verticalLayout.addLayout(self.statusIndicatorsLayout)

        self.progressBar = QProgressBar(Tab)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)


        self.retranslateUi(Tab)

        QMetaObject.connectSlotsByName(Tab)
    # setupUi

    def retranslateUi(self, Tab):
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("Tab", u"Paste URLs here...", None))
        self.formatLabel.setText(QCoreApplication.translate("Tab", u"Format:", None))
        self.formatComboBox.setItemText(0, QCoreApplication.translate("Tab", u"Video", None))
        self.formatComboBox.setItemText(1, QCoreApplication.translate("Tab", u"Audio", None))

        self.qualityLabel.setText(QCoreApplication.translate("Tab", u"Quality:", None))
        self.qualityComboBox.setPlaceholderText(QCoreApplication.translate("Tab", u"Best", None))
        self.subtitlesLabel.setText(QCoreApplication.translate("Tab", u"Subtitles:", None))
        self.subtitlesComboBox.setPlaceholderText(QCoreApplication.translate("Tab", u"None", None))
        self.downloadFolderLabel.setText(QCoreApplication.translate("Tab", u"Download Folder:", None))
        self.downloadFolderIndicatorLabel.setText(QCoreApplication.translate("Tab", u"None", None))
        self.setDownloadFolderButton.setText(QCoreApplication.translate("Tab", u"&Change", None))
#if QT_CONFIG(tooltip)
        self.cropThumbnailsCheckBox.setToolTip(QCoreApplication.translate("Tab", u"Useful when downloading music.", None))
#endif // QT_CONFIG(tooltip)
        self.cropThumbnailsCheckBox.setText(QCoreApplication.translate("Tab", u"Crop &thumbnails / album arts to square shape", None))
#if QT_CONFIG(tooltip)
        self.urlremovalCheckBox.setToolTip(QCoreApplication.translate("Tab", u"Removes each URL from the text entry when it finishes downloading.", None))
#endif // QT_CONFIG(tooltip)
        self.urlremovalCheckBox.setText(QCoreApplication.translate("Tab", u"Remove &URLs as they are downloaded", None))
#if QT_CONFIG(tooltip)
        self.embedSubtitlesCheckBox.setToolTip(QCoreApplication.translate("Tab", u"Embeds subtitles into downloaded videos.", None))
#endif // QT_CONFIG(tooltip)
        self.embedSubtitlesCheckBox.setText(QCoreApplication.translate("Tab", u"Embed &subtitles", None))
#if QT_CONFIG(tooltip)
        self.dataPullButton.setToolTip(QCoreApplication.translate("Tab", u"Pulls data from the URLs, allowing you to set a custom quality and subtitle language to download.", None))
#endif // QT_CONFIG(tooltip)
        self.dataPullButton.setText(QCoreApplication.translate("Tab", u"&Pull Data", None))
        self.downloadButton.setText(QCoreApplication.translate("Tab", u"&Download", None))
        self.statusIconLabel.setText("")
        self.statusLabel.setText("")
        pass
    # retranslateUi