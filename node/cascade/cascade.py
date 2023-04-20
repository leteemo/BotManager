from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import node.cascade.widgetCascade as widgetCascade
from node.base import BaseNode
import threading
import os
import bots


class Cascade(BaseNode, QWidget):

    def __init__(self, parent, *args, size=[130, 100]):

        super(QWidget, self).__init__(*args)

        self.setAcceptDrops(True)
        self.setGeometry(10, 10, size[0], size[1])
        self.ui= widgetCascade.Ui_Form()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.mLabel.mousePressEvent = parent.nodePress
        self.bot = bots.Bot(parent=self, type="Cascade")
        self.fileRep = None


    def getClassName(self):
        return "Cascade"

    def loadData(self, extra=None):
        if extra != None:
            self.fileRep = extra
        if self.fileRep != None:
            self.ui.mLabel.setStyleSheet("\n""border: 1px solid black; background-color:rgba(100, 150, 100, 200);")
            self.bot.setData(self.fileRep)

    def getInput(self):
        return self.fileRep

    def getFileRep(self):
        return self.fileRep



    def dragEnterEvent(self, e):
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):

        files = [u.toLocalFile() for u in e.mimeData().urls()]
        for f in files:
            f = f.replace("/", "\\")
            self.fileRep = 'cascade\\' + os.path.basename(f)
            commande = 'copy "' + f + '" ' + self.fileRep
            os.system(commande)
            self.loadData()
