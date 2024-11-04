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


from PySide6.QtWidgets import QSlider

class Toggle(QSlider):
    def __init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sliderPressed.connect(self.record_value)
        self.sliderReleased.connect(self.change_value)
        self.sliderMoved.connect(self.record_movement)

        self.slider_moved = False
        self.current_value = None

 
    def record_value(self):
        self.current_value = self.value()


    def record_movement(self):
        self.slider_moved = True


    def change_value(self):
        if self.current_value == self.value() and not self.slider_moved:
            self.setValue(not self.current_value)

        self.slider_moved = False