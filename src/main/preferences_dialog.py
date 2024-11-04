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

from ui import Ui_PreferencesDialog
from .settings import Settings
from utils import update_combobox_items


class PreferencesDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_PreferencesDialog()
        self.ui.setupUi(self)
        self.connect_signals_and_slots()
        self.setup_vars()
        
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
                "set-value-func": self.ui.preferredResolutionSettingComboBox.setCurrentText,
                "get-value-func": self.ui.preferredResolutionSettingComboBox.currentText,
            },
            "preferred-bitrate": {
                "set-value-func": self.ui.preferredBitrateSettingComboBox.setCurrentText,
                "get-value-func": self.ui.preferredBitrateSettingComboBox.currentText,
            },
        }

        update_combobox_items(
            self.ui.preferredResolutionSettingComboBox,
            self.settings_manager.CONSTANT_SETTTINGS["preferred-resolutions"]
        )
        update_combobox_items(
            self.ui.preferredBitrateSettingComboBox,
            self.settings_manager.CONSTANT_SETTTINGS["preferred-bitrates"]
        )


    def setup_vars(self):
        self.slider_moved = False
        self.current_value = None
        self.loading_settings = True


    def load_settings(self, defaults=False):
        if not defaults:
            for setting_name, setting_func in self.SETTINGS.items():
                value = self.settings_manager.load_setting(setting_name)
                if value != None:
                    setting_func["set-value-func"](value)
        else:
            for setting_name, setting_func in self.SETTINGS.items():
                setting_func["set-value-func"](self.settings_manager.DEFAULT_SETTINGS[setting_name]["value"])


    def save_setting(self, setting_name):
        if not self.loading_settings:
            self.settings_manager.save_setting(setting_name, self.SETTINGS[setting_name]["get-value-func"])

    
    def connect_signals_and_slots(self):
        for button in self.ui.buttonBox.buttons():
            button_role = self.ui.buttonBox.buttonRole(button)
            
            if button_role == QDialogButtonBox.ButtonRole.DestructiveRole:
                button.clicked.connect(self.close)
            elif button_role == QDialogButtonBox.ButtonRole.ResetRole:
                button.clicked.connect(lambda: self.load_settings(defaults=True))

        self.sliders = [
            self.ui.horizontalSlider,
            self.ui.horizontalSlider2,
        ]
        for slider in self.sliders:
            slider.sliderPressed.connect(lambda slider=slider: self.record_slider_value(slider))
            slider.sliderReleased.connect(lambda slider=slider: self.change_slider_value(slider))
            slider.sliderMoved.connect(self.record_slider_moved)

        self.ui.horizontalSlider.valueChanged.connect(lambda: self.save_setting("remember-tab-settings"))
        self.ui.horizontalSlider.valueChanged.connect(lambda: self.save_setting("remove-downloaded-urls"))
        self.ui.preferredBitrateSettingComboBox.currentIndexChanged.connect(lambda: self.save_setting("preferred-bitrate"))
        self.ui.preferredResolutionSettingComboBox.currentIndexChanged.connect(lambda: self.save_setting("preferred-resolution"))


    def _exec(self):
        self.loading_settings = True
        self.load_settings()
        self.loading_settings = False
        
        self.exec()


    def record_slider_value(self, slider):
        self.current_value = slider.value()


    def record_slider_moved(self):
        self.slider_moved = True


    def change_slider_value(self, slider):
        if self.current_value == slider.value() and not self.slider_moved:
            slider.setValue(not self.current_value)

        self.slider_moved = False