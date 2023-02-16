from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import node.delay.widgetDelay as widgetDelay
from node.base import BaseNode
import threading
import os
import bots
from time import sleep



class Delay(BaseNode, QWidget):

    def __init__(self, parent, *args, file=None, size=[130, 100]):

        super(QWidget, self).__init__(*args)

        self.setGeometry(10, 10, size[0], size[1])
        self.ui= widgetDelay.Ui_Form()
        self.ui.setupUi(self)
        self.parent = parent
        self.selected = False


        self.bot = bots.Bot(delay=1, parent=self)
        self.parent = parent
        self.ui.textBox.textChanged.connect(self.change)
        self.ui.textBox.mousePressEvent = self.setSelect
        self.ui.mLabel.mousePressEvent = self.nodePress
        self.selected = False

    def nodePress(self, event):
        self.parent.nodePress(event)
        self.setSelect(selected=False)

    def setSelect(self, event=None, selected=True):
        if selected==True:
            self.parent.nodePress(event=None)

        try:
            self.ui.textBox.setReadOnly(not selected)
        except:
            pass

        self.selected = selected

    def loadData(self, extra):
        if extra != None:
            self.ui.textBox.setText(extra)

    def getInput(self):
        return self.ui.textBox.text()

    def getClassName(self):
        return "Delay"

    def change(self):
        self.ui.textBox.deselect()
        try:
            delay = float(self.ui.textBox.text())
            self.bot.setDelay(delay)

        except:
            self.bot.setDelay(1)
