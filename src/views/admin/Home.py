from PyQt5.QtWidgets import QWidget, QMessageBox, QMainWindow,QAbstractItemView, QApplication, QPushButton
from PyQt5.QtCore import Qt, QPoint, pyqtSlot
from PyQt5.QtGui import QMouseEvent, QIcon, QPixmap

from src.views.ui_generated.admin.home import Ui_MainWindow
from src.controllers.admin.UserController import UserController
from src.models.users import User


class HomeWindow(QMainWindow):
    def __init__(self, user_id):
        super(HomeWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.USER_ID = user_id

        # hide collapse menu
        self.ui.icon_only_widget.hide()
        # initialize widget in app
        self.customers_btn_2 = self.ui.customers_btn_2
        self.pages = self.ui.stackedWidget
        self.pages.setCurrentIndex(9)

        # connect signal and slot
        # change window
        self.customers_btn_2.toggled.connect(
            lambda: self.do_change_page(self.customers_btn_2))
        # self.create_pw_btn.toggled.connect(
        #     lambda: self.do_change_page(self.create_pw_btn))
        # self.conf_btn.toggled.connect(
        #     lambda: self.do_change_page(self.conf_btn))

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

    def do_change_page(self, btn):
        """
        function for change page
        """
        btn_text = btn.text().strip()
        if btn_text == self.home_btn_2.text().strip():
            self.pages.setCurrentIndex(0)
            self.on_showSearchBtn_clicked()
        elif btn_text == self.customers_btn_2.text().strip():
            self.pages.setCurrentIndex(2)
        else:
            self.pages.setCurrentIndex(2)
            self.on_confRefreshBtn_clicked()

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

    ## functions for changing menu page
    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_dashborad_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_dashborad_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_orders_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_orders_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_products_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_products_btn_2_toggled(self, ):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_customers_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_customers_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        # self.ui.stackedWidget.setCurrentIndex(4)

    def validateEmpty(self, data: dict, messages: dict, color_style, border_style):
        result = []
        for key, value in data.items():
            label_name = f"error_{key}"
            label = getattr(self.ui, label_name, None)
            input_name = f"{key}_le"
            input_text = getattr(self.ui, input_name, None)
            print(input_name)
            if not value:
                message = messages[f"{key}Empty"]
                result.append(message)
                if label:
                    label.setText(message)
                    label.setStyleSheet(color_style)
                if input_text:
                    input_text.setStyleSheet(border_style)
        return result

    def getAllUser(self):
        user_controller = UserController()
        test = user_controller.getData()

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

        if user_controller.checkExitsUser(username=username):
            self.ui.error_username.setStyleSheet(color_style)
            self.ui.error_username.setText(messages["usernameExit"])
            self.ui.username_le.setStyleSheet(border_style)
            return

        message = user_controller.checkUserEmailOrPhone(username=username)
        if message:
            self.ui.error_username.setStyleSheet(color_style)
            self.ui.error_username.setText(message)
            self.ui.username_le.setStyleSheet(border_style)
            return

        user = User(name=name, username=username, password=password)
        user_controller.saveUser(user=user)
