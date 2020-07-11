# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designer_Files\encrypt_menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

menu_icon = "Icons/favicon.ico"
search_folder_icon = "Icons/folder-search.png"
original_img_icon = "Icons/image-file-search.png"
terminal_icon = "Icons/terminal.png"


class Ui_encrypt_menu(object):
    def setupUi(self, encrypt_menu):
        encrypt_menu.setObjectName("encrypt_menu")
        encrypt_menu.setEnabled(True)
        encrypt_menu.resize(665, 271)
        encrypt_menu.setWindowIcon(QtGui.QIcon(menu_icon))
        self.centralwidget = QtWidgets.QWidget(encrypt_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.files_list = QtWidgets.QListWidget(self.centralwidget)
        self.files_list.setGeometry(QtCore.QRect(10, 10, 321, 211))
        self.files_list.setObjectName("files_list")
        self.search_folder = QtWidgets.QPushButton(self.centralwidget)
        self.search_folder.setIcon(QtGui.QIcon(search_folder_icon))
        self.search_folder.setGeometry(QtCore.QRect(10, 230, 321, 31))
        self.search_folder.setObjectName("search_folder")
        self.original_img = QtWidgets.QLineEdit(self.centralwidget)
        self.original_img.setEnabled(True)
        self.original_img.setGeometry(QtCore.QRect(350, 30, 221, 21))
        self.original_img.setReadOnly(True)
        self.original_img.setObjectName("original_img")
        self.original_img_label = QtWidgets.QLabel(self.centralwidget)
        self.original_img_label.setGeometry(QtCore.QRect(350, 10, 81, 16))
        self.original_img_label.setObjectName("original_img_label")
        self.search_image = QtWidgets.QPushButton(self.centralwidget)
        self.search_image.setIcon(QtGui.QIcon(original_img_icon))
        self.search_image.setGeometry(QtCore.QRect(580, 30, 75, 23))
        self.search_image.setObjectName("search_image")
        self.new_name_label = QtWidgets.QLabel(self.centralwidget)
        self.new_name_label.setGeometry(QtCore.QRect(350, 150, 111, 16))
        self.new_name_label.setObjectName("new_name_label")
        self.new_name = QtWidgets.QLineEdit(self.centralwidget)
        self.new_name.setGeometry(QtCore.QRect(350, 170, 301, 21))
        self.new_name.setObjectName("new_name")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setIcon(QtGui.QIcon(terminal_icon))
        self.start.setGeometry(QtCore.QRect(350, 200, 301, 61))
        self.start.setObjectName("start")
        self.new_location_label = QtWidgets.QLabel(self.centralwidget)
        self.new_location_label.setGeometry(QtCore.QRect(350, 80, 101, 16))
        self.new_location_label.setObjectName("new_location_label")
        self.new_location = QtWidgets.QLineEdit(self.centralwidget)
        self.new_location.setReadOnly(True)
        self.new_location.setGeometry(QtCore.QRect(350, 100, 221, 21))
        self.new_location.setObjectName("new_location")
        self.search_location = QtWidgets.QPushButton(self.centralwidget)
        self.search_location.setIcon(QtGui.QIcon(search_folder_icon))
        self.search_location.setGeometry(QtCore.QRect(580, 100, 75, 23))
        self.search_location.setObjectName("search_location")
        encrypt_menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(encrypt_menu)
        QtCore.QMetaObject.connectSlotsByName(encrypt_menu)

    def retranslateUi(self, encrypt_menu):
        _translate = QtCore.QCoreApplication.translate
        encrypt_menu.setWindowTitle(
            _translate("encrypt_menu", "Hides - El ocultador de archivos")
        )
        self.original_img_label.setText(_translate("encrypt_menu", "Imagen original"))
        self.new_name_label.setText(_translate("encrypt_menu", "Nombre del archivo"))
        self.new_location_label.setText(
            _translate("encrypt_menu", "Directorio de destino")
        )
