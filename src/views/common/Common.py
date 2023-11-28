# messagebox.py
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon, QPixmap


def warningMessagebox(content):
    """
    Common messagebox function
    """
    msgbox = QMessageBox()
    msgbox.setWindowIcon(QIcon("./static/icon/key-6-128.ico"))
    msgbox.setIconPixmap(QPixmap("./static/icon/exclamation-48.ico"))
    msgbox.setWindowTitle("Warning")
    msgbox.setText(content)
    msgbox.setStandardButtons(QMessageBox.Close)

    msgbox.exec_()
