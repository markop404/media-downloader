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


from PySide6.QtCore import QEvent, QObject

class InvokeEvent(QEvent):
    def __init__(self, fn):
        QEvent.__init__(self, QEvent.Type(QEvent.registerEventType()))
        self.fn = fn


class Invoker(QObject):
    def event(self, event):
        event.fn()
        return True


def plain_text_to_set(text):
    lines = set()
    line = ""
    for char in text:
        if char == " " or char == "\t" or char == "\n" and line == "":
            continue
        elif char == "\n" and line != "":
            line.replace(" ", "")
            lines.add(line)
            line = ""
        else:
            line += char
    if line:
        lines.add(line)
    return lines


def list_to_plain_text(lines):
    text = ""
    lines = list(lines)
    for line in lines[:-1]:
        text += line + "\n"
    text += lines[-1]
    
    return text


def remove_lines(text, urls):   
    for url in urls:
        if url + "\n" in text:
            text = text.replace(url + "\n", "")
        elif url in text:
            text = text.replace(url, "")
    
    return text


def update_combobox_items(combobox, items=[]):
    combobox.clear()
    for item in items:
        combobox.addItem(item)
    combobox.setCurrentIndex(0)
