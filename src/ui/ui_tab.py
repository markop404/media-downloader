# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabEkOnBv.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QHBoxLayout, QLabel, QPlainTextEdit, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Tab(object):
    def setupUi(self, Tab):
        if not Tab.objectName():
            Tab.setObjectName(u"Tab")
        self.verticalLayout = QVBoxLayout(Tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plainTextEdit = QPlainTextEdit(Tab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.horizontalSpacer1 = QSpacerItem(0, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.horizontalSpacer1)

        self.downloadOptionsFormLayout = QFormLayout()
        self.downloadOptionsFormLayout.setObjectName(u"downloadOptionsFormLayout")
        self.downloadOptionsFormLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.FieldsStayAtSizeHint)
        self.downloadOptionsFormLayout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.DontWrapRows)
        self.downloadOptionsFormLayout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.downloadOptionsFormLayout.setFormAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.formatLabel = QLabel(Tab)
        self.formatLabel.setObjectName(u"formatLabel")

        self.downloadOptionsFormLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.formatLabel)

        self.formatComboBox = QComboBox(Tab)
        self.formatComboBox.addItem("")
        self.formatComboBox.addItem("")
        self.formatComboBox.setObjectName(u"formatComboBox")
        self.formatComboBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.downloadOptionsFormLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.formatComboBox)

        self.qualityLabel = QLabel(Tab)
        self.qualityLabel.setObjectName(u"qualityLabel")

        self.downloadOptionsFormLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.qualityLabel)

        self.qualityComboBox = QComboBox(Tab)
        self.qualityComboBox.setObjectName(u"qualityComboBox")
        self.qualityComboBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.qualityComboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.downloadOptionsFormLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.qualityComboBox)

        self.subtitlesLabel = QLabel(Tab)
        self.subtitlesLabel.setObjectName(u"subtitlesLabel")

        self.downloadOptionsFormLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.subtitlesLabel)

        self.subtitlesComboBox = QComboBox(Tab)
        self.subtitlesComboBox.setObjectName(u"subtitlesComboBox")
        self.subtitlesComboBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.subtitlesComboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.downloadOptionsFormLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.subtitlesComboBox)

        self.downloadFolderLabel = QLabel(Tab)
        self.downloadFolderLabel.setObjectName(u"downloadFolderLabel")

        self.downloadOptionsFormLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.downloadFolderLabel)

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


        self.downloadOptionsFormLayout.setLayout(3, QFormLayout.ItemRole.FieldRole, self.downloadFolderLayout)


        self.verticalLayout.addLayout(self.downloadOptionsFormLayout)

        self.cropThumbnailsCheckBox = QCheckBox(Tab)
        self.cropThumbnailsCheckBox.setObjectName(u"cropThumbnailsCheckBox")
        self.cropThumbnailsCheckBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.verticalLayout.addWidget(self.cropThumbnailsCheckBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.embedSubtitlesCheckBox = QCheckBox(Tab)
        self.embedSubtitlesCheckBox.setObjectName(u"embedSubtitlesCheckBox")
        self.embedSubtitlesCheckBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.embedSubtitlesCheckBox.setChecked(True)

        self.verticalLayout.addWidget(self.embedSubtitlesCheckBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer3 = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.horizontalSpacer3)

        self.actionButtonsLayout = QHBoxLayout()
        self.actionButtonsLayout.setObjectName(u"actionButtonsLayout")
        self.horizontalSpacer4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.actionButtonsLayout.addItem(self.horizontalSpacer4)

        self.dataPullButton = QPushButton(Tab)
        self.dataPullButton.setObjectName(u"dataPullButton")
        self.dataPullButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.dataPullButton.setIcon(icon1)

        self.actionButtonsLayout.addWidget(self.dataPullButton)

        self.downloadButton = QPushButton(Tab)
        self.downloadButton.setObjectName(u"downloadButton")
        self.downloadButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoDown))
        self.downloadButton.setIcon(icon2)

        self.actionButtonsLayout.addWidget(self.downloadButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.actionButtonsLayout.addItem(self.horizontalSpacer5)


        self.verticalLayout.addLayout(self.actionButtonsLayout)

        self.horizontalSpacer6 = QSpacerItem(0, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.horizontalSpacer6)

        self.statusIndicatorsLayout = QHBoxLayout()
        self.statusIndicatorsLayout.setObjectName(u"statusIndicatorsLayout")
        self.horizontalSpacer7 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.statusIndicatorsLayout.addItem(self.horizontalSpacer7)

        self.statusIconLabel = QLabel(Tab)
        self.statusIconLabel.setObjectName(u"statusIconLabel")
        self.statusIconLabel.setMinimumSize(QSize(28, 28))

        self.statusIndicatorsLayout.addWidget(self.statusIconLabel)

        self.horizontalSpacer8 = QSpacerItem(3, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.statusIndicatorsLayout.addItem(self.horizontalSpacer8)

        self.statusLabel = QLabel(Tab)
        self.statusLabel.setObjectName(u"statusLabel")
        font = QFont()
        font.setPointSize(14)
        self.statusLabel.setFont(font)

        self.statusIndicatorsLayout.addWidget(self.statusLabel)

        self.horizontalSpacer9 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.statusIndicatorsLayout.addItem(self.horizontalSpacer9)


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
#if QT_CONFIG(tooltip)
        self.plainTextEdit.setToolTip(QCoreApplication.translate("Tab", u"Each URL should be pasted on it's own line.", None))
#endif // QT_CONFIG(tooltip)
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("Tab", u"Paste URLs here...", None))
        self.formatLabel.setText(QCoreApplication.translate("Tab", u"<u>F</u>ormat:", None))
        self.formatComboBox.setItemText(0, QCoreApplication.translate("Tab", u"Video", None))
        self.formatComboBox.setItemText(1, QCoreApplication.translate("Tab", u"Audio", None))

#if QT_CONFIG(tooltip)
        self.formatComboBox.setToolTip(QCoreApplication.translate("Tab", u"Format options<br>(Alt+F)", None))
#endif // QT_CONFIG(tooltip)
        self.qualityLabel.setText(QCoreApplication.translate("Tab", u"<u>Q</u>uality:", None))
#if QT_CONFIG(tooltip)
        self.qualityComboBox.setToolTip(QCoreApplication.translate("Tab", u"Quality options<br>(Alt+Q)", None))
#endif // QT_CONFIG(tooltip)
        self.qualityComboBox.setPlaceholderText(QCoreApplication.translate("Tab", u"Best", None))
        self.subtitlesLabel.setText(QCoreApplication.translate("Tab", u"<u>S</u>ubtitles:", None))
#if QT_CONFIG(tooltip)
        self.subtitlesComboBox.setToolTip(QCoreApplication.translate("Tab", u"Subtitle options<br>(Alt+S)", None))
#endif // QT_CONFIG(tooltip)
        self.subtitlesComboBox.setPlaceholderText(QCoreApplication.translate("Tab", u"None", None))
        self.downloadFolderLabel.setText(QCoreApplication.translate("Tab", u"Download Folder:", None))
        self.downloadFolderIndicatorLabel.setText(QCoreApplication.translate("Tab", u"None", None))
#if QT_CONFIG(tooltip)
        self.setDownloadFolderButton.setToolTip(QCoreApplication.translate("Tab", u"Change download folder<br>(Alt+C)", None))
#endif // QT_CONFIG(tooltip)
        self.setDownloadFolderButton.setText(QCoreApplication.translate("Tab", u"&Change...", None))
#if QT_CONFIG(tooltip)
        self.cropThumbnailsCheckBox.setToolTip(QCoreApplication.translate("Tab", u"Crop thumbnails / album arts to square shape (useful when downloading music)<br>(Alt+T)", None))
#endif // QT_CONFIG(tooltip)
        self.cropThumbnailsCheckBox.setText(QCoreApplication.translate("Tab", u"Crop &thumbnails square", None))
#if QT_CONFIG(tooltip)
        self.embedSubtitlesCheckBox.setToolTip(QCoreApplication.translate("Tab", u"Embed subtitles directly into audio / video files instead of downloading them to a separate file<br>(Alt+E)", None))
#endif // QT_CONFIG(tooltip)
        self.embedSubtitlesCheckBox.setText(QCoreApplication.translate("Tab", u"&Embed subtitles", None))
#if QT_CONFIG(tooltip)
        self.dataPullButton.setToolTip(QCoreApplication.translate("Tab", u"Load subtitle and quality options<br>(Alt+L)", None))
#endif // QT_CONFIG(tooltip)
        self.dataPullButton.setText(QCoreApplication.translate("Tab", u"&Load Options", None))
#if QT_CONFIG(tooltip)
        self.downloadButton.setToolTip(QCoreApplication.translate("Tab", u"Alt+D", None))
#endif // QT_CONFIG(tooltip)
        self.downloadButton.setText(QCoreApplication.translate("Tab", u"&Download", None))
        pass
    # retranslateUi

