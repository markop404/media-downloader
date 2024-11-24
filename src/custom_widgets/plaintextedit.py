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


from PySide6.QtWidgets import QPlainTextEdit


class PlainTextEdit(QPlainTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setting_text = False


    def cleanup(self):
        text = self.toPlainText()
        lines = ""
        line = ""

        for char in text:
            if line == "" and (char == " " or char == "\t" or char == "\n"):
                continue
            elif line != "" and char == "\n":
                line.replace(" ", "")
                lines += line + "\n"
                line = ""
            else:
                line += char
        if line:
            lines += line + "\n"
        
        self.set_text(lines)
    

    def get_lines():
        text = self.toPlainText()
        lines = set()
        line = ""

        for char in text:
            if line == "" and (char == " " or char == "\t" or char == "\n"):
                continue
            elif line != "" and char == "\n":
                line.replace(" ", "")
                lines.add(line)
                line = ""
            else:
                line += char
        if line:
            lines.add(line)
        
        return lines


    def remove_lines(lines):
        text = self.toPlainText()

        for line in lines:
            if line + "\n" in text:
                text = text.replace(url + "\n", "")
            elif line in text:
                text = text.replace(url, "")
        
        self.set_text(text)


    def set_text(self, text=""):
        self.setting_text = True
        self.setPlainText(text)
        self.setting_text = False


    def set_text_by_lines(lines):
        text = ""
        for line in lines:
            text += line + "\n"
        
        self.set_text(lines)