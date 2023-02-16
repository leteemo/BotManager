from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(130, 100)

        self.centralwidget = QtWidgets.QWidget(Form)

        self.mLabel = QtWidgets.QLabel(Form)
        self.mLabel.setGeometry(QtCore.QRect(0, 0, 130, 100))
        self.mLabel.setStyleSheet("\n""border: 1px solid black; background-color:rgba(150, 100, 100, 200);")
        self.mLabel.setText("Drag and Drop Image")
        self.mLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mLabel.setObjectName("mLabel")


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
