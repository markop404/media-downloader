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


from time import sleep
from concurrent.futures import ThreadPoolExecutor

from PySide6.QtCore import QSettings, QByteArray
from PySide6.QtWidgets import QMainWindow, QWidget, QMenu
from PySide6.QtGui import QIcon, QKeySequence, QShortcut

from src import ui
from src import main

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.connect_signals_and_slots()
        
        self.settings = QSettings()
        self.executor = ThreadPoolExecutor()
        self.highest_tab_number = 0
        self.popup_window_running = False
        
        self.create_new_tab()
        self.read_settings()
    

    def read_settings(self):
        self.settings.beginGroup("MainWindow")
        geometry = self.settings.value("geometry", QByteArray())
        if not geometry.isEmpty():
            self.restoreGeometry(geometry)
        self.settings.endGroup()
    

    def write_settings(self):
        self.settings.beginGroup("MainWindow")
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.endGroup()
    

    def closeEvent(self, event):
        for i in range(self.ui.tabWidget.count()):
            self.ui.tabWidget.widget(i).destroy()
        self.executor.shutdown(wait=False)
        self.write_settings()
        event.accept()


    def setup_ui(self):
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.about_dialog = main.AboutDialog(self)
        self.keyboard_shortcuts_dialog = main.KeyboardShortcutsDialog(self)

        self.tab_button_layout = QWidget()
        self.tab_buttons = ui.Ui_TabButtons()
        self.tab_buttons.setupUi(self.tab_button_layout)
        
        self.main_menu = QMenu()
        self.main_menu.addAction(self.ui.actionKeyboardShortcuts)
        self.main_menu.addAction(self.ui.actionAbout)
        self.tab_buttons.menuButton.setMenu(self.main_menu)

        self.ui.tabWidget.setCornerWidget(self.tab_button_layout)
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)

        for i in range(1, 10):
            QShortcut(QKeySequence(f"Alt+{i}"), self).activated.connect(lambda i=i: self.switch_tab(i - 1))
        QShortcut(QKeySequence("Alt+0"), self).activated.connect(lambda: self.switch_tab(9))
        QShortcut(QKeySequence("Ctrl+PgUp"), self).activated.connect(lambda: self.switch_tab(move="left"))
        QShortcut(QKeySequence("Ctrl+PgDown"), self).activated.connect(lambda: self.switch_tab(move="right"))
        QShortcut(QKeySequence("Ctrl+w"), self).activated.connect(self.close_tab)


    def connect_signals_and_slots(self):
        self.ui.actionAbout.triggered.connect(self.about_dialog.exec)
        self.ui.actionKeyboardShortcuts.triggered.connect(self.keyboard_shortcuts_dialog.exec)
        self.tab_buttons.newTabButton.clicked.connect(self.create_new_tab)
    

    def create_new_tab(self):
        self.highest_tab_number += 1
        new_tab = main.Tab(self, self.highest_tab_number)
        new_tab_index = self.ui.tabWidget.addTab(new_tab, f"{self.highest_tab_number}")
        self.ui.tabWidget.setCurrentIndex(new_tab_index)
    

    def close_tab(self, index=None):
        if self.ui.tabWidget.count() == 1:
            self.close()
        if not index:
            index = self.ui.tabWidget.currentIndex()
        tab_object = self.ui.tabWidget.widget(index)
        
        tab_object.destroy()
        self.ui.tabWidget.removeTab(index)
        tab_object.deleteLater()
    

    def update_tab(self, index, pretty_tab_number, situation=None, progress=None):
        if situation:
            if progress and len(progress) == 2:
                progress_text = f" {progress[0]}/{progress[1]}"
            else:
                progress_text = ""

            text = f"{pretty_tab_number} - {main.Config.TAB_TEXT[situation]}{progress_text}"
            self.ui.tabWidget.setTabText(index, text)
            self.ui.tabWidget.setTabIcon(index, main.Config.STATUS_LABEL_ICONS[situation])
        else:
            self.ui.tabWidget.setTabText(index, f"{pretty_tab_number}")
            self.ui.tabWidget.setTabIcon(index, QIcon())
    

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
