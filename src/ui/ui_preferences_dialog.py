# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences_dialogsgFxXP.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from custom_widgets.combobox import ComboBox
from custom_widgets.toggle import Toggle

class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        if not PreferencesDialog.objectName():
            PreferencesDialog.setObjectName(u"PreferencesDialog")
        self.PreferencesDialogLayout = QVBoxLayout(PreferencesDialog)
        self.PreferencesDialogLayout.setObjectName(u"PreferencesDialogLayout")
        self.topSpacer = QSpacerItem(0, 21, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.PreferencesDialogLayout.addItem(self.topSpacer)

        self.restoreSettingsLayout = QHBoxLayout()
        self.restoreSettingsLayout.setObjectName(u"restoreSettingsLayout")
        self.restoreSettingsLabelLayout = QVBoxLayout()
        self.restoreSettingsLabelLayout.setObjectName(u"restoreSettingsLabelLayout")
        self.restoreSettingsMainLabel = QLabel(PreferencesDialog)
        self.restoreSettingsMainLabel.setObjectName(u"restoreSettingsMainLabel")
        font = QFont()
        font.setWeight(QFont.DemiBold)
        self.restoreSettingsMainLabel.setFont(font)
        self.restoreSettingsMainLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.restoreSettingsLabelLayout.addWidget(self.restoreSettingsMainLabel)

        self.restoreSettingsDescriptionLabel = QLabel(PreferencesDialog)
        self.restoreSettingsDescriptionLabel.setObjectName(u"restoreSettingsDescriptionLabel")
        font1 = QFont()
        font1.setWeight(QFont.Thin)
        self.restoreSettingsDescriptionLabel.setFont(font1)
        self.restoreSettingsDescriptionLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.restoreSettingsLabelLayout.addWidget(self.restoreSettingsDescriptionLabel)


        self.restoreSettingsLayout.addLayout(self.restoreSettingsLabelLayout)

        self.restoreSettingsLayoutSpacer = QSpacerItem(200, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.restoreSettingsLayout.addItem(self.restoreSettingsLayoutSpacer)

        self.horizontalSlider = Toggle(PreferencesDialog)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.horizontalSlider.setMaximum(1)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.restoreSettingsLayout.addWidget(self.horizontalSlider)


        self.PreferencesDialogLayout.addLayout(self.restoreSettingsLayout)

        self.verticalSpacer1 = QSpacerItem(0, 21, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.PreferencesDialogLayout.addItem(self.verticalSpacer1)

        self.removeURLsLayout = QHBoxLayout()
        self.removeURLsLayout.setObjectName(u"removeURLsLayout")
        self.removeURLsLabelLayout = QVBoxLayout()
        self.removeURLsLabelLayout.setObjectName(u"removeURLsLabelLayout")
        self.removeURLsMainLabel = QLabel(PreferencesDialog)
        self.removeURLsMainLabel.setObjectName(u"removeURLsMainLabel")
        self.removeURLsMainLabel.setFont(font)
        self.removeURLsMainLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.removeURLsLabelLayout.addWidget(self.removeURLsMainLabel)

        self.removeURLsDescriptionLabel = QLabel(PreferencesDialog)
        self.removeURLsDescriptionLabel.setObjectName(u"removeURLsDescriptionLabel")
        self.removeURLsDescriptionLabel.setFont(font1)
        self.removeURLsDescriptionLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.removeURLsLabelLayout.addWidget(self.removeURLsDescriptionLabel)


        self.removeURLsLayout.addLayout(self.removeURLsLabelLayout)

        self.removeURLsLayoutSpacer = QSpacerItem(200, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.removeURLsLayout.addItem(self.removeURLsLayoutSpacer)

        self.horizontalSlider2 = Toggle(PreferencesDialog)
        self.horizontalSlider2.setObjectName(u"horizontalSlider2")
        self.horizontalSlider2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.horizontalSlider2.setMaximum(1)
        self.horizontalSlider2.setPageStep(1)
        self.horizontalSlider2.setOrientation(Qt.Orientation.Horizontal)

        self.removeURLsLayout.addWidget(self.horizontalSlider2)


        self.PreferencesDialogLayout.addLayout(self.removeURLsLayout)

        self.verticalSpacer2 = QSpacerItem(0, 21, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.PreferencesDialogLayout.addItem(self.verticalSpacer2)

        self.preferredResolutionSettingLayout = QHBoxLayout()
        self.preferredResolutionSettingLayout.setObjectName(u"preferredResolutionSettingLayout")
        self.preferredResolutionSettingLabelLayout = QVBoxLayout()
        self.preferredResolutionSettingLabelLayout.setObjectName(u"preferredResolutionSettingLabelLayout")
        self.preferredResolutionMainLabel = QLabel(PreferencesDialog)
        self.preferredResolutionMainLabel.setObjectName(u"preferredResolutionMainLabel")
        self.preferredResolutionMainLabel.setFont(font)
        self.preferredResolutionMainLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.preferredResolutionSettingLabelLayout.addWidget(self.preferredResolutionMainLabel)

        self.preferredResolutionDescriptionLabel = QLabel(PreferencesDialog)
        self.preferredResolutionDescriptionLabel.setObjectName(u"preferredResolutionDescriptionLabel")
        self.preferredResolutionDescriptionLabel.setFont(font1)
        self.preferredResolutionDescriptionLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.preferredResolutionSettingLabelLayout.addWidget(self.preferredResolutionDescriptionLabel)


        self.preferredResolutionSettingLayout.addLayout(self.preferredResolutionSettingLabelLayout)

        self.preferredResolutionSettingLayoutSpacer = QSpacerItem(200, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.preferredResolutionSettingLayout.addItem(self.preferredResolutionSettingLayoutSpacer)

        self.preferredResolutionSettingComboBox = ComboBox(PreferencesDialog)
        self.preferredResolutionSettingComboBox.setObjectName(u"preferredResolutionSettingComboBox")
        self.preferredResolutionSettingComboBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.preferredResolutionSettingLayout.addWidget(self.preferredResolutionSettingComboBox)


        self.PreferencesDialogLayout.addLayout(self.preferredResolutionSettingLayout)

        self.verticalSpacer3 = QSpacerItem(0, 21, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.PreferencesDialogLayout.addItem(self.verticalSpacer3)

        self.preferredBitrateSettingLayout = QHBoxLayout()
        self.preferredBitrateSettingLayout.setObjectName(u"preferredBitrateSettingLayout")
        self.preferredBitrateSettingLabelLayout = QVBoxLayout()
        self.preferredBitrateSettingLabelLayout.setObjectName(u"preferredBitrateSettingLabelLayout")
        self.preferredBitrateSettingMainLabel = QLabel(PreferencesDialog)
        self.preferredBitrateSettingMainLabel.setObjectName(u"preferredBitrateSettingMainLabel")
        self.preferredBitrateSettingMainLabel.setFont(font)
        self.preferredBitrateSettingMainLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.preferredBitrateSettingLabelLayout.addWidget(self.preferredBitrateSettingMainLabel)

        self.preferredBitrateSettingDescriptionLabel = QLabel(PreferencesDialog)
        self.preferredBitrateSettingDescriptionLabel.setObjectName(u"preferredBitrateSettingDescriptionLabel")
        self.preferredBitrateSettingDescriptionLabel.setFont(font1)
        self.preferredBitrateSettingDescriptionLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.preferredBitrateSettingLabelLayout.addWidget(self.preferredBitrateSettingDescriptionLabel)


        self.preferredBitrateSettingLayout.addLayout(self.preferredBitrateSettingLabelLayout)

        self.preferredBitrateSettingLayoutSpacer = QSpacerItem(200, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.preferredBitrateSettingLayout.addItem(self.preferredBitrateSettingLayoutSpacer)

        self.preferredBitrateSettingComboBox = ComboBox(PreferencesDialog)
        self.preferredBitrateSettingComboBox.setObjectName(u"preferredBitrateSettingComboBox")
        self.preferredBitrateSettingComboBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.preferredBitrateSettingLayout.addWidget(self.preferredBitrateSettingComboBox)


        self.PreferencesDialogLayout.addLayout(self.preferredBitrateSettingLayout)

        self.buttonBoxSpacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.PreferencesDialogLayout.addItem(self.buttonBoxSpacer)

        self.buttonBox = QDialogButtonBox(PreferencesDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close|QDialogButtonBox.StandardButton.RestoreDefaults)

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
        self.preferredBitrateSettingMainLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Preferred audio quality", None))
        self.preferredBitrateSettingDescriptionLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Highest bitrate that gets selected by default", None))
    # retranslateUi

