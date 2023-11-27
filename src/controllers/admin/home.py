from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import Qt, QPoint, pyqtSlot
from PyQt5.QtGui import QMouseEvent, QIcon, QPixmap

from src.views.admin.home import Ui_MainWindow
from src.controllers.connect_database import ConnectMySQL
from src.controllers.common.common_function import warning_messagebox

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

    def on_btnUser_clicked(self):
        user_name = self.ui.user_le.text().strip()
        password = self.ui.pass_le.text().strip()
        confirm = self.ui.confirm_le.text().strip()
        warning_messagebox(confirm)






