from PyQt5.QtWidgets import QWidget, QHBoxLayout, QMainWindow, QTableWidgetItem, QAbstractItemView, QApplication, \
    QCompleter, QComboBox
from PyQt5.QtCore import QLocale, pyqtSlot
from src.views.ui_generated.admin.supplier_detail import Ui_Form
from src.views.common.Common import *
from src.enums.enums import *
from src.views.common.Common import *
from src.controllers.admin.UserController import UserController
from src.controllers.admin.SupplierController import SupplierController
from src.models.suppliers import Supplier
from src.views.common.form_group_btn_order import Test


class SupplierDetailWindow(QWidget):
    def __init__(self):
        super(SupplierDetailWindow, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # # khởi tạo các ui
        # self.search_box_product_order = self.ui.search_box_product_order
        # self.search_box_product_order.lineEdit().setPlaceholderText("Tìm kiếm theo mã sản phẩm")
        # self.user_le = self.ui.user_le
        # self.user_le.lineEdit().setPlaceholderText("Tìm kiếm theo số điện thoại")
        # self.table_product_order = self.ui.table_product_order
        # self.table_product_order.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.total_quantity_product_order = self.ui.total_quantity_product_order
        # self.table_info_user = self.ui.table_info_user
        # self.table_info_user.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # # khởi tạo biến
        # self.customer_controller = CustomerController()
        self.supplier_controller = SupplierController()
        self.user_controller = UserController()
        # self.member_rank_controller = MemberRankController()
        # self.order_detail_controller = OrderDetailController()
        # # danh sách người dùng
        # self.customer_list = []
        # # danh sách sản phẩm
        # self.product_list = []
        # # danh sách sản phẩm được chọn
        # self.product_selected = {}
        # # người đặt hàng
        # self.customer_selected = None
        # # tổng tiền các sản phẩm
        # self.total_price = 0
        # # tổng tiền sau khuyến mãi
        # self.final_price = 0
        # # số lượng sản phẩm đặt hàng
        # self.total_quantity_order = 0
        # self.mode = FormMode.ADD.value
        # self.order_selected = None
        # self.order_details = []
        # self.product_update = {}
        # # giảm giá
        # self.discount = 0
        #
        # self.user_le.setInsertPolicy(QComboBox.NoInsert)
        # self.user_le.completer().setCompletionMode(QCompleter.PopupCompletion)
        # self.user_le.completer().setCaseSensitivity(0)
        # self.user_le.activated.connect(self.handle_user_le_selected)
        # self.search_box_product_order.setInsertPolicy(QComboBox.NoInsert)
        # self.search_box_product_order.completer().setCompletionMode(QCompleter.PopupCompletion)
        # self.search_box_product_order.completer().setCaseSensitivity(0)
        # self.search_box_product_order.activated.connect(self.handle_product_le_selected)

    @pyqtSlot()
    def save_supplier(self, form_mode, order_id=None):
        code = self.ui.code_le.text().strip()
        name = self.ui.name_le.text().strip()
        phone = self.ui.phone_le.text().strip()
        address = self.ui.address_le.text().strip()
        self.clear_error()
        messages = {
            'codeEmpty': "Vui lòng nhập mã đơn vị cung cấp",
            'codeExit': "Mã đơn vị cung cấp đã tồn tại",
            'nameEmpty': "Vui lòng nhập tên đơn vị cung cấp",
            'phoneValid': "Số điện thoại không đúng định dạng",
        }

        # validate dữ liệu các cột không được trống
        is_valid = validateEmpty(self, {'code': code, 'name': name}, messages)

        if phone:
            if not self.user_controller.isValidPhoneNumber(phone):
                self.ui.error_phone.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
                self.ui.error_phone.setText(messages["phoneValid"])
                self.ui.phone_le.setStyleSheet(Validate.BORDER_ERROR.value)
                return
        if is_valid:
            return

        supplier = Supplier(code=code, name=name, phone=phone, address=address)

        try:
            if form_mode == FormMode.ADD.value:
                if self.supplier_controller.checkExitsDataWithModel(Supplier.code, data=code):
                    self.ui.error_code.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
                    self.ui.error_code.setText(messages["codeExit"])
                    self.ui.code_le.setStyleSheet(Validate.BORDER_ERROR.value)
                    return
                self.supplier_controller.insertData(supplier)
            elif form_mode == FormMode.EDIT.value:
                del order.order_details
                order.id = order_id
                if self.order_controller.checkExitsDataUpdateWithModel(Order.order_code, data=order_code,
                                                                       model_id=order_id):
                    self.ui.error_order_code.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
                    self.ui.error_order_code.setText(messages["order_codeExit"])
                    self.ui.order_code_le.setStyleSheet(Validate.BORDER_ERROR.value)
                    return
                self.order_controller.updateDataWithModelRelation(
                    order,
                    {
                        'order_details': self.order_details,
                    },
                    [
                        {
                            'action': FormMode.EDIT.value,
                            'data': self.product_update,
                        },
                        {
                            'action': FormMode.EDIT.value,
                            'data': customer,
                        },
                    ]
                )

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
            self.customer_selected = self.order_selected.customer
            for index, item in enumerate(self.order_selected.order_details):
                self.product_selected[item.product.id] = item
                self.product_selected[item.product.id].order_detail_id = item.id
                self.product_selected[item.product.id].id = item.product.id
                self.product_selected[item.product.id].quantity = item.product.quantity
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
        self.ui.code_le.setText("")
        self.ui.name_le.setText("")
        self.ui.phone_le.setText("")
        self.ui.address_le.setText("")

    # clear lỗi
    def clear_error(self):
        self.ui.code_le.setStyleSheet(Validate.BORDER_VALID.value)
        self.ui.name_le.setStyleSheet(Validate.BORDER_VALID.value)
        self.ui.phone_le.setStyleSheet(Validate.BORDER_VALID.value)
        self.ui.error_code.setText("")
        self.ui.error_name.setText("")
        self.ui.error_phone.setText("")
        self.ui.error_address.setText("")
