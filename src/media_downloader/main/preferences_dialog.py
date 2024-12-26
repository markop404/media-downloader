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

from ..ui import Ui_PreferencesDialog
from .settings import Settings
from .. import utils


class PreferencesDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.loading_settings = True
        self.ui = Ui_PreferencesDialog()
        self.ui.setupUi(self)
        self.connect_signals_and_slots()
        
        self.settings_manager = Settings()
        self.SETTINGS = {
            "remember-tab-settings": {
                "set-value-func": lambda value: self.ui.horizontalSlider.setValue(int(value)),
                "get-value-func": lambda: bool(self.ui.horizontalSlider.value()),
            },
            "remove-downloaded-urls": {
                "set-value-func": lambda value: self.ui.horizontalSlider2.setValue(int(value)),
                "get-value-func": lambda: bool(self.ui.horizontalSlider2.value()),
            },
            "preferred-resolution": {
                "set-value-func":
                    lambda value: 
                        self.ui.preferredResolutionSettingComboBox.setCurrentText(
                            self.settings_manager.CONSTANT_SETTINGS["preferred-resolutions"][value]
                        ),
                "get-value-func": self.ui.preferredResolutionSettingComboBox.currentData,
            },
            "preferred-bitrate": {
                "set-value-func":
                    lambda value: 
                        self.ui.preferredBitrateSettingComboBox.setCurrentText(
                            self.settings_manager.CONSTANT_SETTINGS["preferred-bitrates"][value]
                        ),
                "get-value-func": self.ui.preferredBitrateSettingComboBox.currentData,
            },
        }

        self.ui.preferredResolutionSettingComboBox.replace_all_items(
            self.settings_manager.CONSTANT_SETTINGS["preferred-resolutions"],
        )
        self.ui.preferredBitrateSettingComboBox.replace_all_items(
            self.settings_manager.CONSTANT_SETTINGS["preferred-bitrates"],
        )

        self.load_settings()
        self.setFixedSize(self.sizeHint())


    def load_settings(self, defaults=False):
        self.loading_settings = True
        
        if defaults:
            for setting_name, setting_func in self.SETTINGS.items():
                setting_func["set-value-func"](self.settings_manager.DEFAULT_SETTINGS[setting_name]["value"])
                self.settings_manager.remove(setting_name)
        else:
            for setting_name, setting_func in self.SETTINGS.items():
                value = self.settings_manager.load_setting(setting_name)
                if value != None:
                    setting_func["set-value-func"](value)

        self.loading_settings = False


    def save_setting(self, setting_name):
        if not self.loading_settings:
            self.settings_manager.save_setting(
                setting_name,
                self.SETTINGS[setting_name]["get-value-func"](),
                force=True,
            )

    
    def connect_signals_and_slots(self):
        for button in self.ui.buttonBox.buttons():
            button_role = self.ui.buttonBox.buttonRole(button)
            
            if button_role == QDialogButtonBox.ButtonRole.RejectRole:
                button.clicked.connect(self.close)
            elif button_role == QDialogButtonBox.ButtonRole.ResetRole:
                button.clicked.connect(lambda: self.load_settings(defaults=True))


        self.ui.horizontalSlider.valueChanged.connect(lambda: self.save_setting("remember-tab-settings"))
        self.ui.horizontalSlider2.valueChanged.connect(lambda: self.save_setting("remove-downloaded-urls"))
        self.ui.preferredBitrateSettingComboBox.currentIndexChanged.connect(lambda: self.save_setting("preferred-bitrate"))
        self.ui.preferredResolutionSettingComboBox.currentIndexChanged.connect(lambda: self.save_setting("preferred-resolution"))