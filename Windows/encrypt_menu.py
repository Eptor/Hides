# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designer_Files\encrypt_menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_encrypt_menu(object):
    def setupUi(self, encrypt_menu):
        encrypt_menu.setObjectName("encrypt_menu")
        encrypt_menu.setEnabled(True)
        encrypt_menu.resize(665, 271)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("Designer_Files\\../Icons/favicon.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        encrypt_menu.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(encrypt_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.files_list = QtWidgets.QListWidget(self.centralwidget)
        self.files_list.setGeometry(QtCore.QRect(10, 10, 321, 211))
        self.files_list.setObjectName("files_list")
        self.search_folder = QtWidgets.QPushButton(self.centralwidget)
        self.search_folder.setGeometry(QtCore.QRect(10, 230, 321, 31))
        self.search_folder.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("Designer_Files\\../Icons/folder-search.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.search_folder.setIcon(icon1)
        self.search_folder.setObjectName("search_folder")
        self.original_img = QtWidgets.QLineEdit(self.centralwidget)
        self.original_img.setEnabled(True)
        self.original_img.setGeometry(QtCore.QRect(350, 30, 221, 21))
        self.original_img.setReadOnly(True)
        self.original_img.setObjectName("original_img")
        self.original_img_label = QtWidgets.QLabel(self.centralwidget)
        self.original_img_label.setGeometry(QtCore.QRect(350, 10, 221, 16))
        self.original_img_label.setObjectName("original_img_label")
        self.search_image = QtWidgets.QPushButton(self.centralwidget)
        self.search_image.setGeometry(QtCore.QRect(580, 30, 75, 23))
        self.search_image.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("Designer_Files\\../Icons/image-file-search.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.search_image.setIcon(icon2)
        self.search_image.setObjectName("search_image")
        self.new_name_label = QtWidgets.QLabel(self.centralwidget)
        self.new_name_label.setGeometry(QtCore.QRect(350, 110, 221, 16))
        self.new_name_label.setObjectName("new_name_label")
        self.new_name = QtWidgets.QLineEdit(self.centralwidget)
        self.new_name.setEnabled(True)
        self.new_name.setGeometry(QtCore.QRect(350, 130, 301, 21))
        self.new_name.setReadOnly(False)
        self.new_name.setObjectName("new_name")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(350, 200, 301, 61))
        self.start.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap("Designer_Files\\../Icons/terminal.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.start.setIcon(icon3)
        self.start.setObjectName("start")
        self.new_location_label = QtWidgets.QLabel(self.centralwidget)
        self.new_location_label.setGeometry(QtCore.QRect(350, 60, 221, 16))
        self.new_location_label.setObjectName("new_location_label")
        self.new_location = QtWidgets.QLineEdit(self.centralwidget)
        self.new_location.setEnabled(True)
        self.new_location.setGeometry(QtCore.QRect(350, 80, 221, 21))
        self.new_location.setReadOnly(True)
        self.new_location.setObjectName("new_location")
        self.search_location = QtWidgets.QPushButton(self.centralwidget)
        self.search_location.setGeometry(QtCore.QRect(580, 80, 75, 23))
        self.search_location.setText("")
        self.search_location.setIcon(icon1)
        self.search_location.setObjectName("search_location")
        self.encrypt = QtWidgets.QCheckBox(self.centralwidget)
        self.encrypt.setGeometry(QtCore.QRect(470, 170, 70, 17))
        self.encrypt.setObjectName("encrypt")
        encrypt_menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(encrypt_menu)
        QtCore.QMetaObject.connectSlotsByName(encrypt_menu)

    def retranslateUi(self, encrypt_menu):
        _translate = QtCore.QCoreApplication.translate
        encrypt_menu.setWindowTitle(
            _translate("encrypt_menu", "Hides - El ocultador de archivos")
        )
        self.original_img_label.setText(
            _translate("encrypt_menu", "Foto original")
        )
        self.new_name_label.setText(
            _translate(
                "encrypt_menu", "Nombre del nuevo archivo (sin extension)"
            )
        )
        self.new_location_label.setText(
            _translate("encrypt_menu", "Directorio de destino")
        )
        self.encrypt.setText(_translate("encrypt_menu", "Encriptar"))
