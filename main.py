# Local imports
from Windows import encrypt_menu
from Defs.defs import *

# Vanilla imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
import sys
from os import system
from pathlib import Path


# Icons (Grabbed from StreamLineIcons)
ok_zip = "Icons/zip-file-check.png"
wait_zip = "Icons/zip-file-clock"
error_zip = "Icons/zip-file-disable.png"

# Date variables
current_date = date.today()
day = fecha_actual.strftime("%d")
month = fecha_actual.strftime("%m")
year = fecha_actual.strftime("%y")
today = f"{dia}_{mes}_{año}"

filename = f"{today}.zip"

def popup(icon, text, title):
    msg = QMessageBox()
    msg.setWindowIcon(QtGui.QIcon(icon))
    # msg.setWindowIcon(QtGui.QIcon(icono))
    msg.setText(text)
    msg.setWindowTitle(title)
    msg.exec_()


class encrypt_class(QMainWindow, encrypt_menu.Ui_encrypt_menu):

    """ Maneja el popup para añadir empleados """

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.search_folder.clicked.connect(self.folder_lookup)
        self.search_image.clicked.connect(self.original)
        self.search_location.clicked.connect(self.location)
        self.start.clicked.connect(self.hide)

    def folder_lookup(self):
        directory = str(
            QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        )
        files = get_file_to_zip(directory)

        for file in files:
            self.files_list.addItem(str(Path(file)))

    def original(self):
        self.pic = QtWidgets.QFileDialog.getOpenFileName(self, "Select image")[0]
        self.original_img.setText(self.pic)

    def location(self):
        self.directory = str(
            QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        )
        self.new_location.setText(self.directory)

    def hide(self):
        try:
            popup(wait_zip, "Your window will freeze while the files are being hiden, everything is ok.", "Starting")
            zipall(filename ,self.pic, self.directory, self.new_name.text())

        except Exception as e:
            popup(error_zip, "The process failed, we are deleting the zip.", "Error")

        else:
            popup(ok_zip, "Files successfully hiden.", "Complete")

        finally:
            self.files_list.clear()
            system(f"del {filename}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    # app.setStyleSheet(open("style.css").read())
    gui = encrypt_class()
    gui.show()
    sys.exit(app.exec_())
