from email.message import EmailMessage
import ssl
import smtplib
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def open(self):
        from nine2 import Ui_Form
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def back(self):
        from seven1 import Ui_Form
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()
    def email(self):
        email_sender = 'alishahowais@gmail.com'
        email_password = 'yocntkcliuilosrj'
        email_reciver = self.lineEdit.text()
        subject = "new client requirement "
        body =str(self.lineEdit_2.text())
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_reciver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_reciver, em.as_string())

    def email1(self):
        email_sender = 'alishahowais@gmail.com'
        email_password = 'yocntkcliuilosrj'
        email_reciver = self.lineEdit_4.text()
        subject = "new client requirement"
        body = str( self.lineEdit_3.text())

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_reciver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_reciver, em.as_string())
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(521, 501)
        Form.setMaximumSize(QtCore.QSize(598, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-10, 0, 551, 600))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 0, 541, 501))
        self.label.setMaximumSize(QtCore.QSize(541, 501))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(C:/Users/F I ENTERPRISES/Documents/ise project/ise project 2k22/login.jpeg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 190, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.email)

        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(150, 60, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(170, 300, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(180, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 100, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 140, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 390, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 340, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setGeometry(QtCore.QRect(200, 440, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_4.clicked.connect(Form.close)
        self.pushButton_7.clicked.connect(self.email1)

        self.pushButton_4.clicked.connect(self.back)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_3.setText(_translate("Form", "Send"))
        self.pushButton_4.setText(_translate("Form", "BACK"))
        self.label_6.setText(_translate("Form", "FOR CONTRACTOR"))
        self.label_9.setText(_translate("Form", "FOR ARCHITECT"))
        self.lineEdit.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Form", "EMAIL-ID"))
        self.lineEdit_2.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "WRITE..."))
        self.lineEdit_3.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "WRITE..."))
        self.lineEdit_4.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "EMAIL-ID"))
        self.pushButton_7.setText(_translate("Form", "Send"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
