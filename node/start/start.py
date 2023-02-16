from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import node.start.widgetStart as widgetStart
from node.base import BaseNode
import threading
import os
import bots


class Start(BaseNode, QWidget):

    def __init__(self, parent, *args, file=None, size=[130, 100]):

        super(QWidget, self).__init__(*args)

        self.setAcceptDrops(True)
        self.setGeometry(10, 10, size[0], size[1])
        self.ui= widgetStart.Ui_Form()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.mLabel.mousePressEvent = parent.nodePress
        self.bot = bots.Bot(delay=1, parent=self)
        self.fileRep = file


    def getClassName(self):
        return "Start"
