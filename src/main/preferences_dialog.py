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

from src.ui import Ui_PreferencesDialog
from .settings import Settings


class PreferencesDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_PreferencesDialog()
        self.ui.setupUi(self)
        self.connect_signals_and_slots()
        
        self.settings_manager = Settings()
        self.SETTINGS = [
            {
                "name": "remember-tab-settings",
                "set-value-func": self.ui.restoreSettingsCheckBox.setChecked,
                "get-value-func": self.ui.restoreSettingsCheckBox.isChecked,
            },
            {
                "name": "remove-downloaded-urls",
                "set-value-func": self.ui.removeURLsCheckBox.setChecked,
                "get-value-func": self.ui.removeURLsCheckBox.isChecked,
            },
            {
                "name": "preferred-resolution",
                "set-value-func": self.ui.preferredResolutionComboBox.setCurrentText,
                "get-value-func": self.ui.preferredResolutionComboBox.currentText,
            },
            {
                "name": "preferred-bitrate",
                "set-value-func": self.ui.preferredBitrateComboBox.setCurrentText,
                "get-value-func": self.ui.preferredBitrateComboBox.currentText,
            },
        ]

        for resolution in self.settings_manager.CONSTANT_SETTTINGS["preferred-resolutions"]:
            self.ui.preferredResolutionComboBox.addItem(resolution)
        for bitrate in self.settings_manager.CONSTANT_SETTTINGS["preferred-bitrates"]:
            self.ui.preferredBitrateComboBox.addItem(bitrate)


    def load_settings(self, defaults=False):
        if not defaults:
            for setting in self.SETTINGS:
                value = self.settings_manager.load_setting(setting["name"])
                if value != None:
                    setting["set-value-func"](value)
        else:
            for setting in self.SETTINGS:
                setting["set-value-func"](self.settings_manager.DEFAULT_SETTINGS[setting["name"]]["value"])


    def save_and_close(self):
        for setting in self.SETTINGS:
            self.settings_manager.save_setting(setting["name"], setting["get-value-func"]())
      
        self.close()

    
    def connect_signals_and_slots(self):
        for button in self.ui.buttonBox.buttons():
            button_role = self.ui.buttonBox.buttonRole(button)
            
            if button_role == QDialogButtonBox.ButtonRole.ApplyRole:
                button.clicked.connect(self.save_and_close)
            elif button_role == QDialogButtonBox.ButtonRole.RejectRole:
                button.clicked.connect(self.close)
            elif button_role == QDialogButtonBox.ButtonRole.ResetRole:
                button.clicked.connect(lambda: self.load_settings(defaults=True))


    def _exec(self):
        self.load_settings()
        self.exec()