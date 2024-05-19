import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def openforms(self):
        from first1 import Ui_MainWindow
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
    def openformss(self):
        from third1 import Ui_Forms
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Forms()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def openformsss(self):
        from four2 import Ui_Formsss
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Formsss()
        self.ui.setupUi(self.Form)

        self.Form.show()

    def loginfunction(self):
        user = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if len(user) == 0 or len(password) == 0:
            self.error1.setText("Please input all fields.")

        else:
            try:

                conn = sqlite3.connect("register.db")
                cur = conn.cursor()
                query = 'SELECT password FROM reg WHERE username =\'' + user + "\'"
                cur.execute(query)
                result_pass = cur.fetchone()[0]
                if result_pass == password:
                    #self.pushButton_2.clicked.connect(Form.close)
                    self.pushButton_2.clicked.connect(self.openformsss)
                    self.pushButton_2.clicked.connect(Form.close)

                    #self.pushButton_2.clicked.connect(Form.close)
                else:
                    self.error1.setText("Invalid username or password")
            except:
                print("a")


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(517, 501)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, -1, 541, 511))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(-4, -1, 521, 501))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(C:/Users/F I ENTERPRISES/Documents/ise project/ise project 2k22/login.jpeg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(150, 80, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 160, 231, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgb(56, 73, 91);\n"
"padding-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 220, 231, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgbargb(54, 71, 89);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 310, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.loginfunction)
        #self.pushButton_2.clicked.connect(Form.close)


        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 370, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.openformss)
        self.pushButton_3.clicked.connect(Form.close)

        self.error1 = QtWidgets.QLabel(self.widget)
        self.error1.setGeometry(QtCore.QRect(110, 270, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.error1.setFont(font)
        self.error1.setStyleSheet("color: rgb(255, 0, 0);")
        self.error1.setText("")
        self.error1.setObjectName("error1")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_4.clicked.connect(self.openforms)
        #self.pushButton_4.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">SA ARCHITECT</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Form", "  User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Password"))
        self.pushButton_2.setText(_translate("Form", "L o g  I n"))
        self.pushButton_3.setText(_translate("Form", "Register Yourself"))
        self.pushButton_4.setText(_translate("Form", "BACK"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.setFixedHeight(501)
    Form.setFixedWidth(517)

    Form.show()
    sys.exit(app.exec_())
