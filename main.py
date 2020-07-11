from Defs.functions import *
from Windows import menu

class menu_class(QMainWindow, menu.Ui_choose_menu):

    """ Encryption window handling """

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.encrypt_button.clicked.connect(self.enc)
        self.decrypt_button.clicked.connect(self.dec)

    def enc(self):
        self.enc_window = encrypt_class()
        self.enc_window.show()
        self.close()

    def dec(self):
        self.dec_window = decrypt_class()
        self.dec_window.show()
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app.setStyleSheet(open("style.css").read())
    menu = menu_class()
    menu.show()
    sys.exit(app.exec_())
