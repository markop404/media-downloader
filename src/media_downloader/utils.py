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


def update_combobox_items(combobox, items={}):
    combobox.clear()
    for data, value in items.items():
        combobox.addItem(value, data)
    combobox.setCurrentIndex(0)
