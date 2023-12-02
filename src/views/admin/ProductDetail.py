from PyQt5.QtWidgets import QWidget, QHBoxLayout, QMainWindow, QTableWidgetItem, QAbstractItemView, QApplication, \
    QPushButton
from PyQt5.QtCore import Qt, QPoint, pyqtSlot
from src.views.ui_generated.admin.product_detail import Ui_Form
from src.views.common.Common import *
from src.enums.enums import *
from src.views.common.Common import *
from src.controllers.admin.CategoryController import CategoryController
from src.models.category import Category


class ProductDetailWindow(QWidget):
    def __init__(self):
        super(ProductDetailWindow, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.category_controller = CategoryController()

    @pyqtSlot()
    def save_product(self, form_mode, product_id=None):
        product_name = self.ui.product_name_le.text().strip()
        product_code = self.ui.product_code_le.text().strip()

        color_style = "color: #ef5350;"
        border_style = "border: 1px solid #ef5350;"
        self.clear_form()

        messages = {
            'product_nameEmpty': "Vui lòng nhập tên sản phẩm.",
            'category_nameExit': "Tên loại sản phẩm đã tồn tại.",
        }

        # validate dữ liệu các cột không được trống
        is_valid = validateEmpty(self,{'product_name': product_name}, messages, color_style, border_style)

        if is_valid:
            return

        if form_mode == FormMode.ADD:
            if self.category_controller.checkExitsDataWithModel(Category.category_name, data=category_name):
                self.ui.error_category_name.setStyleSheet(color_style)
                self.ui.error_category_name.setText(messages["category_nameExit"])
                self.ui.category_name_le.setStyleSheet(border_style)
                return
            self.category_controller.insertData(Category(category_name=category_name))
        elif form_mode == FormMode.EDIT:
            if self.category_controller.checkExitsDataUpdateWithModel(Category.category_name, data=category_name, model_id=1):
                self.ui.error_category_name.setStyleSheet(color_style)
                self.ui.error_category_name.setText(messages["category_nameExit"])
                self.ui.category_name_le.setStyleSheet(border_style)
                return
            self.category_controller.updateDataWithModel(data={'category_name': category_name}, model_id=product_id)
        else:
            return

        return True

    # gán các giá trị lên form
    def handle_edit_event(self, category_id):
        category = self.category_controller.getDataByIdWithModel(category_id)
        if category:
            self.ui.category_name_le.setText(category.category_name)

    # clear dữ liệu trên form
    def clear_form(self):
        self.ui.product_name_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.product_code_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.product_image_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.combobox_category_id.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.price_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.quantity_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.manufacture_date_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.error_product_name.setText("")
        self.ui.error_product_code.setText("")
        self.ui.error_category.setText("")
        self.ui.error_product_image.setText("")
        self.ui.error_price.setText("")
        self.ui.error_quantity.setText("")
        self.ui.error_manufacture_date.setText("")
        self.ui.product_name_le.setText("")
        self.ui.product_image_le.setText("")
        # self.ui.combobox_category_i
        self.ui.price_le.setText("")
        self.ui.quantity_le.setValue(0)
        self.ui.manufacture_date_le.setText("")
        self.ui.description_le.setPlainText("")

