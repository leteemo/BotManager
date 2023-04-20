from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import node.position.widgetPosition as widgetPosition
from node.base import BaseNode
import threading
import os
import bots
from time import sleep



class Position(BaseNode, QWidget):

    def __init__(self, parent, *args, file=None, size=[130, 100]):

        super(QWidget, self).__init__(*args)

        self.setGeometry(10, 10, size[0], size[1])
        self.ui= widgetPosition.Ui_Form()
        self.ui.setupUi(self)
        self.parent = parent
        self.selected = False

        self.bot = bots.Bot(parent=self, type="Position")
        self.parent = parent

        self.ui.textBoxX.textChanged.connect(self.change)
        self.ui.textBoxX.mousePressEvent = self.setSelect

        self.ui.textBoxY.textChanged.connect(self.change)
        self.ui.textBoxY.mousePressEvent = self.setSelect

        self.ui.mLabel.mousePressEvent = self.nodePress
        self.selected = False

    def nodePress(self, event):
        self.parent.nodePress(event)
        self.setSelect(selected=False)

    def setSelect(self, event=None, selected=True):
        if selected==True:
            self.parent.nodePress(event=None)

        try:
            self.ui.textBoxX.setReadOnly(not selected)
            self.ui.textBoxY.setReadOnly(not selected)
        except:
            pass

        self.selected = selected

    def loadData(self, extra):
        if extra != None:
            self.ui.textBoxX.setText(extra[0])
            self.ui.textBoxY.setText(extra[1])

    def getInput(self):
        return [self.ui.textBoxX.text(), self.ui.textBoxY.text()]

    def getClassName(self):
        return "Position"

    def change(self):
        self.ui.textBoxX.deselect()
        self.ui.textBoxY.deselect()
        try:
            coord = [float(self.ui.textBoxX.text()), float(self.ui.textBoxY.text())]
            self.bot.setData(coord)

        except:
            pass
