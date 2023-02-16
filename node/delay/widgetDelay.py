from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(130, 100)

        self.centralwidget = QtWidgets.QWidget(Form)


        self.mLabel = QtWidgets.QLabel(Form)
        self.mLabel.setGeometry(QtCore.QRect(0, 0, 130, 100))
        self.mLabel.setStyleSheet("\n""border: 1px solid black; background-color: rgba(100, 100, 150, 200);")
        self.mLabel.setText("")
        self.mLabel.setObjectName("mLabel")

        self.textBox = QtWidgets.QLineEdit(Form)
        self.textBox.setGeometry(QtCore.QRect(10, 40, 110, 25))
        self.mLabel.setObjectName("textBox")
