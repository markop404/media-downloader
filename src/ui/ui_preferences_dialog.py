# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences_dialogisrPDR.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QSizePolicy,
    QSlider, QSpacerItem, QVBoxLayout, QWidget)

class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        if not PreferencesDialog.objectName():
            PreferencesDialog.setObjectName(u"PreferencesDialog")
        PreferencesDialog.resize(685, 360)
        PreferencesDialog.setMinimumSize(QSize(685, 360))
        PreferencesDialog.setMaximumSize(QSize(800, 450))
        self.PreferencesDialogLayout = QVBoxLayout(PreferencesDialog)
        self.PreferencesDialogLayout.setObjectName(u"PreferencesDialogLayout")
        self.topSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.PreferencesDialogLayout.addItem(self.topSpacer)

        self.restoreSettingsLayout = QHBoxLayout()
        self.restoreSettingsLayout.setObjectName(u"restoreSettingsLayout")
        self.restoreSettingsLabelLayout = QVBoxLayout()
        self.restoreSettingsLabelLayout.setObjectName(u"restoreSettingsLabelLayout")
        self.restoreSettingsMainLabel = QLabel(PreferencesDialog)
        self.restoreSettingsMainLabel.setObjectName(u"restoreSettingsMainLabel")
        self.restoreSettingsMainLabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.restoreSettingsMainLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.restoreSettingsLabelLayout.addWidget(self.restoreSettingsMainLabel)

        self.restoreSettingsDescriptionLabel = QLabel(PreferencesDialog)
        self.restoreSettingsDescriptionLabel.setObjectName(u"restoreSettingsDescriptionLabel")
        font = QFont()
        font.setPointSize(10)
        font.setWeight(QFont.ExtraLight)
        self.restoreSettingsDescriptionLabel.setFont(font)
        self.restoreSettingsDescriptionLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.restoreSettingsDescriptionLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.restoreSettingsLabelLayout.addWidget(self.restoreSettingsDescriptionLabel)


        self.restoreSettingsLayout.addLayout(self.restoreSettingsLabelLayout)

        self.restoreSettingsLayoutSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.restoreSettingsLayout.addItem(self.restoreSettingsLayoutSpacer)

        self.horizontalSlider = QSlider(PreferencesDialog)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximumSize(QSize(40, 16777215))
        self.horizontalSlider.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.horizontalSlider.setMaximum(1)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.restoreSettingsLayout.addWidget(self.horizontalSlider)


        self.PreferencesDialogLayout.addLayout(self.restoreSettingsLayout)

        self.verticalSpacer1 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.PreferencesDialogLayout.addItem(self.verticalSpacer1)

        self.removeURLsLayout = QHBoxLayout()
        self.removeURLsLayout.setObjectName(u"removeURLsLayout")
        self.removeURLsLabelLayout = QVBoxLayout()
        self.removeURLsLabelLayout.setObjectName(u"removeURLsLabelLayout")
        self.removeURLsMainLabel = QLabel(PreferencesDialog)
        self.removeURLsMainLabel.setObjectName(u"removeURLsMainLabel")
        self.removeURLsMainLabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.removeURLsMainLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.removeURLsLabelLayout.addWidget(self.removeURLsMainLabel)

        self.removeURLsDescriptionLabel = QLabel(PreferencesDialog)
        self.removeURLsDescriptionLabel.setObjectName(u"removeURLsDescriptionLabel")
        self.removeURLsDescriptionLabel.setFont(font)
        self.removeURLsDescriptionLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.removeURLsDescriptionLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.removeURLsLabelLayout.addWidget(self.removeURLsDescriptionLabel)


        self.removeURLsLayout.addLayout(self.removeURLsLabelLayout)

        self.removeURLsLayoutSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.removeURLsLayout.addItem(self.removeURLsLayoutSpacer)

        self.horizontalSlider2 = QSlider(PreferencesDialog)
        self.horizontalSlider2.setObjectName(u"horizontalSlider2")
        self.horizontalSlider2.setMaximumSize(QSize(40, 16777215))
        self.horizontalSlider2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.horizontalSlider2.setMaximum(1)
        self.horizontalSlider2.setPageStep(1)
        self.horizontalSlider2.setOrientation(Qt.Orientation.Horizontal)

        self.removeURLsLayout.addWidget(self.horizontalSlider2)


        self.PreferencesDialogLayout.addLayout(self.removeURLsLayout)

        self.verticalSpacer2 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.PreferencesDialogLayout.addItem(self.verticalSpacer2)

        self.preferredResolutionLayout = QHBoxLayout()
        self.preferredResolutionLayout.setObjectName(u"preferredResolutionLayout")
        self.preferredResolutionLabelLayout = QVBoxLayout()
        self.preferredResolutionLabelLayout.setObjectName(u"preferredResolutionLabelLayout")
        self.preferredResolutionMainLabel = QLabel(PreferencesDialog)
        self.preferredResolutionMainLabel.setObjectName(u"preferredResolutionMainLabel")
        self.preferredResolutionMainLabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.preferredResolutionMainLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.preferredResolutionLabelLayout.addWidget(self.preferredResolutionMainLabel)

        self.preferredResolutionDescriptionLabel = QLabel(PreferencesDialog)
        self.preferredResolutionDescriptionLabel.setObjectName(u"preferredResolutionDescriptionLabel")
        self.preferredResolutionDescriptionLabel.setFont(font)
        self.preferredResolutionDescriptionLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.preferredResolutionDescriptionLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.preferredResolutionLabelLayout.addWidget(self.preferredResolutionDescriptionLabel)


        self.preferredResolutionLayout.addLayout(self.preferredResolutionLabelLayout)

        self.preferredResolutionLayoutSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.preferredResolutionLayout.addItem(self.preferredResolutionLayoutSpacer)

        self.preferredResolutionComboBox = QComboBox(PreferencesDialog)
        self.preferredResolutionComboBox.setObjectName(u"preferredResolutionComboBox")
        self.preferredResolutionComboBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.preferredResolutionLayout.addWidget(self.preferredResolutionComboBox)


        self.PreferencesDialogLayout.addLayout(self.preferredResolutionLayout)

        self.verticalSpacer3 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.PreferencesDialogLayout.addItem(self.verticalSpacer3)

        self.preferredBitrateLayout = QHBoxLayout()
        self.preferredBitrateLayout.setObjectName(u"preferredBitrateLayout")
        self.preferredBitrateLabelLayout = QVBoxLayout()
        self.preferredBitrateLabelLayout.setObjectName(u"preferredBitrateLabelLayout")
        self.preferredBitrateMainLabel = QLabel(PreferencesDialog)
        self.preferredBitrateMainLabel.setObjectName(u"preferredBitrateMainLabel")
        self.preferredBitrateMainLabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.preferredBitrateMainLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.preferredBitrateLabelLayout.addWidget(self.preferredBitrateMainLabel)

        self.preferredBitrateDescriptionLabel = QLabel(PreferencesDialog)
        self.preferredBitrateDescriptionLabel.setObjectName(u"preferredBitrateDescriptionLabel")
        self.preferredBitrateDescriptionLabel.setFont(font)
        self.preferredBitrateDescriptionLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.preferredBitrateDescriptionLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.preferredBitrateLabelLayout.addWidget(self.preferredBitrateDescriptionLabel)


        self.preferredBitrateLayout.addLayout(self.preferredBitrateLabelLayout)

        self.preferredBitrateLayoutSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.preferredBitrateLayout.addItem(self.preferredBitrateLayoutSpacer)

        self.preferredBitrateComboBox = QComboBox(PreferencesDialog)
        self.preferredBitrateComboBox.setObjectName(u"preferredBitrateComboBox")
        self.preferredBitrateComboBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.preferredBitrateLayout.addWidget(self.preferredBitrateComboBox)


        self.PreferencesDialogLayout.addLayout(self.preferredBitrateLayout)

        self.buttonBoxSpacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.PreferencesDialogLayout.addItem(self.buttonBoxSpacer)

        self.buttonBox = QDialogButtonBox(PreferencesDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Apply|QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.RestoreDefaults)

        self.PreferencesDialogLayout.addWidget(self.buttonBox)


        self.retranslateUi(PreferencesDialog)

        QMetaObject.connectSlotsByName(PreferencesDialog)
    # setupUi

    def retranslateUi(self, PreferencesDialog):
        PreferencesDialog.setWindowTitle(QCoreApplication.translate("PreferencesDialog", u"Preferences", None))
        self.restoreSettingsMainLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Restore previously used settings in new tabs", None))
        self.restoreSettingsDescriptionLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Restore settings from previously used tab in new tabs", None))
        self.removeURLsMainLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Remove URLs as they are downloaded", None))
        self.removeURLsDescriptionLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Remove each URL from the text entry when it finishes downloading", None))
        self.preferredResolutionMainLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Preferred video quality", None))
        self.preferredResolutionDescriptionLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Highest resolution that gets selected by default", None))
        self.preferredBitrateMainLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Preferred audio quality", None))
        self.preferredBitrateDescriptionLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Highest bitrate that gets selected by default", None))
    # retranslateUi