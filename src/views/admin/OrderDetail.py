from PyQt5.QtWidgets import QWidget, QHBoxLayout, QMainWindow, QTableWidgetItem, QAbstractItemView, QApplication, \
    QCompleter, QComboBox
from PyQt5.QtCore import QLocale, pyqtSlot
from src.views.ui_generated.admin.order_detail import Ui_Form
from src.views.common.Common import *
from src.enums.enums import *
from src.views.common.Common import *
from src.controllers.admin.UserController import UserController
from src.controllers.admin.ProductController import ProductController
from src.controllers.admin.OrderController import OrderController
from src.controllers.admin.OrderDetailController import OrderDetailController
from src.models.orders import Order
from src.models.order_details import OrderDetail
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
        self.table_product_order.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.total_quantity_product_order = self.ui.total_quantity_product_order
        self.table_info_user = self.ui.table_info_user
        self.table_info_user.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # khởi tạo biến
        self.user_controller = UserController()
        self.product_controller = ProductController()
        self.order_controller = OrderController()
        self.order_detail_controller = OrderDetailController()
        # danh sách người dùng
        self.user_list = []
        # danh sách sản phẩm
        self.product_list = []
        self.user_selected = None
        # danh sách sản phẩm được chọn
        self.product_selected = {}
        # người đặt hàng
        self.user_selected = None
        # tổng tiền các sản phẩm
        self.total_price = 0
        # số lượng sản phẩm đặt hàng
        self.total_quantity_order = 0
        self.mode = FormMode.ADD.value
        self.order_selected = None
        self.delete_product_order_detail = []
        self.insert_product_order_detail = []
        self.update_product_order_detail = []
        self.order_detail_ids = []

        self.user_le.setInsertPolicy(QComboBox.NoInsert)
        self.user_le.completer().setCompletionMode(QCompleter.PopupCompletion)
        self.user_le.completer().setCaseSensitivity(0)
        self.user_le.activated.connect(self.handle_user_le_selected)
        self.search_box_product_order.setInsertPolicy(QComboBox.NoInsert)
        self.search_box_product_order.completer().setCompletionMode(QCompleter.PopupCompletion)
        self.search_box_product_order.completer().setCaseSensitivity(0)
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
        self.user_selected = None
        self.user_selected = self.user_list[index]
        self.show_table_user()

    def show_table_user(self):
        self.table_info_user.setRowCount(1)
        self.table_info_user.setRowHeight(0, 32)
        self.table_info_user.setItem(0, 0, QTableWidgetItem(str(self.user_selected.name)))
        self.table_info_user.setItem(0, 1, QTableWidgetItem(str(self.user_selected.username)))


    # Xử lý tính tổng tiền đơn hàng
    def handle_total_quantity_product_order(self):
        self.total_price = sum(int(product.total_price) for product in self.product_selected.values())
        self.total_quantity_order = sum(int(product.quantity_order) for product in self.product_selected.values())
        self.total_quantity_product_order.setText(formatCurrency(int(self.total_price), 'đ'))

    # xử lý khi người dùng chọn sản phẩm
    def handle_product_le_selected(self, index):
        selected_item = self.product_list[index]

        try:
            if selected_item.id not in self.product_selected:
                selected_item.quantity_order = 1
                selected_item.total_price = selected_item.price * selected_item.quantity_order
                self.product_selected[selected_item.id] = selected_item
        except Exception as E:
            print(f"{E}- file OrderDetail.py function handle_product_le_selected")
            return
        self.handle_total_quantity_product_order()
        self.show_table_product()

    def generate_group_order_btn(self, row, total_quantity, label_price):
        widget = QtWidgets.QWidget()
        widget.setContentsMargins(0, 0, 0, 0)
        widget.setStyleSheet("#order_group_btn{\n"
                             "    border: 1px solid #e5e5e5;\n"
                             "    border-left: 0;\n"
                             "    border-right: 0;\n"
                             "}\n"
                             "\n"
                             "#group_order_btn QPushButton{\n"
                             "    min-width: 7px;\n"
                             "    max-width: 7px;\n"
                             "    width: 7x;\n"
                             "    min-height: 22px;\n"
                             "    max-height: 22px;\n"
                             "    border: none;\n"
                             "    text-align: center;\n"
                             "    border-left: 1px solid #e5e5e5;\n"
                             "    border-right: 1px solid #e5e5e5;\n"
                             "    border-radius: 0;\n"
                             "}\n"
                             "#group_order_btn QSpinBox{\n"
                             "    border-radius: 0;\n"
                             "    background: transparent;\n"
                             "    max-width: 35px;\n"
                             "    min-width: 35px;\n"
                             "    width: 35px;\n"
                             "    padding: 0;\n"
                             "    margin: 0;\n"
                             "    min-height: 0px;\n"
                             "    max-height: 0px;\n"
                             "    height: 28px;\n"
                             "    border: none;\n"
                             "    color: #222;\n"
                             "    font-size: 13px;\n"
                             "}\n")
        widget.setObjectName("group_order_btn")
        horizontalLayout_2 = QtWidgets.QHBoxLayout(widget)
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_2.setSpacing(0)
        order_group_btn = QtWidgets.QWidget(widget)
        order_group_btn.setMinimumSize(QtCore.QSize(0, 28))
        order_group_btn.setMaximumSize(QtCore.QSize(100, 28))
        order_group_btn.setObjectName("order_group_btn")
        horizontalLayout_3 = QtWidgets.QHBoxLayout(order_group_btn)
        horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_3.setSpacing(0)
        horizontalLayout_3.setObjectName("horizontalLayout_3")
        horizontalLayout = QtWidgets.QHBoxLayout()
        horizontalLayout.setSpacing(0)
        horizontalLayout.setObjectName("horizontalLayout")
        minus_order_btn = QtWidgets.QPushButton(order_group_btn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(minus_order_btn.sizePolicy().hasHeightForWidth())
        minus_order_btn.setSizePolicy(sizePolicy)
        minus_order_btn.setMinimumSize(QtCore.QSize(29, 28))
        minus_order_btn.setMaximumSize(QtCore.QSize(28, 28))
        minus_order_btn.setText("-")
        minus_order_btn.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        minus_order_btn.setObjectName(f"minus_order_btn_{row}")
        horizontalLayout.addWidget(minus_order_btn)
        quantity_order = QtWidgets.QSpinBox(order_group_btn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(quantity_order.sizePolicy().hasHeightForWidth())
        quantity_order.setSizePolicy(sizePolicy)
        quantity_order.setMinimumSize(QtCore.QSize(35, 0))
        quantity_order.setMaximumSize(QtCore.QSize(35, 20))
        quantity_order.setLayoutDirection(Qt.LeftToRight)
        quantity_order.setFrame(False)
        quantity_order.setAlignment(Qt.AlignCenter)
        quantity_order.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        quantity_order.setObjectName(f"quantity_order_{row}")
        quantity_order.setMinimum(1)
        quantity_order.setValue(total_quantity)
        quantity_order.setMaximum(10)
        horizontalLayout.addWidget(quantity_order, 0, Qt.AlignTop)
        plus_order_btn = QtWidgets.QPushButton(order_group_btn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(plus_order_btn.sizePolicy().hasHeightForWidth())
        plus_order_btn.setSizePolicy(sizePolicy)
        plus_order_btn.setMinimumSize(QtCore.QSize(29, 28))
        plus_order_btn.setMaximumSize(QtCore.QSize(28, 28))
        plus_order_btn.setText("+")
        plus_order_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        plus_order_btn.setObjectName(f"plus_order_btn_{row}")
        horizontalLayout.addWidget(plus_order_btn)
        horizontalLayout_3.addLayout(horizontalLayout)
        horizontalLayout_2.addWidget(order_group_btn)
        minus_order_btn.clicked.connect(
            lambda: self.decreaseQuantity(quantity_order, label_price)
        )
        plus_order_btn.clicked.connect(
            lambda: self.increaseQuantity(quantity_order, label_price)
        )
        return widget, minus_order_btn, plus_order_btn, quantity_order

    # Hiển thị các sản phẩm được chọn
    def show_table_product(self):
        self.table_product_order.setRowCount(0)
        if self.product_selected:
            try:
                row_index = 0
                for index, item in self.product_selected.items():
                    column_index = 0
                    self.table_product_order.setRowCount(row_index + 1)
                    self.table_product_order.setRowHeight(row_index, 120)
                    # cột sản phẩm
                    self.table_product_order.setCellWidget(row_index, column_index, self.generate_info_product_order(item))
                    self.table_product_order.setColumnWidth(column_index, 200)
                    # cột đơn giá
                    self.table_product_order.setItem(row_index, column_index + 1, QTableWidgetItem(formatCurrency(int(item.price), 'đ')))

                    widget_price, label_price = self.generate_column_price(row_index, item) # tạo view cột thành tiền
                    widget,  minus_order_btn, plus_order_btn, quantity_label = self.generate_group_order_btn(item.id, item.quantity_order, label_price) # tạo view group button
                    # cột số lượng
                    self.table_product_order.setCellWidget(row_index, column_index + 2, widget)
                    # cột thành tiền
                    self.table_product_order.setCellWidget(row_index, column_index + 3, widget_price)
                    row_index += 1

            except Exception as E:
                print(f"{E} - file OrderDetail.py")
                return

    # sự kiện click button giảm số lượng sản phẩm
    def decreaseQuantity(self, quantity_label, label_price):
        try:
            # lấy data
            button = self.sender()
            # quantity_label.maximum()
            index = int(button.objectName().strip().rsplit('_', 1)[-1])
            # cập nhật cột thành tiền
            if quantity_label.value() > quantity_label.minimum():
                self.product_selected[index].quantity_order -= 1
                self.product_selected[index].total_price = int(self.product_selected[index].quantity_order) * int(
                    self.product_selected[index].price)
                label_price.setText(formatCurrency(self.product_selected[index].total_price, 'đ'))
                quantity_label.setValue(int(self.product_selected[index].quantity_order))
            self.handle_total_quantity_product_order()
        except Exception as E:
            print(f"{E} - file OrderDetail.py")
            return

    # tăng số lượng sản phẩm
    def increaseQuantity(self, quantity_label, label_price):
        try:
            # lấy data
            button = self.sender()
            # quantity_label.maximum()
            index = int(button.objectName().strip().rsplit('_', 1)[-1])
            # cập nhật cột thành tiền
            if quantity_label.value() < quantity_label.maximum():
                self.product_selected[index].quantity_order += 1
                self.product_selected[index].total_price = int(self.product_selected[index].quantity_order) * int(self.product_selected[index].price)
                label_price.setText(formatCurrency(self.product_selected[index].total_price, 'đ'))
                quantity_label.setValue(int(self.product_selected[index].quantity_order))
            self.handle_total_quantity_product_order()
        except Exception as E:
            print(f"{E} - file OrderDetail.py")
            return

    # tạo view cột thành tiền
    def generate_column_price(self, row, data):
        self.label = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # sét giá trị cột thành tiền
        self.label.setText(formatCurrency(int(data.quantity_order) * int(data.price),
                           'đ'))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName(f"label_price_{row}")
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.setAlignment(Qt.AlignHCenter | Qt.AlignLeft)
        layout.setContentsMargins(0, 0, 0, 0)
        widget = QWidget()
        widget.setLayout(layout)
        return widget, self.label

    # tạo view cột thông tin sản phẩm
    def generate_info_product_order(self, data):
        self.widget = QtWidgets.QWidget()
        self.widget.setMinimumSize(QtCore.QSize(0, 100))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 110))
        self.widget.setStyleSheet("#info_product_order QPushButton{\n"
                                  "    max-width: 30px;\n"
                                  "    min-width: 30px;\n"
                                  "    width: 30px;\n"
                                  "    height: 18px;\n"
                                  "    min-height: 18px;\n"
                                  "    text-align: left;\n"
                                  "    border: none;\n"
                                  "    padding: 0;\n"
                                  "    color: #46694f;\n"
                                  "    background: transparent;\n"
                                  "}\n"
                                  "\n"
                                  "#delete_order_product:hover, #product_name_order:hover{\n"
                                  "    color: #80b885;\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "")
        self.widget.setObjectName("info_product_order")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(80, 80))
        self.label.setMaximumSize(QtCore.QSize(80, 80))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        image_url = None
        if data.product_image:
            image_url = data.product_image[0].image_url
        self.label.setPixmap(QPixmap(image_url))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.group_info_order = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_info_order.sizePolicy().hasHeightForWidth())
        self.group_info_order.setSizePolicy(sizePolicy)
        self.group_info_order.setMaximumSize(QtCore.QSize(16777215, 110))
        self.group_info_order.setObjectName("group_info_order")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.group_info_order)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.setSpacing(10)
        self.product_name_order = QtWidgets.QLabel(self.group_info_order)
        self.product_name_order.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.product_name_order.setWordWrap(True)
        self.product_name_order.setText(data.product_name)
        self.product_name_order.setObjectName("product_name_order")
        self.verticalLayout_2.addWidget(self.product_name_order)
        self.product_code_order = QtWidgets.QLabel(self.group_info_order)
        self.product_code_order.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.product_code_order.setText(data.product_code)
        self.product_code_order.setObjectName("product_code_order")
        self.verticalLayout_2.addWidget(self.product_code_order)
        self.delete_order_product = QtWidgets.QPushButton(self.group_info_order)
        self.delete_order_product.setMinimumSize(QtCore.QSize(30, 20))
        self.delete_order_product.setMaximumSize(QtCore.QSize(30, 20))
        self.delete_order_product.setText("Xóa")
        self.delete_order_product.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_order_product.setObjectName(f"delete_order_product_{data.id}")
        self.delete_order_product.clicked.connect(self.delete_product_order_detail)
        self.verticalLayout_2.addWidget(self.delete_order_product)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6.addWidget(self.group_info_order)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)
        return self.widget

    # xóa sản phẩm đã chọn
    def on_delete_product_order_detail(self):
        button = self.sender()
        row_id = int(button.objectName().strip().rsplit('_', 1)[-1])
        order_detail_delete = self.product_selected.pop(row_id, None)
        self.handle_total_quantity_product_order()
        if self.mode == FormMode.EDIT.value:
            self.delete_product_order_detail.append(order_detail_delete.order_detail_id)
        self.show_table_product()

    @pyqtSlot()
    def save_order(self, form_mode, order_id=None):
        order_code = self.ui.order_code_le.text().strip()
        price = self.total_price
        self.clear_error()
        messages = {
            'order_codeEmpty': "Vui lòng nhập mã đơn hàng",
            'order_codeExit': "Mã đơn hàng đã tồn tại",
            'userEmpty': "Vui lòng chọn người đặt hàng",
            'productEmpty': "Vui lòng chọn sản phẩm đặt hàng",
        }

        # validate dữ liệu các cột không được trống
        is_valid = validateEmpty(self,{'order_code': order_code, 'user': self.user_selected, 'product': self.product_selected}, messages)
        order = Order(order_code=order_code, user_id=self.user_selected.id, price=self.total_price, quantity=self.total_quantity_order, status=OrderStatus.PROGRESS.value)
        for index, item in self.product_selected.items():
            order.order_details.append(OrderDetail(total_price=item.total_price, quantity_order=item.quantity_order, product_id=item.id))
        if is_valid:
            return
        try:
            if form_mode == FormMode.ADD.value:

                if self.order_controller.checkExitsDataWithModel(Order.order_code, data=order_code):
                    self.ui.error_order_code.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
                    self.ui.error_order_code.setText(messages["order_codeExit"])
                    self.ui.order_code_le.setStyleSheet(Validate.BORDER_ERROR.value)
                    return
                self.order_controller.insertData(order)
            elif form_mode == FormMode.EDIT.value:
                if self.order_controller.checkExitsDataUpdateWithModel(Order.order_code, data=order_code, model_id=order_id):
                    self.ui.error_order_code.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
                    self.ui.error_order_code.setText(messages["order_codeExit"])
                    self.ui.order_code_le.setStyleSheet(Validate.BORDER_ERROR.value)
                    return
                # xóa các product
                if self.delete_product_order_detail:
                    self.order_detail_controller.deleteDataMutipleWithModel(self.delete_product_order_detail)
                self.order_controller.updateDataWithModel({'order_code': order_code, 'user_id': self.user_selected.id, 'price': self.total_price, 'quantity': self.total_quantity_order, 'status': OrderStatus.PROGRESS.value}, model_id=order_id)
                # self.category_controller.updateDataWithModel(data={'category_name': category_name}, model_id=order_id)
            else:
                return
        except Exception as E:
            print(E)
            return

        return True

    # gán các giá trị lên form
    def handle_edit_event(self, order_id):
        self.mode = FormMode.EDIT.value
        self.order_selected = self.order_controller.getDataByModelIdWithRelation(order_id)
        if self.order_selected:
            self.ui.order_code_le.setText(self.order_selected.order_code)
            self.user_selected = self.order_selected.user
            for index, item in enumerate(self.order_selected.order_details):
                self.order_detail_ids.append(item.id)
                self.product_selected[item.product.id] = item
                self.product_selected[item.product.id].order_detail_id = item.id
                self.product_selected[item.product.id].id = item.product.id
                self.product_selected[item.product.id].product_image = item.product.product_image
                self.product_selected[item.product.id].product_name = item.product.product_name
                self.product_selected[item.product.id].product_code = item.product.product_code
                self.product_selected[item.product.id].price = item.product.price
            self.handle_total_quantity_product_order()
            self.show_table_product()
            self.show_table_user()

    # clear dữ liệu trên form
    def clear_form(self):
        self.clear_error()
        self.ui.user_le.setCurrentIndex(-1)
        self.ui.search_box_product_order.setCurrentIndex(-1)
        self.ui.search_box_product_order.setStyleSheet(Validate.BORDER_VALID.value)
        self.ui.total_quantity_product_order.setText("0đ")
        self.ui.status_order.setCurrentIndex(1)
        self.ui.table_product_order.setRowCount(0)
        self.ui.table_info_user.setRowCount(0)

    # clear lỗi
    def clear_error(self):
        self.ui.order_code_le.setStyleSheet(Validate.BORDER_VALID.value)
        self.ui.user_le.setStyleSheet(Validate.BORDER_VALID.value)
        self.ui.error_user.setText("")
        self.ui.error_product.setText("")

