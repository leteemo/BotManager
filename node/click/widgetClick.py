from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(130, 100)
        
        self.mLabel = QtWidgets.QLabel(Form)
        self.mLabel.setGeometry(QtCore.QRect(0, 0, 130, 100))
        self.mLabel.setStyleSheet("\n""border: 1px solid black; background-color:rgba(150, 100, 100, 200);")
        self.mLabel.setText("")
        self.mLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mLabel.setObjectName("mLabel")

        self.layout = QtWidgets.QGridLayout(Form)

        self.radiobutton1 = QtWidgets.QRadioButton("right click")
        self.radiobutton1.data = "right"
        self.layout.addWidget(self.radiobutton1, 0, 0)

        self.radiobutton2 = QtWidgets.QRadioButton("left click")
        self.radiobutton2.data = "left"
        self.layout.addWidget(self.radiobutton2, 1, 0)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
