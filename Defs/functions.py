# Local imports
from Windows import encrypt_menu, decrypt_menu
from Defs.defs import *

# Vanilla imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
import sys
from os import system, path
from pathlib import Path


# Icons (Grabbed from StreamLineIcons)
ok_zip = "Icons/zip-file-check.png"
wait_zip = "Icons/zip-file-clock"
error_zip = "Icons/zip-file-disable.png"

# Date variables
current_date = date.today()
day = current_date.strftime("%d")
month = current_date.strftime("%m")
year = current_date.strftime("%y")
today = f"{day}_{month}_{year}"

filename = f"{today}.zip"


def popup(icon, text, title):
    msg = QMessageBox()
    msg.setWindowIcon(QtGui.QIcon(icon))
    msg.setText(text)
    msg.setWindowTitle(title)
    msg.exec_()


class encrypt_class(QMainWindow, encrypt_menu.Ui_encrypt_menu):

    """ Encryption window handling """

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.search_folder.clicked.connect(self.folder_lookup)
        self.search_image.clicked.connect(self.original)
        self.search_location.clicked.connect(self.location)
        self.start.clicked.connect(self.hide)

    def folder_lookup(self):
        """ Gets the path and the files of the directory to hide """
        directory = str(
            QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        )

        files = get_file_to_zip(directory)

        for file in files:
            self.files_list.addItem(str(Path(file)))  # Adds the files to the list

    def original(self):
        """ Gets the path for the photo used to hide the files """
        self.pic = QtWidgets.QFileDialog.getOpenFileName(self, "Select image")[0]
        self.original_img.setText(self.pic)

    def location(self):
        """ Gets the output directory for the picture with the hiden files"""
        self.directory = str(
            QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        )
        self.new_location.setText(self.directory)

    def hide(self):
        """ Hides the files """
        try:
            # Shows the popup indicating you have to wait
            popup(
                wait_zip,
                "Your window will freeze while the files are being hiden, everything is ok.",
                "Starting",
            )

            # Makes a zip file with all the files choosen by the user
            zipall(filename, self.pic, self.directory, self.new_name.text())

        except Exception as ಠ_ಠ:
            # In case of failure, notify it
            popup(error_zip, "The process failed, we are deleting the zip.", "Error")

        else:
            # In case of no flaws, notify it
            popup(ok_zip, "Files successfully hiden.", "Complete")

        finally:
            # Clear the list and delete the generated zip file
            self.files_list.clear()
            if path.isfile(filename):
                system(f"del {filename}")


class decrypt_class(QMainWindow, decrypt_menu.Ui_decrypt_menu):

    """ Decryption window handling """

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.unzip_file_search.clicked.connect(self.file)
        self.output_dir_search.clicked.connect(self.output)
        self.start.clicked.connect(self.reveal)

    def file(self):
        self.pic = QtWidgets.QFileDialog.getOpenFileName(self, "Select image")[0]

        self.unzip_file.setText(self.pic)

    def output(self):
        self.output = str(
            QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        )

        self.output_dir.setText(self.output)

    def reveal(self):
        try:
            popup(
                wait_zip,
                "Your window will freeze while the files are being revealed, everything is ok.",
                "Starting",
            )

            unzip(self.output, self.pic)
        except Exception as ಠ_ಠ:
            popup(error_zip, "An error has ocurred.", "Error")
        else:
            popup(ok_zip, "successfully revealed files.", "Complete")
