from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import node.keyboard.widgetKeyboard as widgetKeyboard
from node.base import BaseNode
import threading
import os
import bots


class Keyboard(BaseNode, QWidget):

    def __init__(self, parent, *args, size=[130, 100]):

        super(QWidget, self).__init__(*args)

        self.setAcceptDrops(True)
        self.setGeometry(10, 10, size[0], size[1])
        self.ui= widgetKeyboard.Ui_Form()
        self.ui.setupUi(self)
        self.bot = bots.Bot(parent=self, type="Keyboard")
        self.parent = parent
        self.ui.textBoxText.textChanged.connect(self.change)
        self.ui.textBoxText.mousePressEvent = self.setSelect

        self.ui.textBoxDelay.textChanged.connect(self.change)
        self.ui.textBoxDelay.mousePressEvent = self.setSelect

        self.ui.mLabel.mousePressEvent = self.nodePress
        self.selected = False

    def nodePress(self, event):
        self.parent.nodePress(event)
        self.setSelect(selected=False)

    def setSelect(self, event=None, selected=True):
        if selected==True:
            self.parent.nodePress(event=None)

        try:
            self.ui.textBoxText.setReadOnly(not selected)
            self.ui.textBoxDelay.setReadOnly(not selected)
        except:
            pass

        self.selected = selected


    def getClassName(self):
        return "Keyboard"


    def change(self):
        self.ui.textBoxText.deselect()
        self.ui.textBoxDelay.deselect()
        try:
            self.bot.setData([self.ui.textBoxText.text(), self.ui.textBoxDelay.text()])

        except:
            pass
