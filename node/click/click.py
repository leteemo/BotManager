from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import node.click.widgetClick as widgetClick
from node.base import BaseNode
import threading
import os
import bots


class Click(BaseNode, QWidget):

    def __init__(self, parent, *args, size=[130, 100]):

        super(QWidget, self).__init__(*args)

        self.setAcceptDrops(True)
        self.setGeometry(10, 10, size[0], size[1])
        self.ui= widgetClick.Ui_Form()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.mLabel.mousePressEvent = parent.nodePress
        self.ui.radiobutton1.toggled.connect(self.onClicked)
        self.ui.radiobutton2.toggled.connect(self.onClicked)
        self.bot = bots.Bot(parent=self, type="Click")

    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            print(radioButton.data)
            self.bot.setData(radioButton.data)


    def getClassName(self):
        return "Click"
