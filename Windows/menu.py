# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designer_Files\menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

menu_icon = "Icons/favicon.ico"

class Ui_choose_menu(object):
    def setupUi(self, choose_menu):
        choose_menu.setObjectName("choose_menu")
        choose_menu.resize(231, 61)
        choose_menu.setWindowIcon(QtGui.QIcon(menu_icon))
        self.centralwidget = QtWidgets.QWidget(choose_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.encrypt_button = QtWidgets.QPushButton(self.centralwidget)
        self.encrypt_button.setGeometry(QtCore.QRect(10, 10, 101, 41))
        self.encrypt_button.setObjectName("encrypt_button")
        self.decrypt_button = QtWidgets.QPushButton(self.centralwidget)
        self.decrypt_button.setGeometry(QtCore.QRect(120, 10, 101, 41))
        self.decrypt_button.setObjectName("decrypt_button")
        choose_menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(choose_menu)
        QtCore.QMetaObject.connectSlotsByName(choose_menu)

    def retranslateUi(self, choose_menu):
        _translate = QtCore.QCoreApplication.translate
        choose_menu.setWindowTitle(_translate("choose_menu", "Hides"))
        self.encrypt_button.setText(_translate("choose_menu", "Encrypt"))
        self.decrypt_button.setText(_translate("choose_menu", "Decrypt"))
