import os, time

from PyQt5.QtWidgets import QWidget, QDesktopWidget, QLineEdit, QLabel
from PyQt5.QtCore import Qt

from app.utils.constants import *
from app.utils.functions import get_installed_apps


class SearchWidget(QWidget):
    mode = RUN
    status = IDLE
    title = "Cerebelo"

    app = None
    widget_style = """
        background-color: #000;
    """

    textbox = None
    textbox_style = """
        color: white;
        font-size: 20px;
        padding: 0 20px;
    """

    error_label = None
    error_label_style = """
        color: red;
        font-size: 14px;
        background: #000;
    """

    def __init__(self, app):
        super(SearchWidget, self).__init__()
        self.app = app
        self.config_layout()
        self.add_components()
        self.show_application()

    def config_layout(self, width=WIDTH, height=HEIGHT):
        self.setWindowTitle(self.title)
        self.setFixedSize(width, height)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.setStyleSheet(self.widget_style)

    def show_application(self):
        screen_g = QDesktopWidget().screenGeometry()
        x_pos = int(screen_g.width() / 2) - WIDTH
        self.move(x_pos, Y_POS + HEIGHT)
        self.show()

    def add_components(self):
        self.textbox = QLineEdit(self)
        widget_g = self.geometry()
        widget_w = widget_g.width()
        widget_h = widget_g.height()
        self.textbox.resize(widget_w, widget_h)
        self.textbox.setStyleSheet(self.textbox_style)
        self.error_label = QLabel(self)
        self.error_label.setStyleSheet(self.error_label_style)
        self.error_label.resize(0, 0)

    def set_textbox_status(self, status):
        if status == ERROR:
            self.textbox_style = f"{self.textbox_style} border: 1px solid red;".replace(
                "color: white;", "color: red;"
            )
        else:
            self.textbox_style = self.textbox_style.replace(
                "border: 1px solid red;", ""
            ).replace("color: red;", "color: white;")

    def show_error(self, error):
        self.error_label.setText(error)
        self.error_label.resize(WIDTH - 30, 20)
        self.error_label.move(15, HEIGHT + 15)
        # self.set_textbox_status(ERROR)
        self.setFixedSize(WIDTH, HEIGHT + 50)
        self.textbox.setStyleSheet(self.textbox_style)

    def reset_error(self):
        self.error_label.setText("")
        self.error_label.move(0, 0)
        self.error_label.resize(0, 0)
        self.setFixedSize(WIDTH, HEIGHT)
        self.set_textbox_status(SUCCESS)
        self.textbox.setStyleSheet(self.textbox_style)

    def clear_input(self):
        self.textbox.setText("")

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.app.quit()
            event.accept()
        
        command = self.textbox.text()
        if event.key() in [Qt.Key_Return, Qt.Key_Enter]:
            if command in ["exit", "quit"]:
                self.app.quit()
            elif command in ["clear", "reset", "cls"]:
                self.reset_error()
                self.clear_input()
            else:
                if self.mode == RUN:
                    installed_apps = get_installed_apps()
                    for app in installed_apps:
                        if command in app:
                            os.system(f"{command} &")
                            self.app.quit()

                    self.clear_input()
                    self.show_error("App or command not found")
                    # TODO: Fix sleep to work correctly with reset_error
                    # time.sleep(3)
                    # self.reset_error()

        event.accept()
