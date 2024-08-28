# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowuEQJii.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(590, 665)
        MainWindow.setMinimumSize(QSize(400, 550))
        icon = QIcon()
        icon.addFile(u"icons/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.actionExit.setIcon(icon1)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout))
        self.actionAbout.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.horizontalSpacer1 = QSpacerItem(40, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer1)

        self.downloadOptionsFormLayout = QFormLayout()
        self.downloadOptionsFormLayout.setObjectName(u"downloadOptionsFormLayout")
        self.downloadOptionsFormLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.FieldsStayAtSizeHint)
        self.downloadOptionsFormLayout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapLongRows)
        self.downloadOptionsFormLayout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.downloadOptionsFormLayout.setFormAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.formatLabel = QLabel(self.centralwidget)
        self.formatLabel.setObjectName(u"formatLabel")

        self.downloadOptionsFormLayout.setWidget(0, QFormLayout.LabelRole, self.formatLabel)

        self.formatComboBox = QComboBox(self.centralwidget)
        self.formatComboBox.addItem("")
        self.formatComboBox.addItem("")
        self.formatComboBox.setObjectName(u"formatComboBox")

        self.downloadOptionsFormLayout.setWidget(0, QFormLayout.FieldRole, self.formatComboBox)

        self.qualityLabel = QLabel(self.centralwidget)
        self.qualityLabel.setObjectName(u"qualityLabel")

        self.downloadOptionsFormLayout.setWidget(1, QFormLayout.LabelRole, self.qualityLabel)

        self.qualityComboBox = QComboBox(self.centralwidget)
        self.qualityComboBox.setObjectName(u"qualityComboBox")
        self.qualityComboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.downloadOptionsFormLayout.setWidget(1, QFormLayout.FieldRole, self.qualityComboBox)

        self.subtitlesLabel = QLabel(self.centralwidget)
        self.subtitlesLabel.setObjectName(u"subtitlesLabel")

        self.downloadOptionsFormLayout.setWidget(2, QFormLayout.LabelRole, self.subtitlesLabel)

        self.subtitlesComboBox = QComboBox(self.centralwidget)
        self.subtitlesComboBox.setObjectName(u"subtitlesComboBox")
        self.subtitlesComboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.downloadOptionsFormLayout.setWidget(2, QFormLayout.FieldRole, self.subtitlesComboBox)

        self.downloadFolderLabel = QLabel(self.centralwidget)
        self.downloadFolderLabel.setObjectName(u"downloadFolderLabel")

        self.downloadOptionsFormLayout.setWidget(3, QFormLayout.LabelRole, self.downloadFolderLabel)

        self.downloadFolderHorizontalLayout = QHBoxLayout()
        self.downloadFolderHorizontalLayout.setSpacing(5)
        self.downloadFolderHorizontalLayout.setObjectName(u"downloadFolderHorizontalLayout")
        self.downloadFolderIndicatorLabel = QLabel(self.centralwidget)
        self.downloadFolderIndicatorLabel.setObjectName(u"downloadFolderIndicatorLabel")
        self.downloadFolderIndicatorLabel.setOpenExternalLinks(True)

        self.downloadFolderHorizontalLayout.addWidget(self.downloadFolderIndicatorLabel)

        self.setDownloadFolderPushButton = QPushButton(self.centralwidget)
        self.setDownloadFolderPushButton.setObjectName(u"setDownloadFolderPushButton")
        self.setDownloadFolderPushButton.setMaximumSize(QSize(72, 16777215))
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSaveAs))
        self.setDownloadFolderPushButton.setIcon(icon3)
        self.setDownloadFolderPushButton.setIconSize(QSize(18, 12))

        self.downloadFolderHorizontalLayout.addWidget(self.setDownloadFolderPushButton)


        self.downloadOptionsFormLayout.setLayout(3, QFormLayout.FieldRole, self.downloadFolderHorizontalLayout)


        self.verticalLayout.addLayout(self.downloadOptionsFormLayout)

        self.horizontalSpacer2 = QSpacerItem(40, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer2)

        self.urlremovalCheckBox = QCheckBox(self.centralwidget)
        self.urlremovalCheckBox.setObjectName(u"urlremovalCheckBox")
        self.urlremovalCheckBox.setChecked(True)

        self.verticalLayout.addWidget(self.urlremovalCheckBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.cropthumbnailsCheckBox = QCheckBox(self.centralwidget)
        self.cropthumbnailsCheckBox.setObjectName(u"cropthumbnailsCheckBox")

        self.verticalLayout.addWidget(self.cropthumbnailsCheckBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.embedSubtitlesCheckBox = QCheckBox(self.centralwidget)
        self.embedSubtitlesCheckBox.setObjectName(u"embedSubtitlesCheckBox")
        self.embedSubtitlesCheckBox.setChecked(True)

        self.verticalLayout.addWidget(self.embedSubtitlesCheckBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer3 = QSpacerItem(40, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer3)

        self.actionButtonsHorizontalLayout = QHBoxLayout()
        self.actionButtonsHorizontalLayout.setObjectName(u"actionButtonsHorizontalLayout")
        self.refreshPushButton = QPushButton(self.centralwidget)
        self.refreshPushButton.setObjectName(u"refreshPushButton")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.refreshPushButton.setIcon(icon4)
        self.refreshPushButton.setIconSize(QSize(18, 12))

        self.actionButtonsHorizontalLayout.addWidget(self.refreshPushButton, 0, Qt.AlignmentFlag.AlignRight)

        self.downloadPushButton = QPushButton(self.centralwidget)
        self.downloadPushButton.setObjectName(u"downloadPushButton")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoDown))
        self.downloadPushButton.setIcon(icon5)
        self.downloadPushButton.setIconSize(QSize(18, 12))

        self.actionButtonsHorizontalLayout.addWidget(self.downloadPushButton, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout.addLayout(self.actionButtonsHorizontalLayout)

        self.horizontalSpacer4 = QSpacerItem(40, 60, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer4)

        self.statusLabel = QLabel(self.centralwidget)
        self.statusLabel.setObjectName(u"statusLabel")
        font = QFont()
        font.setPointSize(14)
        self.statusLabel.setFont(font)

        self.verticalLayout.addWidget(self.statusLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 590, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.downloadPushButton.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Media Downloader", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"&Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"&About", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Paste URLs here...", None))
        self.formatLabel.setText(QCoreApplication.translate("MainWindow", u"Format:", None))
        self.formatComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Video", None))
        self.formatComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Audio", None))

        self.qualityLabel.setText(QCoreApplication.translate("MainWindow", u"Quality:", None))
        self.qualityComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Best", None))
        self.subtitlesLabel.setText(QCoreApplication.translate("MainWindow", u"Subtitles:", None))
        self.subtitlesComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"None", None))
#if QT_CONFIG(tooltip)
        self.downloadFolderLabel.setToolTip(QCoreApplication.translate("MainWindow", u"The folder where everything will be saved.", None))
#endif // QT_CONFIG(tooltip)
        self.downloadFolderLabel.setText(QCoreApplication.translate("MainWindow", u"Download Folder:", None))
        self.downloadFolderIndicatorLabel.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.setDownloadFolderPushButton.setText(QCoreApplication.translate("MainWindow", u"Change", None))
#if QT_CONFIG(tooltip)
        self.urlremovalCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"Removes each URL from the text entry when it finishes downloading.", None))
#endif // QT_CONFIG(tooltip)
        self.urlremovalCheckBox.setText(QCoreApplication.translate("MainWindow", u"Remove URLs as they are downloaded", None))
#if QT_CONFIG(tooltip)
        self.cropthumbnailsCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"Useful when downloading music.", None))
#endif // QT_CONFIG(tooltip)
        self.cropthumbnailsCheckBox.setText(QCoreApplication.translate("MainWindow", u"Crop thumbnails / album arts", None))
#if QT_CONFIG(tooltip)
        self.embedSubtitlesCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"Embeds subtitles into downloaded videos.", None))
#endif // QT_CONFIG(tooltip)
        self.embedSubtitlesCheckBox.setText(QCoreApplication.translate("MainWindow", u"Embed subtitles", None))
#if QT_CONFIG(tooltip)
        self.refreshPushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Refreshes the data from the URLs, allowing you to set a custom quality and subtitle language to download.", None))
#endif // QT_CONFIG(tooltip)
        self.refreshPushButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.downloadPushButton.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"Fi&le", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi
