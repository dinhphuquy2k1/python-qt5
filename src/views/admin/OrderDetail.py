from PyQt5.QtWidgets import QWidget, QHBoxLayout, QMainWindow, QTableWidgetItem, QAbstractItemView, QApplication, \
    QCompleter
from PyQt5.QtCore import Qt, QPoint, pyqtSlot
from PyQt5.QtGui import QMouseEvent, QIcon, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from src.views.ui_generated.admin.order_detail import Ui_Form
from src.views.common.Common import *
from src.enums.enums import *
from src.views.common.Common import *
from src.controllers.admin.UserController import UserController
from src.controllers.admin.ProductController import ProductController
from src.models.category import Category
from src.views.common.form_group_btn_order import Test


class OrderDetailWindow(QWidget):
    def __init__(self):
        super(OrderDetailWindow, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # khởi tạo các ui
        self.search_box_product_order = self.ui.search_box_product_order
        self.search_box_product_order.lineEdit().setPlaceholderText("Tìm kiếm theo mã sản phẩm")
        self.user_le = self.ui.user_le
        self.user_le.lineEdit().setPlaceholderText("Tìm kiếm theo số điện thoại")
        self.table_product_order = self.ui.table_product_order

        # khởi tạo biến
        self.user_controller = UserController()
        self.product_controller = ProductController()
        # danh sách người dùng
        self.user_list = []
        # danh sách sản phẩm
        self.product_list = []
        self.user_selected = None
        # danh sách sản phẩm được chọn
        self.product_selected = []

        self.user_le.setInsertPolicy(QComboBox.NoInsert)
        self.user_le.completer().setCompletionMode(QCompleter.PopupCompletion)
        self.user_le.activated.connect(self.handle_user_le_selected)
        self.search_box_product_order.setInsertPolicy(QComboBox.NoInsert)
        self.search_box_product_order.completer().setCompletionMode(QCompleter.PopupCompletion)
        self.search_box_product_order.activated.connect(self.handle_product_le_selected)

    # Hàm luôn chạy khi form được show
    # Thực hiện lấy dữ liệu từ database
    def showEvent(self, event):
        # Lấy dữ liệu từ database
        self.user_list = self.user_controller.getDataByModel()
        self.product_list = self.product_controller.getDataByModel()
        # gắn dữ liệu lên combobox
        self.user_le.addItems([item.username for index, item in enumerate(self.user_list)])
        self.search_box_product_order.addItems([item.product_code for index, item in enumerate(self.product_list)])

    # Xử lý khi người dùng chọn người đặt hàng
    def handle_user_le_selected(self, index):
        print(self.user_list[index])

    # xử lý khi người dùng chọn sản phẩm
    def handle_product_le_selected(self, index):
        self.product_selected.insert(index, self.product_list[index])
        self.show_table_product()

    def show_table_product(self):
        self.table_product_order.setRowCount(0)
        if self.product_selected:
            try:
                for index, item in enumerate(self.product_selected):
                    print()
                    column_index = 0
                    self.table_product_order.setRowCount(index + 1)
                    self.table_product_order.setRowHeight(index, 120)
                    self.table_product_order.setItem(index, column_index, QTableWidgetItem(str(index + 1)))
                    widget = Test()
                    # self.table_product_order.setItem(index, column_index + 1, QTableWidgetItem(str(item.id)))
                    # self.table_product_order.setItem(index, column_index + 2, QTableWidgetItem(str(item.product_name)))
                    # widget, edit_btn, delete_btn = generate_action_row(item.id, "user")
                    # edit_btn.clicked.connect(
                    #     lambda: self.on_row_click(FormMode.EDIT.value,
                    #                               self.page_index["CATEGORY_PAGE_DETAIL"], self.category_widget_detail,
                    #                               self.page_index["CATEGORY_PAGE"], "category"))
                    # delete_btn.clicked.connect(
                    #     lambda: self.on_row_click(FormMode.DELETE.value,
                    #                               self.page_index["CATEGORY_PAGE_DETAIL"], self.category_widget_detail,
                    #                               self.page_index["CATEGORY_PAGE"], "category"))
                    self.table_product_order.setCellWidget(index, column_index + 1, widget)
            except Exception as E:
                print(f"{E} - OrderDetail.py")
                return

    def generate_group_order_btn(self):
        widget_container = QWidget()
        widget_container.setObjectName("Form_gourp_btn")
        widget_container.setStyleSheet("#order_group_btn{\n"
                                     "    border: 1px solid #e5e5e5;\n"
                                     "}\n"
                                     "\n"
                                     "#minus_order_btn, #plus_order_btn{\n"
                                     "    border: none;\n"
                                     "}\n"
                                     "\n"
                                     "#minus_order_btn{\n"
                                     "    border-right: 1px solid #e5e5e5;\n"
                                     "}\n"
                                     "\n"
                                     "#plus_order_btn{\n"
                                     "        border-left: 1px solid #e5e5e5;\n"
                                     "}")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.order_group_btn = QtWidgets.QWidget()
        self.order_group_btn.setMaximumSize(QtCore.QSize(100, 28))
        self.order_group_btn.setObjectName("order_group_btn")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.order_group_btn)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(self.order_group_btn)
        self.widget.setMinimumSize(QtCore.QSize(0, 28))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 28))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.minus_order_btn = QtWidgets.QPushButton(self.widget)
        self.minus_order_btn.setMinimumSize(QtCore.QSize(28, 28))
        self.minus_order_btn.setMaximumSize(QtCore.QSize(28, 28))
        self.minus_order_btn.setText("-")
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.minus_order_btn.setFont(font)
        self.minus_order_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minus_order_btn.setObjectName("minus_order_btn")
        self.horizontalLayout_2.addWidget(self.minus_order_btn)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(28, 28))
        self.label.setMaximumSize(QtCore.QSize(28, 28))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.plus_order_btn = QtWidgets.QPushButton(self.widget)
        self.plus_order_btn.setMinimumSize(QtCore.QSize(28, 28))
        self.plus_order_btn.setMaximumSize(QtCore.QSize(28, 28))
        self.plus_order_btn.setText("+")
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.plus_order_btn.setFont(font)
        self.plus_order_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plus_order_btn.setObjectName("plus_order_btn")
        self.horizontalLayout_2.addWidget(self.plus_order_btn)
        self.horizontalLayout_3.addWidget(self.widget)
        self.horizontalLayout.addWidget(self.order_group_btn, 0, QtCore.Qt.AlignTop)
        widget_container.setLayout(self.horizontalLayout)
        return widget_container


    def on_btn_save_order_clicked(self):
        print(self.combo_box_handler.selected_item)

    @pyqtSlot()
    def save_category(self, form_mode, order_id=None):
        # category_name = self.ui.category_name_le.text().strip()
        # color_style = "color: #ef5350;"
        # border_style = "border: 1px solid #ef5350;"
        # # sét border mặc định cho input
        # self.ui.category_name_le.setStyleSheet("border: 1px solid #e0e5e9;")
        # # xóa error text
        # self.ui.error_category_name.setText("")
        #
        # messages = {
        #     'category_nameEmpty': "Vui lòng nhập tên loại sản phẩm.",
        #     'category_nameExit': "Tên loại sản phẩm đã tồn tại.",
        # }
        #
        # # validate dữ liệu các cột không được trống
        # is_valid = validateEmpty(self,{'category_name': category_name}, messages)
        # if is_valid:
        #     return
        # try:
        #     if form_mode == FormMode.ADD.value:
        #         if self.category_controller.checkExitsDataWithModel(Category.category_name, data=category_name):
        #             self.ui.error_category_name.setStyleSheet(color_style)
        #             self.ui.error_category_name.setText(messages["category_nameExit"])
        #             self.ui.category_name_le.setStyleSheet(border_style)
        #             return
        #         self.category_controller.insertData(Category(category_name=category_name))
        #     elif form_mode == FormMode.EDIT.value:
        #         if self.category_controller.checkExitsDataUpdateWithModel(Category.category_name, data=category_name, model_id=order_id):
        #             self.ui.error_category_name.setStyleSheet(color_style)
        #             self.ui.error_category_name.setText(messages["category_nameExit"])
        #             self.ui.category_name_le.setStyleSheet(border_style)
        #             return
        #         self.category_controller.updateDataWithModel(data={'category_name': category_name}, model_id=order_id)
        #     else:
        #         return
        # except Exception as E:
        #     print(E)
        #     return

        return True

    # gán các giá trị lên form
    def handle_edit_event(self, category_id):
        category = self.category_controller.getDataByIdWithModel(category_id)
        # if category:
        #     self.ui.category_name_le.setText(category.category_name)

    # clear dữ liệu trên form
    def clear_form(self):
        self.ui.order_code_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.order_code_le.setText("")
        self.ui.user_le.setText("")
