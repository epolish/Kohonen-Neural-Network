import sys
from classes.MainForm import *
from PyQt5.QtWidgets import QApplication, QDialog

def main():
    app = QApplication(sys.argv)
    dialog = QDialog()
    ui = MainForm()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()