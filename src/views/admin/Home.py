from PyQt5.QtWidgets import QWidget, QMessageBox, QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import Qt, QPoint, pyqtSlot
from PyQt5.QtGui import QMouseEvent, QIcon, QPixmap

from src.views.ui_generated.admin.home import Ui_MainWindow
from src.controllers.admin.UserController import UserController
from src.enums.enums import *

class HomeWindow(QMainWindow):
    def __init__(self):
        super(HomeWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # initialize widget in app
        # hide collapse menu
        self.ui.icon_only_widget.hide()
        self.customers_btn_2 = self.ui.customers_btn_2

        ## connect signal and slot
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
            self.pages.setCurrentIndex(7)
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

    def validateEmpty(self, data: dict, messages: dict, color_style):
        result = []
        for key, value in data.items():
            label_name = f"error_{key}"
            label = getattr(self.ui, label_name, None)
            if not value:
                message = messages[f"{key}Empty"]
                result.append(message)
                if label:
                    label.setText(message)
                    label.setStyleSheet(color_style)
            else:
                if label:
                    label.setText("")
        return result

    @pyqtSlot()
    def on_btnUser_clicked(self):
        user = self.ui.user_le.text().strip()
        password = self.ui.pass_le.text().strip()
        confirm = self.ui.confirm_le.text().strip()
        color_style = "color: #ef5350;"
        messages = {
            'userEmpty': "Vui lòng nhập thông tin tài khoản.",
            'userExit': "Tài khoản đã tồn tại.",
            'passwordEmpty': "Vui lòng nhập thông tin mật khẩu.",
            'confirmEmpty': "Vui lòng nhập lại mật khẩu.",
            'confirmNotMatch': "Mật  khẩu không trùng khớp.",
        }

        is_valid = self.validateEmpty({'user': user, 'password': password, 'confirm': confirm}, messages, color_style)
        if is_valid:
            return

        if password != confirm:
            self.ui.error_confirm.setStyleSheet(color_style)
            self.ui.error_confirm.setText(messages["confirmNotMatch"])
            return

        user_controller = UserController()

        if user_controller.checkExitsUser(username=user):
            self.ui.error_user.setStyleSheet(color_style)
            self.ui.error_user.setText(messages["userExit"])
            return

        message = user_controller.checkUserEmailOrPhone(username=user)
        if message:
            self.ui.error_user.setStyleSheet(color_style)
            self.ui.error_user.setText(message)
            return
