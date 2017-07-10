from classes.Programm import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MainForm(object):
    @property
    def programm(self):
        return self.__programm

    def __init__(self):
        self.__programm = Programm()
        self.__programm.file = None
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(260, 135)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 100, 90, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox.setGeometry(QtCore.QRect(150, 20, 90, 20))
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setProperty("value", 0.4)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 120, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 60, 90, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.pushButton_2Clicked)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 120, 20))
        self.label_3.setObjectName("label_3")
        self.file_dialog = QtWidgets.QFileDialog(Form)
        self.file_dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        self.file_dialog.setNameFilter("JSON files (*.json)")
        self.message_box = QtWidgets.QMessageBox()
        self.message_box.setIcon(QtWidgets.QMessageBox.Warning)
        self.message_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", u"Сеть Кохонена"))
        self.pushButton.setText(_translate("Form", "Результат"))
        self.label_2.setText(_translate("Form", "Коэффициент обучения"))
        self.pushButton_2.setText(_translate("Form", "Выбрать файл"))
        self.label_3.setText(_translate("Form", "Имя файла..."))
        self.message_box.setText(_translate("Form", "Вы не выбрали файл"))
        self.message_box.setWindowTitle(_translate("Form", "Предупреждение"))
        
    def pushButtonClicked(self, Form):
        if self.__programm.file == None:
            self.message_box.exec_()
        else:
            try:
                self.__programm.run(float(self.doubleSpinBox.text().replace(',', '.')))
            except Exception as ex:
                _translate = QtCore.QCoreApplication.translate
                self.message_box.setIcon(QtWidgets.QMessageBox.Critical)
                self.message_box.setText(_translate("Form", "Не корректный формат данных"))
                self.message_box.setWindowTitle(_translate("Form", "Ошибка"))
                self.message_box.exec_()
                
    def pushButton_2Clicked(self, Form):
        if self.file_dialog.exec_():
            filename = self.file_dialog.selectedFiles()[0]
            file = QtCore.QFile(filename)
            self.label_3.setText(QtCore.QFileInfo(file).fileName())
            self.__programm.file = file.fileName()