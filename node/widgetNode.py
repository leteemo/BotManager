from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(150, 120)

        self.centralwidget = QtWidgets.QWidget(Form)

        self.mLabel = QtWidgets.QLabel(Form)
        self.mLabel.setGeometry(QtCore.QRect(0, 0, 150, 120))
        self.mLabel.setStyleSheet("\n""border: 1px solid black; background-color: rgba(100, 100, 100, 200);")
        self.mLabel.setText("")
        self.mLabel.setObjectName("mLabel")

        self.inputPoint = QtWidgets.QLabel(Form)
        self.inputPoint.setGeometry(QtCore.QRect(0, 55, 10, 10))
        self.inputPoint.setStyleSheet("\n""background-color: rgb(255, 0, 0);")
        self.inputPoint.setText("")
        self.inputPoint.setObjectName("mLabel")

        self.outputPoint = QtWidgets.QLabel(Form)
        self.outputPoint.setGeometry(QtCore.QRect(140, 55, 10, 10))
        self.outputPoint.setStyleSheet("\n""background-color: rgb(255, 0, 0);")
        self.outputPoint.setText("")
        self.outputPoint.setObjectName("mLabel")
