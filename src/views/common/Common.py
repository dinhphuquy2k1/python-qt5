# messagebox.py
from PyQt5.QtWidgets import QMessageBox, QPushButton, QWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets


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
def validateEmpty(self, data: dict, messages: dict, color_style, border_style):
    result = []
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
                label.setStyleSheet(color_style)
            if input_text:
                input_text.setStyleSheet(border_style)
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
