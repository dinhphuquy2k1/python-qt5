from PyQt5.QtWidgets import QWidget, QHBoxLayout, QMainWindow, QTableWidgetItem, QAbstractItemView, QApplication, \
    QPushButton
from PyQt5.QtCore import Qt, QPoint, pyqtSlot
from PyQt5.QtGui import QMouseEvent, QIcon, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from src.views.ui_generated.admin.category_detail import Ui_Form
from src.views.common.Common import *
from src.enums.enums import *
from src.views.common.Common import *
from src.controllers.admin.CategoryController import CategoryController
from src.models.category import Category

class CategoryDetailWindow(QWidget):
    def __init__(self, form_mode):
        super(CategoryDetailWindow, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.category_controller = CategoryController()
        self.mode = form_mode

    @pyqtSlot()
    def save_category(self):
        return True
        category_name = self.ui.category_name_le.text().strip()
        color_style = "color: #ef5350;"
        border_style = "border: 1px solid #ef5350;"
        # sét border mặc định cho input
        self.ui.category_name_le.setStyleSheet("border: 1px solid #e0e5e9;")
        # xóa error text
        self.ui.error_category_name.setText("")

        messages = {
            'category_nameEmpty': "Vui lòng nhập tên loại sản phẩm.",
            'category_nameExit': "Tên loại sản phẩm đã tồn tại.",
        }

        # validate dữ liệu các cột không được trống
        is_valid = validateEmpty(self,{'category_name': category_name}, messages, color_style, border_style)

        if is_valid:
            return

        if self.mode == FormMode.ADD:
            if self.category_controller.checkExitsDataWithModel(Category.category_name, data=category_name):
                self.ui.error_category_name.setStyleSheet(color_style)
                self.ui.error_category_name.setText(messages["category_nameExit"])
                self.ui.category_name_le.setStyleSheet(border_style)
                return
            self.category_controller.insertData(Category(category_name=category_name))
        elif self.mode == FormMode.EDIT:
            if self.category_controller.checkExitsDataUpdateWithModel(Category.category_name, data=category_name, model_id=1):
                self.ui.error_category_name.setStyleSheet(color_style)
                self.ui.error_category_name.setText(messages["usernameExit"])
                self.ui.category_name_le.setStyleSheet(border_style)
                return
            self.category_controller.updateUserWithModel(data=Category(category_name=category_name), user_id=self.id_data_selected)
        else:
            return

        return True
        # # quay về trang danh sách
        # self.pages.setCurrentIndex(self.page_index["USER_PAGE"])
        # # load lại dữ liệu
        # self.show_user_table()
