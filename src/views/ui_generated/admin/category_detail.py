# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/admin/category_detail.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(924, 502)
        Form.setStyleSheet("#backBtn{\n"
"    margin-left: 10px;\n"
"    margin-right: 10px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QPushButton{\n"
"    min-height: 36px;\n"
"    font-size: 14px;\n"
"    padding: 2px 12px;\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section {\n"
"      height: 48px;\n"
"    font-weight: 600;\n"
"    text-align: left;\n"
"    font-size: 14px;\n"
"    border-bottom: 1px solid #e0e1ef;\n"
"    border-right: 1px solid #e0e1ef;\n"
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
"QLineEdit{\n"
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
"#centralwidget QLineEdit:focus {\n"
"    border-color: #5500ff;\n"
"}\n"
"\n"
"#btn_cancel_category{\n"
"    background: #ebebeb;\n"
"    outline: none;\n"
"    border: 1px solid #e0e0e0;\n"
"    min-height: 36px;\n"
"    min-width: 80px;\n"
"    border-radius: 4px;\n"
"    padding: 2px 12px;\n"
"}\n"
"\n"
"#btn_cancel_category:hover{\n"
"    background: #f4f5f8;\n"
"}\n"
"\n"
"#btnUser{\n"
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
"#btnUser:hover{\n"
"        background: #0062cc;\n"
"}\n"
"\n"
"#footerUserContainer{\n"
"     background-color: #fbfbfe;\n"
"    padding: 12px 24px;\n"
"    border-top: 1px solid #e0e0e0;\n"
"}\n"
"\n"
"#backBtn{\n"
"    margin-left: 10px;\n"
"    margin-right: 10px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"#dialog_title_category{\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#popupHeader{\n"
"    height: 60px;\n"
"    min-height: 24px;\n"
"}\n"
"\n"
"#widget_12, #widget_11, #widget_10, #widget_7{\n"
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
"#labelName, #labelUserName, #labelPassword, #labelConfirm{\n"
"    margin-top:30px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    min-width: 80px;\n"
"    min-height: 36px;\n"
"    border-radius: 4px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"#error_category_name{\n"
"    padding-top: 8px;\n"
"    padding-bottom: 8px;\n"
"}\n"
"\n"
"#btn_save_category{\n"
"        width:  100px;\n"
"        background: #2979ff;\n"
"        color: #fff;\n"
"}\n"
"\n"
"#btn_save_category:hover{\n"
"    background: #1a73e8;\n"
"}\n"
"\n"
"#btn_save_category QLabel{\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"#search_btn_2{\n"
"    border: none;\n"
"}\n"
"\n"
"#searchBoxContainer QLineEdit, #searchBoxContainer_2 QLineEdit{\n"
"    border: none;\n"
"}\n"
"\n"
"#searchBoxContainer{\n"
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
"#back_btn_category{\n"
"    min-width: 30px;\n"
"}\n"
"\n"
"#search_input_5{\n"
"    padding: 0;\n"
"    padding-left: 10px\n"
"}\n"
"\n"
"#customers_btn_2, #products_btn_2, #orders_btn_2, #dashboard_btn_2,#home_btn_2,#user_btn_2{\n"
"    text-align: left;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_6 = QtWidgets.QWidget(Form)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.popupHeader = QtWidgets.QWidget(self.widget_6)
        self.popupHeader.setMinimumSize(QtCore.QSize(0, 60))
        self.popupHeader.setObjectName("popupHeader")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.popupHeader)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.back_btn_category = QtWidgets.QPushButton(self.popupHeader)
        self.back_btn_category.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_btn_category.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/resources/icon/back.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn_category.setIcon(icon)
        self.back_btn_category.setObjectName("back_btn_category")
        self.horizontalLayout_7.addWidget(self.back_btn_category)
        self.dialog_title_category = QtWidgets.QLabel(self.popupHeader)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.dialog_title_category.setFont(font)
        self.dialog_title_category.setObjectName("dialog_title_category")
        self.horizontalLayout_7.addWidget(self.dialog_title_category)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_7.addWidget(self.popupHeader)
        self.widget_9 = QtWidgets.QWidget(self.widget_6)
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
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.formInput_5 = QtWidgets.QHBoxLayout()
        self.formInput_5.setContentsMargins(-1, 0, -1, -1)
        self.formInput_5.setSpacing(0)
        self.formInput_5.setObjectName("formInput_5")
        self.labelName = QtWidgets.QLabel(self.widget_14)
        self.labelName.setMinimumSize(QtCore.QSize(200, 0))
        self.labelName.setObjectName("labelName")
        self.formInput_5.addWidget(self.labelName, 0, QtCore.Qt.AlignTop)
        self.widget_15 = QtWidgets.QWidget(self.widget_14)
        self.widget_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_15.setObjectName("widget_15")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.widget_15)
        self.verticalLayout_16.setContentsMargins(0, 15, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.category_name_le = QtWidgets.QLineEdit(self.widget_15)
        self.category_name_le.setMinimumSize(QtCore.QSize(222, 46))
        self.category_name_le.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.category_name_le.setText("")
        self.category_name_le.setPlaceholderText("Tên loại sản phẩm")
        self.category_name_le.setClearButtonEnabled(True)
        self.category_name_le.setObjectName("category_name_le")
        self.verticalLayout_16.addWidget(self.category_name_le)
        self.error_category_name = QtWidgets.QLabel(self.widget_15)
        self.error_category_name.setText("")
        self.error_category_name.setObjectName("error_category_name")
        self.verticalLayout_16.addWidget(self.error_category_name)
        self.formInput_5.addWidget(self.widget_15, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_20.addLayout(self.formInput_5)
        self.horizontalLayout_9.addWidget(self.widget_14)
        self.userDialogFormContainer_2.addWidget(self.widget_7)
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
        self.btn_cancel_category = QtWidgets.QPushButton(self.userDialogFormSubContainer)
        self.btn_cancel_category.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cancel_category.setObjectName("btn_cancel_category")
        self.horizontalLayout_19.addWidget(self.btn_cancel_category)
        self.btn_save_category = QtWidgets.QPushButton(self.userDialogFormSubContainer)
        self.btn_save_category.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save_category.setObjectName("btn_save_category")
        self.horizontalLayout_19.addWidget(self.btn_save_category)
        self.verticalLayout_11.addLayout(self.horizontalLayout_19)
        self.userDialogFormContainer_2.addWidget(self.userDialogFormSubContainer)
        self.verticalLayout_10.addLayout(self.userDialogFormContainer_2)
        self.horizontalLayout_11.addWidget(self.userDialogForm)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)
        self.verticalLayout_7.addWidget(self.widget_9)
        self.verticalLayout_9.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addWidget(self.widget_6)
        self.verticalLayout.addLayout(self.verticalLayout_8)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.dialog_title_category.setText(_translate("Form", "Thêm mới loại sản phẩm"))
        self.labelName.setText(_translate("Form", "Tên loại sản phẩm"))
        self.btn_cancel_category.setText(_translate("Form", "Hủy"))
        self.btn_save_category.setText(_translate("Form", "Lưu"))
import ui.resource_rc
