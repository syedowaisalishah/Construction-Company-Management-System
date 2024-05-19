


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def openforms1(self):
        from fifteen1 import Ui_Form
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()
    def openforms2(self):
        from eleven import Ui_Form
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def openforms4(self):
        from first1 import Ui_MainWindow
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(631, 451)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 641, 451))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(-20, -10, 661, 461))
        self.label.setStyleSheet("border-image: url(C:/Users/F I ENTERPRISES/Documents/ise project/ise project 2k22/login.jpeg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(180, 20, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAcceptDrops(False)
        self.label_4.setStyleSheet("color:rgba(79, 90, 102)")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(80, 120, 201, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 120, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(90, 280, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(49)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("image: url(C:/Users/F I ENTERPRISES/Documents/ise project/ise project 2k22/contractor.jpeg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(340, 270, 251, 230))
        self.label_3.setStyleSheet("image: url(C:/Users/F I ENTERPRISES/Documents/ise project/ise project 2k22/architect.jpeg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 10, 101, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton.clicked.connect(self.openforms1)
        self.pushButton.clicked.connect(Form.close)
        self.pushButton_2.clicked.connect(self.openforms2)
        self.pushButton_2.clicked.connect(Form.close)
        self.pushButton_3.clicked.connect(self.openforms4)
        self.pushButton_3.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\">Check Deetails</p><p align=\"center\"><br/></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Client Requirement"))
        self.pushButton_2.setText(_translate("Form", " Report"))
        self.pushButton_3.setText(_translate("Form", "LOGOUT"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
