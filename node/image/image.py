from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import node.image.widgetImage as widgetImage
from node.base import BaseNode
import threading
import os
import bots


class Image(BaseNode, QWidget):

    def __init__(self, parent, *args, size=[130, 100]):

        super(QWidget, self).__init__(*args)

        self.setAcceptDrops(True)
        self.setGeometry(10, 10, size[0], size[1])
        self.ui= widgetImage.Ui_Form()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.mLabel.mousePressEvent = parent.nodePress
        self.bot = bots.Bot(delay=1, parent=self)
        self.fileRep = None


    def getClassName(self):
        return "Image"

    def loadData(self, extra=None):
        if extra != None:
            self.fileRep = extra
        if self.fileRep != None:
            self.LoadFiles(nom=self.fileRep)
            self.bot.setFile(self.fileRep)

    def getInput(self):
        return self.fileRep

    def getFileRep(self):
        return self.fileRep


    def LoadFiles(self, nom):

        self.px = QPixmap(nom)
        self.px = self.px.scaled(self.ui.mLabel.width(),self.ui.mLabel.height())
        self.ui.mLabel.setPixmap(self.px)

    def dragEnterEvent(self, e):
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):

        files = [u.toLocalFile() for u in e.mimeData().urls()]
        for f in files:
            f = f.replace("/", "\\")
            self.fileRep = 'img\\' + os.path.basename(f)
            commande = 'copy "' + f + '" ' + self.fileRep
            os.system(commande)
            self.loadData()
