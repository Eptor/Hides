# Local imports
from Windows import encrypt_menu
from Defs.defs import *

# Vanilla imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
import sys
from pathlib import Path

def popup(texto, titulo):
    msg = QMessageBox()
    # msg.setWindowIcon(QtGui.QIcon(icono))
    msg.setText(texto)
    msg.setWindowTitle(titulo)
    msg.exec_()


class encrypt_class(QMainWindow, encrypt_menu.Ui_encrypt_menu):

    """ Maneja el popup para añadir empleados """

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.search_folder.clicked.connect(self.folder_lookup)
        self.search_image.clicked.connect(self.original)
        self.seach_location.clicked.connect(self.location)
        self.start.clicked.connect(self.hide)

    def folder_lookup(self):
        directory = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        files = get_file_to_zip(directory)

        for file in files:
            self.files_list.addItem(str(Path(file)))

    def original(self):
        self.pic = QtWidgets.QFileDialog.getOpenFileName(self, "Select image")[0]
        self.original_img.setText(self.pic)

    def location(self):
        self.directory = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.new_location.setText(self.directory)

    def hide(self):
        zipall(self.pic, self.directory, self.new_name.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    # app.setStyleSheet(open("style.css").read())
    gui = encrypt_class()
    gui.show()
    sys.exit(app.exec_())
