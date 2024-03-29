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
        self.textBoxX = QtWidgets.QLineEdit(Form)
        self.textBoxX.setGeometry(QtCore.QRect(10, 20, 110, 25))
        self.textBoxX.setPlaceholderText('Position X')
        self.textBoxX.setStyleSheet(style_sheet)

        self.textBoxY = QtWidgets.QLineEdit(Form)
        self.textBoxY.setGeometry(QtCore.QRect(10, 50, 110, 25))
        self.textBoxY.setPlaceholderText('Position Y')
        self.textBoxY.setStyleSheet(style_sheet)
