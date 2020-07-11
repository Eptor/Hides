# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designer_Files\decrypt_menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_decrypt_menu(object):
    def setupUi(self, decrypt_menu):
        decrypt_menu.setObjectName("decrypt_menu")
        decrypt_menu.resize(641, 126)
        self.centralwidget = QtWidgets.QWidget(decrypt_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.unzip_file_search = QtWidgets.QPushButton(self.centralwidget)
        self.unzip_file_search.setGeometry(QtCore.QRect(534, 10, 101, 23))
        self.unzip_file_search.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("Designer_Files\\../Icons/zip-file-search.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.unzip_file_search.setIcon(icon)
        self.unzip_file_search.setObjectName("unzip_file_search")
        self.unzip_file = QtWidgets.QLineEdit(self.centralwidget)
        self.unzip_file.setGeometry(QtCore.QRect(10, 10, 511, 21))
        self.unzip_file.setReadOnly(True)
        self.unzip_file.setObjectName("unzip_file")
        self.output_dir_search = QtWidgets.QPushButton(self.centralwidget)
        self.output_dir_search.setGeometry(QtCore.QRect(534, 50, 101, 23))
        self.output_dir_search.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("Designer_Files\\../Icons/folder-search.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.output_dir_search.setIcon(icon1)
        self.output_dir_search.setObjectName("output_dir_search")
        self.output_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.output_dir.setGeometry(QtCore.QRect(10, 50, 511, 21))
        self.output_dir.setReadOnly(True)
        self.output_dir.setObjectName("output_dir")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(10, 80, 621, 41))
        self.start.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("Designer_Files\\../Icons/terminal.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.start.setIcon(icon2)
        self.start.setObjectName("start")
        decrypt_menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(decrypt_menu)
        QtCore.QMetaObject.connectSlotsByName(decrypt_menu)

    def retranslateUi(self, decrypt_menu):
        _translate = QtCore.QCoreApplication.translate
        decrypt_menu.setWindowTitle(
            _translate("decrypt_menu", "Hides - The files hider")
        )
        self.unzip_file.setPlaceholderText(
            _translate("decrypt_menu", "Secret File")
        )
        self.output_dir.setPlaceholderText(
            _translate("decrypt_menu", "Output directory")
        )
