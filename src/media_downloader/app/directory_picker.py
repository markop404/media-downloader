from pathlib import Path

from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QStandardPaths

class DirectoryPicker:
    def __init__(self, parent, on_select=None):
        self.parent = parent
        self.on_select = on_select
        self.update_paths()


    def open(self):
        self.update_paths(
            QFileDialog.getExistingDirectory(
                self.parent,
                caption="Choose a Folder",
                dir=self.path,
                options=QFileDialog.ShowDirsOnly
            )
        )


    def update_paths(self, path=QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)):
        if path:
            path = Path(path)
            self.path = str(path.resolve())
            
            if path.name:
                name = path.name
            else:
                name = self.path
            
            anchor = f"<a href=\"{path.as_uri()}\">{name}</a>"

            if self.on_select:
                self.on_select(self.path, anchor)