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


import threading
import time

from PySide6.QtWidgets import QMainWindow, QWidget, QMenu
from PySide6.QtGui import QIcon, QKeySequence, QShortcut

from .. import main
from ..ui import Ui_TabButtons, Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.connect_signals_and_slots()
        
        self.highest_tab_number = 0
        self.popup_window_running = False
        
        self.settings_manager = main.Settings()
        self.SETTINGS = [
            {
                "name": "window-geometry",
                "set-value-func": self.restoreGeometry,
                "get-value-func": self.saveGeometry,

            },
            {
                "name": "window-state",
                "set-value-func": self.restoreState,
                "get-value-func": self.saveState,
            },
        ]
        self.load_settings()

        self.create_new_tab()


    def closeEvent(self, event):
        self.save_settings()
        super().closeEvent(event)
        event.accept()
    

    def load_settings(self):
        for setting in self.SETTINGS:
            value = self.settings_manager.value(setting["name"])
            if value != None:
                setting["set-value-func"](value)


    def save_settings(self):
        for setting in self.SETTINGS:
            self.settings_manager.save_setting(setting["name"], setting["get-value-func"]())
        
        self.ui.tabWidget.currentWidget().save_settings()


    def setup_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.about_dialog = main.AboutDialog(self)
        self.keyboard_shortcuts_dialog = main.KeyboardShortcutsDialog(self)
        self.preferences_dialog = main.PreferencesDialog(self)

        self.tab_button_layout = QWidget()
        self.tab_buttons = Ui_TabButtons()
        self.tab_buttons.setupUi(self.tab_button_layout)
        
        self.main_menu = QMenu()
        self.main_menu.addAction(self.ui.actionRetryAll)
        self.main_menu.addAction(self.ui.actionPreferences)
        self.main_menu.addSeparator()
        self.main_menu.addAction(self.ui.actionKeyboardShortcuts)
        self.main_menu.addAction(self.ui.actionAbout)
        self.tab_buttons.menuButton.setMenu(self.main_menu)

        self.ui.tabWidget.setCornerWidget(self.tab_button_layout)

        for i in range(1, 10):
            QShortcut(QKeySequence(f"Alt+{i}"), self).activated.connect(lambda i=i: self.switch_tab(i - 1))
        QShortcut(QKeySequence("Alt+0"), self).activated.connect(lambda: self.switch_tab(9))
        QShortcut(QKeySequence("Ctrl+PgUp"), self).activated.connect(lambda: self.switch_tab(move="left"))
        QShortcut(QKeySequence("Ctrl+PgDown"), self).activated.connect(lambda: self.switch_tab(move="right"))
        QShortcut(QKeySequence("Ctrl+w"), self).activated.connect(self.close_tab)


    def connect_signals_and_slots(self):
        self.ui.actionRetryAll.triggered.connect(self.retry_all)
        self.ui.actionAbout.triggered.connect(self.about_dialog._exec)
        self.ui.actionKeyboardShortcuts.triggered.connect(self.keyboard_shortcuts_dialog.exec)
        self.ui.actionPreferences.triggered.connect(self.exec_preferences)
        self.tab_buttons.newTabButton.clicked.connect(self.create_new_tab)
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)
    

    def retry_all(self):
        for tab_index in range(self.ui.tabWidget.count()):
            self.ui.tabWidget.widget(tab_index).retry_failed()


    def exec_preferences(self):
        self.preferences_dialog.exec()

        for tab_index in range(self.ui.tabWidget.count()):
            self.ui.tabWidget.widget(tab_index).update_settings()


    def create_new_tab(self):
        self.highest_tab_number += 1
        if current_tab := self.ui.tabWidget.currentWidget():
            current_tab.save_settings()
        
        new_tab = main.Tab(self, self.highest_tab_number)
        new_tab_index = self.ui.tabWidget.addTab(new_tab, f"{self.highest_tab_number}")
        self.ui.tabWidget.setCurrentIndex(new_tab_index)
    

    def close_tab(self, index=None):
        if self.ui.tabWidget.count() == 1:
            self.close()
        if not index:
            index = self.ui.tabWidget.currentIndex()

        tab_object = self.ui.tabWidget.widget(index)
        self.ui.tabWidget.removeTab(index)
        threading.Thread(target=lambda: self.delete_tab(tab_object), daemon=True).start()


    def delete_tab(self, tab_object):
        tab_object.cancel_progress = True
        while tab_object.thread_running:
            time.sleep(0.01)
        tab_object.deleteLater()
    

    def update_tab_status_indicators(self, index, pretty_tab_number, situation=None, progress=None):
        if situation:
            if progress and len(progress) == 2:
                progress_text = f" {progress[0]}/{progress[1]}"
            else:
                progress_text = ""
                
            situation_text = self.settings_manager.CONSTANT_SETTTINGS["tab_text"][situation]
            text = f"{pretty_tab_number} - {situation_text}{progress_text}"
            icon = self.settings_manager.CONSTANT_SETTTINGS["tab_icons"][situation]
        else:
            text = f"{pretty_tab_number}"
            icon = QIcon()
        
        self.ui.tabWidget.setTabText(index, text)
        self.ui.tabWidget.setTabIcon(index, icon)
    

    def switch_tab(self, index=None, move=None):
        if isinstance(index, int):
            self.ui.tabWidget.setCurrentIndex(index)
        elif move:
            current_index = self.ui.tabWidget.currentIndex()
            new_index = current_index
            if move == "left":
                new_index = current_index - 1
            elif move == "right":
                new_index = current_index + 1
            
            self.ui.tabWidget.setCurrentIndex(new_index)