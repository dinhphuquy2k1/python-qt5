# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/common/login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(1227, 839)
        Form.setStyleSheet("/* Set style for app title widget */\n"
"#titleWidget {\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    background: #fff;\n"
"    border-right: 1px;\n"
"}\n"
"\n"
"#page{\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"#imgLogin{\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#titleWidgetContainer{\n"
"        border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#Form *{\n"
"    background: #fff;\n"
"}\n"
"\n"
"#titleWidget QLabel {\n"
"    color: rgba(255, 255, 255, 0.8);\n"
"    font-family: \"Stencil\";\n"
"}\n"
"\n"
"#titleLabel1 {\n"
"    font-size: 40px;\n"
"}\n"
"\n"
"#titleLabel2 {\n"
"    font-size: 30px;\n"
"}\n"
"\n"
"/* Set style for function widget */\n"
"#funcWidget {\n"
"    background-color: #fff;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-left: 1px solid #ececec;\n"
"}\n"
"\n"
"/* Set style for all the QLabel in function widget */\n"
"#funcWidget QLabel {\n"
"    color: #505050;\n"
"}\n"
"\n"
"/* Set style for login label and register label in function widget */\n"
"#loginLabel, #registerLabel {\n"
"    font-family: \"Time New Roman\";\n"
"    font-size: 30px;\n"
"}\n"
"\n"
"/* Set style for all the QLineEdit in function widget */\n"
"#funcWidget QLineEdit {\n"
"    border: 1px solid #e5ebf0;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"#funcWidget QLineEdit:focus {\n"
"    border-color: #5500ff;\n"
"}\n"
"\n"
"/* Set style for all the buttons in function widget */\n"
"#funcWidget QPushButton {\n"
"    font-size: 12em;\n"
"    border-radius: 5px;\n"
"    color: #fff;\n"
"}\n"
"\n"
"#funcWidget QPushButton:pressed {\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"/* Set style for login and create user button in function widget */\n"
"#loginBtn, #createBtn {\n"
"    background-color: #0062cc;\n"
"    white-space: nowrap;\n"
"    font-size: 14px;\n"
"     font-weight: normal;\n"
"    padding-top: 7px;\n"
"    height: 48px;\n"
"    padding-bottom: 7px;\n"
"}\n"
"\n"
"#exitBtnContainer QPushButton{\n"
"        padding-top: 10px;\n"
"}\n"
"\n"
"#loginBtn:hover, #loginBtn:pressed, #createBtn:hover, #createBtn:pressed {\n"
"    background-color: #0000ff;\n"
"}\n"
"\n"
"\n"
"/* Set style for exit button in function widget */\n"
"#exitBtn {\n"
"    background-color: #d10000;\n"
"    padding-top: 7px;\n"
"    padding-bottom: 7px;\n"
"    height: 48px;\n"
"}\n"
"\n"
"#exitBtn:hover, #exitBtn:pressed {\n"
"    background-color: #910000;\n"
"}\n"
"\n"
"/* Set style for register and back button in function widget */\n"
"#registerBtn, #backBtn {\n"
"    background-color: #55aa7f;\n"
"}\n"
"\n"
"#registerBtn:hover, #registerBtn:pressed, #backBtn:hover, #backBtn:pressed {\n"
"    background-color: #3aad00;\n"
"}\n"
"\n"
" QLineEdit{\n"
"    border: 1px solid #e0e5e9;\n"
"    background: transparent;\n"
"    font-size: 16px;\n"
"    line-height: 1.2;\n"
"    height: 48px;\n"
"    border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#footerLogin #forgotBtn{\n"
"    white-space: nowrap;\n"
"    color: #1A73E8;\n"
"     padding-top: 7px;\n"
"    padding-bottom: 7px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"#forgotBtn:hover{\n"
"       text-decoration: underline;\n"
"}\n"
" \n"
"QLabel{\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#page, #title{\n"
"    background: #fff;\n"
"}\n"
"\n"
"#funcWidget{\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(111, 835, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.titleWidgetContainer = QtWidgets.QWidget(Form)
        self.titleWidgetContainer.setMinimumSize(QtCore.QSize(500, 600))
        self.titleWidgetContainer.setMaximumSize(QtCore.QSize(500, 600))
        self.titleWidgetContainer.setObjectName("titleWidgetContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.titleWidgetContainer)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titleWidget = QtWidgets.QWidget(self.titleWidgetContainer)
        self.titleWidget.setObjectName("titleWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.titleWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.imgLogin = QtWidgets.QLabel(self.titleWidget)
        self.imgLogin.setMaximumSize(QtCore.QSize(390, 350))
        self.imgLogin.setText("")
        self.imgLogin.setPixmap(QtGui.QPixmap(":/img/resources/img/sideimg.webp"))
        self.imgLogin.setScaledContents(True)
        self.imgLogin.setObjectName("imgLogin")
        self.verticalLayout.addWidget(self.imgLogin, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.titleWidget)
        self.horizontalLayout.addWidget(self.titleWidgetContainer)
        self.funcWidget = QtWidgets.QStackedWidget(Form)
        self.funcWidget.setMinimumSize(QtCore.QSize(500, 600))
        self.funcWidget.setMaximumSize(QtCore.QSize(500, 600))
        self.funcWidget.setObjectName("funcWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 1, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(30)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.loginLabel = QtWidgets.QLabel(self.page)
        self.loginLabel.setStyleSheet("#loginLabel {\n"
"    color: #000;\n"
"}")
        self.loginLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loginLabel.setObjectName("loginLabel")
        self.verticalLayout_5.addWidget(self.loginLabel)
        self.title = QtWidgets.QHBoxLayout()
        self.title.setSpacing(2)
        self.title.setObjectName("title")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.title.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.title.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.title.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.title.addItem(spacerItem3)
        self.verticalLayout_5.addLayout(self.title)
        self.userContainer = QtWidgets.QVBoxLayout()
        self.userContainer.setSpacing(10)
        self.userContainer.setObjectName("userContainer")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 48))
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.userContainer.addWidget(self.lineEdit)
        self.verticalLayout_5.addLayout(self.userContainer)
        self.passContainer = QtWidgets.QVBoxLayout()
        self.passContainer.setSpacing(10)
        self.passContainer.setObjectName("passContainer")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 48))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.passContainer.addWidget(self.lineEdit_2)
        self.verticalLayout_5.addLayout(self.passContainer)
        self.footerLogin = QtWidgets.QWidget(self.page)
        self.footerLogin.setObjectName("footerLogin")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.footerLogin)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.loginBtn = QtWidgets.QPushButton(self.footerLogin)
        self.loginBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.loginBtn.setMaximumSize(QtCore.QSize(16777215, 48))
        self.loginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/login-64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginBtn.setIcon(icon)
        self.loginBtn.setObjectName("loginBtn")
        self.verticalLayout_3.addWidget(self.loginBtn)
        self.forgotBtn = QtWidgets.QPushButton(self.footerLogin)
        self.forgotBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.forgotBtn.setObjectName("forgotBtn")
        self.verticalLayout_3.addWidget(self.forgotBtn)
        self.verticalLayout_5.addWidget(self.footerLogin)
        self.exitBtnContainer = QtWidgets.QHBoxLayout()
        self.exitBtnContainer.setSpacing(5)
        self.exitBtnContainer.setObjectName("exitBtnContainer")
        self.exitBtn = QtWidgets.QPushButton(self.page)
        self.exitBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.exitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/x-mark-3-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitBtn.setIcon(icon1)
        self.exitBtn.setObjectName("exitBtn")
        self.exitBtnContainer.addWidget(self.exitBtn)
        self.verticalLayout_5.addLayout(self.exitBtnContainer)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(79, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(79, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 129, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 0, 1, 1, 1)
        self.funcWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(20, 129, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem7, 0, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(79, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 1, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.registerLabel = QtWidgets.QLabel(self.page_2)
        self.registerLabel.setStyleSheet("#registerLabel {\n"
"    color: #000;\n"
"}")
        self.registerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.registerLabel.setObjectName("registerLabel")
        self.verticalLayout_6.addWidget(self.registerLabel)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(350, 0))
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_7.addWidget(self.lineEdit_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_8.addWidget(self.lineEdit_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.backBtn = QtWidgets.QPushButton(self.page_2)
        self.backBtn.setMinimumSize(QtCore.QSize(0, 30))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/arrow-80-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backBtn.setIcon(icon2)
        self.backBtn.setObjectName("backBtn")
        self.horizontalLayout_2.addWidget(self.backBtn)
        self.createBtn = QtWidgets.QPushButton(self.page_2)
        self.createBtn.setMinimumSize(QtCore.QSize(0, 30))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/check-mark-3-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.createBtn.setIcon(icon3)
        self.createBtn.setObjectName("createBtn")
        self.horizontalLayout_2.addWidget(self.createBtn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout_6, 1, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(79, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 1, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem10, 2, 1, 1, 1)
        self.funcWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.funcWidget)
        spacerItem11 = QtWidgets.QSpacerItem(110, 835, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)

        self.retranslateUi(Form)
        self.funcWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.loginLabel.setText(_translate("Form", "Login"))
        self.label_2.setText(_translate("Form", "Đăng nhập để làm việc với"))
        self.label.setText(_translate("Form", "Fit Store"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Email hoặc số điện thoại"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Mật khẩu"))
        self.loginBtn.setText(_translate("Form", "Đăng nhập"))
        self.forgotBtn.setText(_translate("Form", "Quên mật khẩu?"))
        self.exitBtn.setText(_translate("Form", "Exit"))
        self.registerLabel.setText(_translate("Form", "Register"))
        self.label_3.setText(_translate("Form", "Username"))
        self.label_4.setText(_translate("Form", "Password"))
        self.backBtn.setText(_translate("Form", "Back"))
        self.createBtn.setText(_translate("Form", "Create"))
import ui.resource_rc
