# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/admin/member_rank_detail.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(922, 695)
        Form.setStyleSheet("QSpinBox{\n"
"    border: 1px solid #e0e5e9;\n"
"    background: transparent;\n"
"    font-size: 16px;\n"
"    line-height: 1.2;\n"
"    min-height:34px;\n"
"    height: 34px;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    min-width: 200px;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border-color: #5500ff;\n"
"}\n"
"\n"
"QLineEdit, QPlainTextEdit{\n"
"    border: 1px solid #e0e5e9;\n"
"    font-size: 16px;\n"
"    line-height: 1.2;\n"
"    min-height:34px;\n"
"    height: 34px;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    min-width: 200px;\n"
"}\n"
"\n"
"    QScrollBar:vertical\n"
"    {\n"
"        background-color: #fff;\n"
"        width: 15px;\n"
"        margin: 15px 3px 15px 3px;\n"
"        border: 1px transparent #2A2929;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical\n"
"    {\n"
"        background-color: #cdd3d6;         /* #605F5F; */\n"
"        min-height: 5px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"#scrollArea_2, #verticalLayout_6, #userDialogForm, #scrollAreaWidgetContents_2, #widget{\n"
"    background: #fff;\n"
"}\n"
"    QScrollBar::sub-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"#dialog_product_title{\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#centralwidget QLineEdit:focus, QPlainTextEdit:focus {\n"
"    border-color: #5500ff;\n"
"}\n"
"\n"
"#userDialogForm QLabel{\n"
"    color: #000;\n"
"    font-size: 16px;\n"
"    font-weight: 400;\n"
"}\n"
"\n"
"#userDialogForm  QLineEdit{\n"
"    border: 1px solid #e0e5e9;\n"
"    background: transparent;\n"
"    font-size: 16px;\n"
"    line-height: 1.2;\n"
"    min-height:34px;\n"
"    height: 34px;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    min-width: 200px;\n"
"}\n"
"\n"
"#centralwidget QLineEdit:focus {\n"
"    border-color: #5500ff;\n"
"}\n"
"\n"
"QPushButton{\n"
"    min-height: 36px;\n"
"    font-size: 14px;\n"
"    padding: 2px 12px;\n"
"}\n"
"\n"
"QHBoxLayout QLabel{\n"
"    background: red;\n"
"}\n"
"\n"
"#btn_save_product{\n"
"    min-height: 36px;\n"
"    border-radius: 4px;\n"
"    color: #fff;\n"
"    background: #2979ff;\n"
"    border: 1px;\n"
"    font-size: 14px;\n"
"    padding: 2px 12px;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"#btn_add_product_category{\n"
"    min-height: 42px;\n"
"    border-radius: 4px;\n"
"    color: #fff;\n"
"    background: #2979ff;\n"
"    border: 1px;\n"
"    font-size: 14px;\n"
"    padding: 2px 12px;\n"
"    min-width: 30px;\n"
"}\n"
"\n"
"#btn_save_product:hover{\n"
"        background: #0062cc;\n"
"}\n"
"\n"
"\n"
"#btn_cancel_rank{\n"
"    background: #ebebeb;\n"
"    outline: none;\n"
"    border: 1px solid #e0e0e0;\n"
"    min-height: 36px;\n"
"    min-width: 80px;\n"
"    border-radius: 4px;\n"
"    padding: 2px 12px;\n"
"}\n"
"\n"
"#btn_cancel_product:hover{\n"
"    background: #f4f5f8;\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section {\n"
"      height: 48px;\n"
"    font-weight: 600;\n"
"    text-align: left;\n"
"    font-size: 14px;\n"
"\n"
"    font-weight: 600;\n"
"    background: #fff;\n"
"    padding: 0 16px;\n"
"}\n"
"#tableUserContainer{\n"
"    border: none;\n"
"    border-radius:  4px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"       padding: 0 16px;\n"
"    vertical-align: middle;\n"
"    height: 50px;\n"
"    border-bottom: 1px solid #ddd;    \n"
"    border-right: 1px solid #ddd;\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"#stackedWidget{\n"
"    background: #fff;\n"
"}\n"
"\n"
"#userDialogForm QLabel{\n"
"    color: #000;\n"
"    font-size: 16px;\n"
"    font-weight: 400;\n"
"}\n"
"\n"
"#userDialogForm  QLineEdit, #userDialogForm QComboBox, QSpinBox{\n"
"    border: 1px solid #e0e5e9;\n"
"    background: transparent;\n"
"    font-size: 16px;\n"
"    line-height: 1.2;\n"
"    min-height:34px;\n"
"    height: 34px;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    min-width: 200px;\n"
"}\n"
"\n"
"QLineEdit, QComboxBox,QSpinBox{\n"
"    border: 1px solid #e0e5e9;\n"
"    font-size: 16px;\n"
"    line-height: 1.2;\n"
"    min-height:34px;\n"
"    height: 34px;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    min-width: 200px;\n"
"}\n"
"\n"
"#centralwidget QLineEdit:focus, #centralwidget QComboBox:focus, QSpinBox:focus {\n"
"    border-color: #5500ff;\n"
"}\n"
"\n"
"#btnCancelUser,#btn_image_product, #btn_manufacture_date_product{\n"
"    background: #ebebeb;\n"
"    outline: none;\n"
"    border: 1px solid #e0e0e0;\n"
"    min-height: 36px;\n"
"    min-width: 80px;\n"
"    border-radius: 4px;\n"
"    padding: 2px 12px;\n"
"}\n"
"\n"
"#btn_cancel_rank:hover, #btn_image_product:hover{\n"
"    background: #f4f5f8;\n"
"}\n"
"\n"
"#btn_save_rank{\n"
"    min-height: 36px;\n"
"    border-radius: 4px;\n"
"    color: #fff;\n"
"    background: #2979ff;\n"
"    border: 1px;\n"
"    font-size: 14px;\n"
"    padding: 2px 12px;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    min-height: 36px;\n"
"    font-size: 14px;\n"
"    padding: 2px 12px;\n"
"}\n"
"\n"
"#btn_save_rank:hover{\n"
"        background: #0062cc;\n"
"}\n"
"\n"
"#footerUserContainer{\n"
"     background-color: #fbfbfe;\n"
"    padding: 12px 24px;\n"
"    border-top: 1px solid #e0e0e0;\n"
"}\n"
"\n"
"#back_btn_rank{\n"
"    margin-left: 10px;\n"
"    margin-right: 10px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"#dialogTitleUser{\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#popupHeader{\n"
"    height: 60px;\n"
"    min-height: 24px;\n"
"}\n"
"\n"
"#widget_12, #widget_11, #widget_10, #widget_7, #confirmContainer, #widget_2, #widget_12, #discount_container{\n"
"        border-bottom: 1px solid #e0e0e0;\n"
"}    \n"
"\n"
"#userDialogForm{\n"
"        border-radius: 4px;\n"
"        border: 1px solid #e0e0e0;\n"
"}\n"
"\n"
"\n"
"\n"
"#userDialogFormSubContainer{\n"
"    background: #e9e9e9;\n"
"    border-radius: 4px;\n"
"}\n"
" #formInput_4 QLabel {\n"
"    margin-top: 10px;\n"
"}\n"
"QHBoxLayout QLabel{\n"
"    background: red;\n"
"}\n"
"\n"
"#label_product_1, #labelCode, #labelPassword{\n"
"    margin-top:30px;\n"
"}\n"
"\n"
"QPushButton, QComboBox{\n"
"    min-width: 80px;\n"
"    min-height: 36px;\n"
"    border-radius: 4px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"#error_product_image, #error_quantity, #error_manufacture_date, #error_description, #error_price, #error_name, #error_code, #error_spending, #error_discount{\n"
"    padding-top: 8px;\n"
"    padding-bottom: 8px;\n"
"}\n"
"\n"
"#addUserBtn, #btn_add_category, #btn_add_product{\n"
"        width:  100px;\n"
"        background: #2979ff;\n"
"        color: #fff;\n"
"}\n"
"\n"
"#addUserBtn:hover{\n"
"    background: #1a73e8;\n"
"}\n"
"\n"
"#addUserBtn QLabel{\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"#search_btn_2{\n"
"    border: none;\n"
"}\n"
"\n"
"#searchBoxContainer QLineEdit, #searchBoxContainer_2 QLineEdit, #search_input_category_2, #search_input_product_2{\n"
"    border: none;\n"
"}\n"
"\n"
"#searchBoxContainer, #searchBoxContainer_3,#searchBoxContainer_4{\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 3.5px;    \n"
"    min-height: 36px;\n"
"}\n"
"\n"
"#searchBoxContainer_2{\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 3.5px;\n"
"    min-height: 36px;\n"
"}\n"
"\n"
"#headerAdmin{\n"
"    background: #fff;\n"
"}\n"
"\n"
"#change_btn{\n"
"    max-width: 20px !important;\n"
"}\n"
"\n"
"#change_btn:hover{\n"
"    background: #ddd;\n"
"}\n"
"\n"
"#change_btn, #search_btn_5,  #search_btn_2, #back_btn_category, #search_btn_category_2, #search_btn_product_2, #btn_image_product, #btn_manufacture_date_product, #back_btn_rank{\n"
"    min-width: 30px;\n"
"}\n"
"\n"
"\n"
"#search_input_5{\n"
"    padding: 0;\n"
"    padding-left: 10px\n"
"}\n"
"\n"
"#customers_btn_2, #products_btn_2, #orders_btn_2, #dashboard_btn_2,#home_btn_2,#user_btn_2, #category_btn_2{\n"
"    text-align: left;\n"
"}\n"
"\n"
"#label_required_4, #label_required_3, #label_required_2, #label_required_1{\n"
"    text-align: right;\n"
"}\n"
"\n"
"#btn_image_product{\n"
"    min-height:  40px;\n"
"    min-width: 64px;\n"
"}\n"
"\n"
"QPlainTextEdit{\n"
"    min-height: 82px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.customerDialog = QtWidgets.QWidget(Form)
        self.customerDialog.setObjectName("customerDialog")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.customerDialog)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.popupHeader = QtWidgets.QWidget(self.customerDialog)
        self.popupHeader.setMinimumSize(QtCore.QSize(0, 60))
        self.popupHeader.setObjectName("popupHeader")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.popupHeader)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.back_btn_rank = QtWidgets.QPushButton(self.popupHeader)
        self.back_btn_rank.setMinimumSize(QtCore.QSize(30, 40))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(-1)
        self.back_btn_rank.setFont(font)
        self.back_btn_rank.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_btn_rank.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/resources/icon/back.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn_rank.setIcon(icon)
        self.back_btn_rank.setObjectName("back_btn_rank")
        self.horizontalLayout_7.addWidget(self.back_btn_rank)
        self.dialogTitleUser = QtWidgets.QLabel(self.popupHeader)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(-1)
        font.setBold(True)
        self.dialogTitleUser.setFont(font)
        self.dialogTitleUser.setObjectName("dialogTitleUser")
        self.horizontalLayout_7.addWidget(self.dialogTitleUser)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_7.addWidget(self.popupHeader)
        self.widget_9 = QtWidgets.QWidget(self.customerDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 30)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.userDialogForm = QtWidgets.QWidget(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userDialogForm.sizePolicy().hasHeightForWidth())
        self.userDialogForm.setSizePolicy(sizePolicy)
        self.userDialogForm.setMinimumSize(QtCore.QSize(900, 300))
        self.userDialogForm.setObjectName("userDialogForm")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.userDialogForm)
        self.verticalLayout_10.setContentsMargins(50, 20, 50, 30)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.userDialogFormContainer_2 = QtWidgets.QVBoxLayout()
        self.userDialogFormContainer_2.setContentsMargins(0, 0, 0, 0)
        self.userDialogFormContainer_2.setSpacing(0)
        self.userDialogFormContainer_2.setObjectName("userDialogFormContainer_2")
        self.widget_7 = QtWidgets.QWidget(self.userDialogForm)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.widget_14 = QtWidgets.QWidget(self.widget_7)
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_product_2 = QtWidgets.QWidget(self.widget_14)
        self.label_product_2.setMinimumSize(QtCore.QSize(200, 0))
        self.label_product_2.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label_product_2.setFont(font)
        self.label_product_2.setObjectName("label_product_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.label_product_2)
        self.horizontalLayout_10.setContentsMargins(0, 30, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.label_product_2)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(-1)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.label_required_6 = QtWidgets.QLabel(self.label_product_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_required_6.sizePolicy().hasHeightForWidth())
        self.label_required_6.setSizePolicy(sizePolicy)
        self.label_required_6.setObjectName("label_required_6")
        self.horizontalLayout_10.addWidget(self.label_required_6)
        self.horizontalLayout_2.addWidget(self.label_product_2, 0, QtCore.Qt.AlignTop)
        self.widget_15 = QtWidgets.QWidget(self.widget_14)
        self.widget_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_15.setObjectName("widget_15")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.widget_15)
        self.verticalLayout_16.setContentsMargins(0, 15, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.code_le = QtWidgets.QLineEdit(self.widget_15)
        self.code_le.setMinimumSize(QtCore.QSize(222, 46))
        self.code_le.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(-1)
        self.code_le.setFont(font)
        self.code_le.setText("")
        self.code_le.setPlaceholderText("Mã hạng thành viên")
        self.code_le.setClearButtonEnabled(True)
        self.code_le.setObjectName("code_le")
        self.verticalLayout_16.addWidget(self.code_le)
        self.error_code = QtWidgets.QLabel(self.widget_15)
        self.error_code.setText("")
        self.error_code.setObjectName("error_code")
        self.verticalLayout_16.addWidget(self.error_code)
        self.horizontalLayout_2.addWidget(self.widget_15)
        self.horizontalLayout_9.addWidget(self.widget_14)
        self.userDialogFormContainer_2.addWidget(self.widget_7)
        self.widget_10 = QtWidgets.QWidget(self.userDialogForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.widget_10.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_product_3 = QtWidgets.QWidget(self.widget_10)
        self.label_product_3.setMinimumSize(QtCore.QSize(200, 0))
        self.label_product_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_product_3.setObjectName("label_product_3")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.label_product_3)
        self.horizontalLayout_14.setContentsMargins(0, 30, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_5 = QtWidgets.QLabel(self.label_product_3)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(-1)
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_14.addWidget(self.label_5)
        self.label_required_8 = QtWidgets.QLabel(self.label_product_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_required_8.sizePolicy().hasHeightForWidth())
        self.label_required_8.setSizePolicy(sizePolicy)
        self.label_required_8.setObjectName("label_required_8")
        self.horizontalLayout_14.addWidget(self.label_required_8)
        self.horizontalLayout.addWidget(self.label_product_3, 0, QtCore.Qt.AlignTop)
        self.formInput_6 = QtWidgets.QWidget(self.widget_10)
        self.formInput_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.formInput_6.setObjectName("formInput_6")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.formInput_6)
        self.verticalLayout_13.setContentsMargins(0, 15, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.name_le = QtWidgets.QLineEdit(self.formInput_6)
        self.name_le.setMinimumSize(QtCore.QSize(222, 46))
        self.name_le.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(-1)
        self.name_le.setFont(font)
        self.name_le.setClearButtonEnabled(True)
        self.name_le.setObjectName("name_le")
        self.verticalLayout_13.addWidget(self.name_le)
        self.error_name = QtWidgets.QLabel(self.formInput_6)
        self.error_name.setText("")
        self.error_name.setObjectName("error_name")
        self.verticalLayout_13.addWidget(self.error_name, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.formInput_6)
        self.userDialogFormContainer_2.addWidget(self.widget_10)
        self.confirmContainer = QtWidgets.QWidget(self.userDialogForm)
        self.confirmContainer.setObjectName("confirmContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.confirmContainer)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.confirmContainer_2 = QtWidgets.QWidget(self.confirmContainer)
        self.confirmContainer_2.setMinimumSize(QtCore.QSize(0, 105))
        self.confirmContainer_2.setObjectName("confirmContainer_2")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.confirmContainer_2)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.widget_5 = QtWidgets.QWidget(self.confirmContainer_2)
        self.widget_5.setMinimumSize(QtCore.QSize(200, 0))
        self.widget_5.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setContentsMargins(0, 30, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(-1)
        font.setBold(False)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.label_required_4 = QtWidgets.QLabel(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_required_4.sizePolicy().hasHeightForWidth())
        self.label_required_4.setSizePolicy(sizePolicy)
        self.label_required_4.setObjectName("label_required_4")
        self.horizontalLayout_5.addWidget(self.label_required_4)
        self.horizontalLayout_17.addWidget(self.widget_5, 0, QtCore.Qt.AlignTop)
        self.formInput_3 = QtWidgets.QWidget(self.confirmContainer_2)
        self.formInput_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.formInput_3.setObjectName("formInput_3")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.formInput_3)
        self.verticalLayout_15.setContentsMargins(0, 15, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.spending_le = QtWidgets.QSpinBox(self.formInput_3)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(-1)
        self.spending_le.setFont(font)
        self.spending_le.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spending_le.setMaximum(1000000000)
        self.spending_le.setObjectName("spending_le")
        self.verticalLayout_15.addWidget(self.spending_le)
        self.error_spending = QtWidgets.QLabel(self.formInput_3)
        self.error_spending.setText("")
        self.error_spending.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.error_spending.setObjectName("error_spending")
        self.verticalLayout_15.addWidget(self.error_spending, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_17.addWidget(self.formInput_3, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_17)
        self.verticalLayout_2.addWidget(self.confirmContainer_2)
        self.userDialogFormContainer_2.addWidget(self.confirmContainer)
        self.discount_container = QtWidgets.QWidget(self.userDialogForm)
        self.discount_container.setMinimumSize(QtCore.QSize(0, 105))
        self.discount_container.setObjectName("discount_container")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.discount_container)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.discount_sub_container = QtWidgets.QWidget(self.discount_container)
        self.discount_sub_container.setObjectName("discount_sub_container")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.discount_sub_container)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_dis = QtWidgets.QWidget(self.discount_sub_container)
        self.widget_dis.setMinimumSize(QtCore.QSize(200, 0))
        self.widget_dis.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget_dis.setObjectName("widget_dis")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_dis)
        self.horizontalLayout_13.setContentsMargins(0, 30, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.labelName_3 = QtWidgets.QLabel(self.widget_dis)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(-1)
        font.setBold(False)
        self.labelName_3.setFont(font)
        self.labelName_3.setObjectName("labelName_3")
        self.horizontalLayout_13.addWidget(self.labelName_3)
        self.label_required_7 = QtWidgets.QLabel(self.widget_dis)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_required_7.sizePolicy().hasHeightForWidth())
        self.label_required_7.setSizePolicy(sizePolicy)
        self.label_required_7.setObjectName("label_required_7")
        self.horizontalLayout_13.addWidget(self.label_required_7)
        self.horizontalLayout_3.addWidget(self.widget_dis, 0, QtCore.Qt.AlignTop)
        self.widget_17 = QtWidgets.QWidget(self.discount_sub_container)
        self.widget_17.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_17.setObjectName("widget_17")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.widget_17)
        self.verticalLayout_17.setContentsMargins(0, 15, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.discount_le = QtWidgets.QSpinBox(self.widget_17)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(-1)
        self.discount_le.setFont(font)
        self.discount_le.setMaximum(100)
        self.discount_le.setObjectName("discount_le")
        self.verticalLayout_17.addWidget(self.discount_le)
        self.error_discount = QtWidgets.QLabel(self.widget_17)
        self.error_discount.setText("")
        self.error_discount.setObjectName("error_discount")
        self.verticalLayout_17.addWidget(self.error_discount)
        self.horizontalLayout_3.addWidget(self.widget_17)
        self.verticalLayout_3.addWidget(self.discount_sub_container)
        self.userDialogFormContainer_2.addWidget(self.discount_container)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.userDialogFormContainer_2.addItem(spacerItem2)
        self.userDialogFormSubContainer = QtWidgets.QWidget(self.userDialogForm)
        self.userDialogFormSubContainer.setObjectName("userDialogFormSubContainer")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.userDialogFormSubContainer)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setContentsMargins(-1, 10, 20, 10)
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem3)
        self.btn_cancel_rank = QtWidgets.QPushButton(self.userDialogFormSubContainer)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(-1)
        self.btn_cancel_rank.setFont(font)
        self.btn_cancel_rank.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cancel_rank.setObjectName("btn_cancel_rank")
        self.horizontalLayout_19.addWidget(self.btn_cancel_rank)
        self.btn_save_rank = QtWidgets.QPushButton(self.userDialogFormSubContainer)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(-1)
        self.btn_save_rank.setFont(font)
        self.btn_save_rank.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save_rank.setObjectName("btn_save_rank")
        self.horizontalLayout_19.addWidget(self.btn_save_rank)
        self.verticalLayout_11.addLayout(self.horizontalLayout_19)
        self.userDialogFormContainer_2.addWidget(self.userDialogFormSubContainer)
        self.verticalLayout_10.addLayout(self.userDialogFormContainer_2)
        self.horizontalLayout_11.addWidget(self.userDialogForm)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)
        self.verticalLayout_7.addWidget(self.widget_9)
        self.verticalLayout_9.addLayout(self.verticalLayout_7)
        self.verticalLayout.addWidget(self.customerDialog)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.dialogTitleUser.setText(_translate("Form", "Thêm mới hạng thành viên"))
        self.label_4.setText(_translate("Form", "Mã hạng thành viên"))
        self.label_required_6.setText(_translate("Form", " *"))
        self.label_5.setText(_translate("Form", "Tên hạng thành viên"))
        self.label_required_8.setText(_translate("Form", " *"))
        self.name_le.setPlaceholderText(_translate("Form", "Tên hạng thành viên"))
        self.label_7.setText(_translate("Form", "Chi tiêu tối thiểu"))
        self.label_required_4.setText(_translate("Form", " *"))
        self.labelName_3.setText(_translate("Form", "Khuyến mãi"))
        self.label_required_7.setText(_translate("Form", " *"))
        self.btn_cancel_rank.setText(_translate("Form", "Hủy"))
        self.btn_save_rank.setText(_translate("Form", "Lưu"))
import ui.resource_rc
