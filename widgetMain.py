from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(1000, 600)
        self.form = Form



        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 50, 140, 25))
        self.pushButton.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")

        self.buttonNew = QtWidgets.QPushButton(Form)
        self.buttonNew.setGeometry(QtCore.QRect(30, 100, 140, 25))
        self.buttonNew.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.buttonNew.setObjectName("buttonNew")


        self.box = QtWidgets.QComboBox(Form)
        self.box.addItems(["Image", "Delay", "Position"])
        self.box.setGeometry(QtCore.QRect(30, 130, 140, 25))

        # There is an alternate signal to send the text.
        self.box.currentTextChanged.connect( Form.setNode )


        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.Start)
        self.buttonNew.clicked.connect(Form.newNode)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Bot Manager", "Bot Manager"))
        self.pushButton.setText(_translate("Form", "START"))
        self.buttonNew.setText(_translate("Form", "NEW"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
