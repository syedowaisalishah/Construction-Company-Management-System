from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Formsss(object):
    def logout(self):
        from first1 import Ui_MainWindow
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
    def openformsss(self):
        from fives1 import Ui_Form
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()
    def eight(self):
        from eight1 import Ui_Form
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(631, 451)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 651, 451))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(-20, -10, 661, 471))
        self.label.setAcceptDrops(True)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("border-image: url(CC:/Users/F I ENTERPRISES/Documents/ise project/ise project 2k22/login.jpeg);")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(140, 70, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(79, 90, 102)")
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 140, 231, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 290, 300, 151))
        font = QtGui.QFont()
        font.setPointSize(49)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("image: url(C:/Users/F I ENTERPRISES\Documents/ise project/ise project 2k22/contractor.jpeg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(300, 270, 291, 191))
        self.label_3.setStyleSheet("image: url(C:/Users/F I ENTERPRISES\Documents/ise project/ise project 2k22/architect.jpeg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 0, 641, 71))
        self.textEdit_2.setAcceptDrops(True)
        self.textEdit_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(175, 176, 171);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 90, 101, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)


        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setGeometry(QtCore.QRect(450, 100, 181, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_4.clicked.connect(self.logout)
        self.pushButton_4.clicked.connect(Form.close)
        self.pushButton_3.clicked.connect(self.openformsss)
        self.pushButton_3.clicked.connect(Form.close)
        self.pushButton_7.clicked.connect(self.eight)
        self.pushButton_7.clicked.connect(Form.close)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Select What You Want:"))
        self.pushButton_3.setText(_translate("Form", "Construction and Architect"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#4f5a66;\">We Listen To Your Needs,Design it to your specification, and Built it to your Dreams.</span></p></body></html>"))
        self.pushButton_4.setText(_translate("Form", "LogOut"))

        self.pushButton_7.setText(_translate("Form", "meeting and payment"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Formsss()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
