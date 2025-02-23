# Media Downloader - Web video/audio downloader
# Copyright (C) 2024-2025  Marko Pejić

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


from PySide6.QtCore import QEvent, QObject


class InvokeEvent(QEvent):
    def __init__(self, fn):
        QEvent.__init__(self, QEvent.Type(QEvent.registerEventType()))
        self.fn = fn


class Invoker(QObject):
    def event(self, event):
        event.fn()
        return True


def get_value_if_exists(value, _dict, _type=None):
    if value in _dict:
        value = _dict[value]
        if _type and isinstance(value, _type):
            return value
        elif not _type:
            return value