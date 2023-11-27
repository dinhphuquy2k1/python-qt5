# messagebox.py
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap

def warning_messagebox(content):
    """
    Common messagebox function
    """
    app = QApplication.instance()
    if app is None:
        app = QApplication([])

    msgBox = QMessageBox()
    msgBox.setWindowIcon(QIcon("./static/icon/key-6-128.ico"))
    msgBox.setIconPixmap(QPixmap("./static/icon/exclamation-48.ico"))
    msgBox.setWindowTitle("Warning")
    msgBox.setText(content)
    msgBox.setStandardButtons(QMessageBox.Close)

    msgBox.exec_()
