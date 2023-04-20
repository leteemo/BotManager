from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(130, 100)

        self.centralwidget = QtWidgets.QWidget(Form)

        self.mLabel = QtWidgets.QLabel(Form)
        self.mLabel.setGeometry(QtCore.QRect(0, 0, 130, 100))
        self.mLabel.setStyleSheet("\n""border: 1px solid black; background-color: rgba(100, 150, 100, 200);")
        self.mLabel.setText("")
        self.mLabel.setObjectName("mLabel")


        style_sheet = "QLineEdit { background-color: white; color: gray; }"
        self.textBoxText = QtWidgets.QLineEdit(Form)
        self.textBoxText.setGeometry(QtCore.QRect(10, 20, 110, 25))
        self.textBoxText.setPlaceholderText('Text')
        self.textBoxText.setStyleSheet(style_sheet)

        self.textBoxDelay = QtWidgets.QLineEdit(Form)
        self.textBoxDelay.setGeometry(QtCore.QRect(10, 50, 110, 25))
        self.textBoxDelay.setPlaceholderText('Delay for each letter')
        self.textBoxDelay.setStyleSheet(style_sheet)
