from PySide6.QtWidgets import QDialog
from ..ui import Ui_KeyboardShortcutsDialog

class KeyboardShortcutsDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_KeyboardShortcutsDialog()
        self.ui.setupUi(self)
        self.ui.closeDialogButton.clicked.connect(self.close)
