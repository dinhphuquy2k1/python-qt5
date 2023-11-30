from PyQt5.QtWidgets import QWidget, QHBoxLayout, QMainWindow,QTableWidgetItem,QAbstractItemView, QApplication, QPushButton
from PyQt5.QtCore import Qt, QPoint, pyqtSlot
from PyQt5.QtGui import QMouseEvent, QIcon, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from src.views.ui_generated.admin.home import Ui_MainWindow
from src.views.common.Common import *
from src.enums.enums import *
from src.controllers.admin.UserController import UserController
from src.models.users import User


class HomeWindow(QMainWindow):
    def __init__(self, user_id):
        super(HomeWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.USER_ID = user_id

        self.page_index = dict(
            HOME_PAGE=0,
            DASHBOARD_PAGE=1,
            ORDER_PAGE=2,
            PRODUCT_PAGE=3,
            CUSTOMER_PAGE=4,
            USER_PAGE=6,
            USER_PAGE_DETAIL=7,
        )

        # khởi tạo widget
        self.customers_btn_2 = self.ui.customers_btn_2
        self.products_btn_2 = self.ui.products_btn_2
        self.user_btn_2 = self.ui.user_btn_2
        self.orders_btn_2 = self.ui.orders_btn_2
        self.dashboard_btn_2 = self.ui.dashboard_btn_2
        self.home_btn_2 = self.ui.home_btn_2

        # khởi tạo controller
        self.user_controller = UserController()

        # khởi tạo biến
        self.user_table = self.ui.tableUser
        # hiển thị header
        self.user_table.horizontalHeader().setVisible(True)
        # lưu giá trị data khi click row trong table
        self.id_data_selected = None
        # trạng thái form
        self.mode = FormMode.ADD

        # ẩn menu nhỏ
        self.ui.icon_only_widget.hide()

        # khởi tạo các button change page
        self.customers_btn_2 = self.ui.customers_btn_2
        self.add_user_btn = self.ui.addUserBtn

        # khởi tạo page
        # sét trang mặc định hiển thị khi page được hiển thj
        self.pages = self.ui.stackedWidget
        self.pages.setCurrentIndex(9)

        # khởi tạo signal và slot
        # bắt sự kiện click menu
        self.customers_btn_2.toggled.connect(
            lambda: self.do_change_page(self.page_index['CUSTOMER_PAGE']))
        self.user_btn_2.toggled.connect(
            lambda: self.do_change_page(self.page_index['USER_PAGE']))
        self.products_btn_2.toggled.connect(
            lambda: self.do_change_page(3)
        )
        self.orders_btn_2.toggled.connect(
            lambda: self.do_change_page(self.page_index['ORDER_PAGE'])
        )
        self.dashboard_btn_2.toggled.connect(
            lambda: self.do_change_page(self.page_index['DASHBOARD_PAGE'])
        )
        self.home_btn_2.toggled.connect(
            lambda: self.do_change_page(0)
        )

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_9.setText(search_text)

    ## Function for changing page to user page
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    @pyqtSlot()
    def on_back_btn_user_clicked(self):
        self.pages.setCurrentIndex(self.page_index['USER_PAGE'])
        # load lại dữ liệu
        self.show_user_table()

    # clear input form user
    def clearUserForm(self):
        self.ui.username_le.setText("")
        self.ui.password_le.setText("")
        self.ui.confirm_le.setText("")
        self.ui.name_le.setText("")

    # sự kiện click button thêm mới tài khoản
    @pyqtSlot()
    def on_addUserBtn_clicked(self):
        self.pages.setCurrentIndex(self.page_index['USER_PAGE_DETAIL'])
        self.mode = FormMode.ADD
        self.clearUserForm()

    """
    function for change page
    """
    def do_change_page(self, index):
        self.pages.setCurrentIndex(index)
        if index == self.page_index['USER_PAGE']:
            self.show_user_table()


    ## Change QPushButton Checkable status when stackedWidget index changed
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                   + self.ui.full_menu_widget.findChildren(QPushButton)
        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)

    #validate form input empty
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

    # Lấy danh sách user
    def getAllUser(self):
        return self.user_controller.getData()

    # hiển thị list thông tin user lên table
    def show_user_table(self):
        user_list = self.getAllUser()
        self.user_table.setRowCount(0)
        if user_list:
            for index, item in enumerate(user_list):
                column_index = 0
                self.user_table.setRowCount(index+1)
                self.user_table.setItem(index, column_index, QTableWidgetItem(str(index+1)))
                self.user_table.setItem(index, column_index+1, QTableWidgetItem(str(item.id)))
                self.user_table.setItem(index, column_index+2, QTableWidgetItem(str(item.username)))
                self.user_table.setItem(index, column_index+3, QTableWidgetItem(str(item.name)))
                widget, edit_btn, delete_btn = generate_action_row(item.id, "user")
                edit_btn.clicked.connect(
                    lambda: self.on_row_click(self.user_table, FormMode.EDIT, self.page_index["USER_PAGE_DETAIL"]))
                delete_btn.clicked.connect(
                    lambda: self.on_row_click(self.user_table, FormMode.DELETE, self.page_index["USER_PAGE_DETAIL"]))
                self.user_table.setCellWidget(index, column_index+4, widget)


    # function click edit row
    def on_row_click(self, table, form_mode, page_index):
        # lấy data
        button = self.sender()
        user_id = int(button.objectName().strip().rsplit('_', 1)[-1])
        # xử lý sự kiện cho từng màn
        if page_index == self.page_index["USER_PAGE_DETAIL"]:
            if form_mode == FormMode.DELETE:
                self.on_delete_user(user_id)
            elif form_mode == FormMode.EDIT:
                # hiển thị màn hình
                self.pages.setCurrentIndex(page_index)
                self.on_edit_user(user_id)

    # hàm chỉnh sửa thông tin user
    def on_edit_user(self, user_id):
        self.mode = FormMode.EDIT
        self.id_data_selected = user_id
        user = self.user_controller.getUserByIdWithModel(user_id)
        self.ui.name_le.setText(user.name)
        self.ui.username_le.setText(user.username)
        self.ui.password_le.setText(user.password)
        self.ui.confirm_le.setText(user.password)

    # xóa user
    def on_delete_user(self, user_id):
        reply = self.initialize_message_box_delete().exec_()
        if reply == QMessageBox.Yes:
            self.user_controller.deleteUserWithModel(user_id)
            self.show_user_table()
        else:
            return

    # tạo form hiển thị cảnh báo xóa
    def initialize_message_box_delete(self):
        # Create QMessageBox
        msgBox = QMessageBox(self)
        msgBox.setWindowIcon(QIcon("./static/icon/key-6-128.ico"))
        msgBox.setIconPixmap(QPixmap("./static/icon/question-mark-7-48.ico"))
        msgBox.setWindowTitle("Thông báo")
        msgBox.setText("Bạn có chắc chắn muốn xóa không?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        return msgBox

    # click button thêm mới user
    @pyqtSlot()
    def on_btnUser_clicked(self):
        name = self.ui.name_le.text().strip()
        username = self.ui.username_le.text().strip()
        password = self.ui.password_le.text().strip()
        confirm = self.ui.confirm_le.text().strip()
        color_style = "color: #ef5350;"
        border_style = "border: 1px solid #ef5350;"
        # sét border mặc định cho input
        self.ui.name_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.password_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.username_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.confirm_le.setStyleSheet("border: 1px solid #e0e5e9;")
        # xóa error text
        self.ui.error_username.setText("")
        self.ui.error_confirm.setText("")
        self.ui.error_name.setText("")
        self.ui.error_password.setText("")

        messages = {
            'nameEmpty': "Vui lòng nhập họ và tên.",
            'usernameEmpty': "Vui lòng nhập thông tin tài khoản.",
            'usernameExit': "Tài khoản đã tồn tại.",
            'passwordEmpty': "Vui lòng nhập thông tin mật khẩu.",
            'confirmEmpty': "Vui lòng nhập lại mật khẩu.",
            'confirmNotMatch': "Mật  khẩu không trùng khớp.",
        }
        # validate dữ liệu các cột không được trống
        is_valid = self.validateEmpty({'name': name, 'username': username, 'password': password, 'confirm': confirm},
                                      messages, color_style, border_style)
        if is_valid:
            return

        if password != confirm:
            self.ui.error_confirm.setStyleSheet(color_style)
            self.ui.error_confirm.setText(messages["confirmNotMatch"])
            self.ui.confirm_le.setStyleSheet(border_style)
            return

        user_controller = UserController()
        message = user_controller.checkUserEmailOrPhone(username=username)
        if message:
            self.ui.error_username.setStyleSheet(color_style)
            self.ui.error_username.setText(message)
            self.ui.username_le.setStyleSheet(border_style)
            return


        if self.mode == FormMode.ADD:
            if user_controller.checkExitsUser(username=username):
                self.ui.error_username.setStyleSheet(color_style)
                self.ui.error_username.setText(messages["usernameExit"])
                self.ui.username_le.setStyleSheet(border_style)
                return
            user = User(name=name, username=username, password=password)
            user_controller.saveUser(user=user)
        elif self.mode == FormMode.EDIT:
            if user_controller.checkExitsUserUpdate(username=username, user_id=self.id_data_selected):
                self.ui.error_username.setStyleSheet(color_style)
                self.ui.error_username.setText(messages["usernameExit"])
                self.ui.username_le.setStyleSheet(border_style)
                return
            user = {'username': username, 'name': name, 'password': password}
            user_controller.updateUserWithModel(data=user, user_id=self.id_data_selected)
        else:
            return
        # quay về trang danh sách
        self.pages.setCurrentIndex(self.page_index["USER_PAGE"])
        # load lại dữ liệu
        self.show_user_table()
