# messagebox.py
from PyQt5.QtWidgets import QMessageBox, QPushButton, QWidget, QCalendarWidget, QVBoxLayout, QDialog, QComboBox
from PyQt5.QtGui import QIcon, QPixmap,  QStandardItemModel, QStandardItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, pyqtSignal, QTimer
import uuid
from src.enums.enums import *
import flet
from flet import *

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


# validate form input not empty
def validateEmpty(self, data: dict, messages: dict):
    result = []
    try:
        for key, value in data.items():
            label_name = f"error_{key}"
            label = getattr(self.ui, label_name, None)
            input_name = f"{key}_le"
            input_text = getattr(self.ui, input_name, None)
            if not value:
                message = messages[f"{key}Empty"]
                result.append(message)
                if label:
                    label.setText(message)
                    label.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
                if input_text:
                    input_text.setStyleSheet(Validate.BORDER_ERROR.value)
            else:
                if label:
                    label.setText("")
                if input_text:
                    input_text.setStyleSheet(Validate.BORDER_VALID.value)

    except Exception as E:
        print(E)
        return
    return result


# tạo view button xóa sửa trên row
def generate_action_row(row_id, model):
    horizontalLayout = QtWidgets.QHBoxLayout()
    horizontalLayout.setContentsMargins(0, 0, 0, 0)
    horizontalLayout.setSpacing(0)
    horizontalLayout_3 = QtWidgets.QHBoxLayout()
    spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    horizontalLayout_3.addItem(spacerItem)
    widget_2 = QtWidgets.QWidget()
    horizontalLayout_4 = QtWidgets.QHBoxLayout(widget_2)
    horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
    horizontalLayout_4.setSpacing(0)
    # button sửa
    pushButton = QPushButton(widget_2)
    pushButton.setMinimumSize(QtCore.QSize(36, 36))
    pushButton.setMaximumSize(QtCore.QSize(36, 36))
    pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    pushButton.setText("")
    icon = QtGui.QIcon("resources/icon/pen.svg")
    pushButton.setIcon(icon)
    pushButton.setIconSize(QtCore.QSize(24, 24))
    pushButton.setObjectName(f"row_edit_{model}_{row_id}")
    pushButton.setToolTip("Sửa")
    horizontalLayout_4.addWidget(pushButton)
    # button xóa
    pushButton_2 = QtWidgets.QPushButton(widget_2)
    pushButton_2.setMinimumSize(QtCore.QSize(36, 36))
    pushButton_2.setMaximumSize(QtCore.QSize(36, 36))
    pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    pushButton_2.setText("")
    pushButton_2.setToolTip("Xóa")
    icon1 = QtGui.QIcon("resources/icon/red-delete-10433.svg")
    pushButton_2.setIcon(icon1)
    pushButton_2.setIconSize(QtCore.QSize(24, 24))
    pushButton_2.setObjectName(f"row_delete_{model}_{row_id}")
    # # kết nối click button xóa với hàm xóa
    # pushButton_2.clicked.connect(
    #     lambda: selon_row_click(self.user_table, FormMode.DELETE, self.page_index["USER_PAGE_DETAIL"], FormMode.EDIT))
    horizontalLayout_4.addWidget(pushButton_2)
    horizontalLayout_3.addWidget(widget_2)
    horizontalLayout_3.addWidget(widget_2, 0, QtCore.Qt.AlignTop)
    spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    horizontalLayout_3.addItem(spacerItem1)
    horizontalLayout.addLayout(horizontalLayout_3)

    widget = QWidget()
    widget.setContentsMargins(0, 0, 0, 0)
    widget.setLayout(horizontalLayout)
    widget.setObjectName(f"row_{model}_{row_id}")
    return widget, pushButton, pushButton_2


class DateDialog(QDialog):
    date_selected = pyqtSignal(QDate)

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        self.calendar_widget = QCalendarWidget(self)
        self.calendar_widget.selectionChanged.connect(self.handle_date_selection)
        layout.addWidget(self.calendar_widget)

    def handle_date_selection(self):
        selected_date = self.calendar_widget.selectedDate()
        self.date_selected.emit(selected_date)
        # Ẩn QDialog khi người dùng chọn một ngày
        self.hide()


# tạo tên file duy nhất
def generate_unique_filename(file_name):
    unique_filename = f"{str(uuid.uuid4())}_{file_name}"
    return unique_filename
