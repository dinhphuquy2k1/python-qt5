# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/admin/toast.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_gourp_btn(object):
    def setupUi(self, Form_gourp_btn):
        Form_gourp_btn.setObjectName("Form_gourp_btn")
        Form_gourp_btn.resize(400, 300)
        Form_gourp_btn.setStyleSheet("#order_group_btn{\n"
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
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form_gourp_btn)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.order_group_btn = QtWidgets.QWidget(Form_gourp_btn)
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
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.plus_order_btn.setFont(font)
        self.plus_order_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plus_order_btn.setObjectName("plus_order_btn")
        self.horizontalLayout_2.addWidget(self.plus_order_btn)
        self.horizontalLayout_3.addWidget(self.widget)
        self.horizontalLayout.addWidget(self.order_group_btn, 0, QtCore.Qt.AlignTop)

        self.retranslateUi(Form_gourp_btn)
        QtCore.QMetaObject.connectSlotsByName(Form_gourp_btn)

    def retranslateUi(self, Form_gourp_btn):
        _translate = QtCore.QCoreApplication.translate
        Form_gourp_btn.setWindowTitle(_translate("Form_gourp_btn", "Form"))
        self.minus_order_btn.setText(_translate("Form_gourp_btn", "-"))
        self.label.setText(_translate("Form_gourp_btn", "1"))
        self.plus_order_btn.setText(_translate("Form_gourp_btn", "+"))
import ui.resource_rc
