# Media Downloader - Web video/audio downloader
# Copyright (C) 2024  Marko Pejić

# This file is part of Media Downloader

# Media Downloader is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Media Downloader is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtCore import QSettings

from src.ui import Ui_PreferencesDialog


class PreferencesDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_PreferencesDialog()
        self.ui.setupUi(self)
        self.connect_signals_and_slots()
        self.load_settings()


    def load_settings(self):
        self.settings_manager = QSettings()

        settings = [
            {"setting": "remember-tab-settings", "func": self.ui.restoreSettingsCheckBox.setChecked, "type": bool},
            {"setting": "remove-downloaded-urls", "func": self.ui.removeURLsCheckBox.setChecked, "type": bool},
            {"setting": "preferred-resolution", "func": lambda res: self.ui.preferredResolutionComboBox.setCurrentIndex(self.ui.preferredResolutionComboBox.findText(res)), "type": str},
            {"setting": "preferred-bitrate", "func": lambda res: self.ui.preferredBitrateComboBox.setCurrentIndex(self.ui.preferredBitrateComboBox.findText(res)), "type": str},
        ]

        for setting in settings:
            value = self.settings_manager.value(setting["setting"], type=setting["type"])
            if value or value == False:
                func = setting["func"](value)


    def save_settings(self):
        settings = [
            {"setting": "remember-tab-settings", "func": self.ui.restoreSettingsCheckBox.isChecked},
            {"setting": "remove-downloaded-urls", "func": self.ui.removeURLsCheckBox.isChecked},
            {"setting": "preferred-resolution", "func": self.ui.preferredResolutionComboBox.currentText},
            {"setting": "preferred-bitrate", "func": self.ui.preferredBitrateComboBox.currentText},
        ]
        for setting in settings:
            self.settings_manager.setValue(setting["setting"], setting["func"]())
        
        self.close()

    
    def connect_signals_and_slots(self):
        for button in self.ui.buttonBox.buttons():
            button_role = self.ui.buttonBox.buttonRole(button)
            
            if button_role == QDialogButtonBox.ButtonRole.ApplyRole:
                button.clicked.connect(self.save_settings)
            elif button_role == QDialogButtonBox.ButtonRole.RejectRole:
                button.clicked.connect(self.close)