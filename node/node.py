import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import widgetMain as widgetMain
import node.widgetNode as widgetsNode

from node.position.position import Position
import threading
import keyboard
import bots




class Node(QWidget):

    def __init__(self, parent, *args, id, coords=[0, 0], file=None, child=None):

        super(Node, self).__init__(*args)
        self.setGeometry(300+coords[0], 250+coords[1], 150, 120)
        self.ui= widgetsNode.Ui_Form()
        self.ui.setupUi(self)
        self.parent = parent
        self.child = None
        self.previous = []
        self.next = None
        self.enterOnPoint = False
        self.bot = None

        self.ui.mLabel.mousePressEvent = self.nodePress
        self.ui.outputPoint.mousePressEvent = self.selectPoint
        self.ui.outputPoint.mouseReleaseEvent = self.selecOutputPoint
        self.ui.inputPoint.mousePressEvent = self.selectInputPoint
        parent.ui.form.mousePressEvent = self.deselectNone
        parent.ui.form.mouseReleaseEvent = self.deselectPoint

        self.id = id

        self.setRole()

    def setChild(self, child, keyboard):
        self.child = child
        self.bot = self.child.getBot()
        self.child.setKeyboard(keyboard)


    #cas particulier
    def setRole(self):
        if(self.id==0):
            self.ui.inputPoint.setStyleSheet("\n""background-color: rgba(0, 0, 0, 0);")


    def selectPoint(self, event):

        if event.button() == Qt.LeftButton:
            self.enterOnPoint = True
            self.parent.setPointTrace(self, self.ui.outputPoint)
            self.parent.selectEntry(self)

        if event.button() == Qt.RightButton:
            self.parent.deleteInputLink(self)


    def deselectPoint(self, event):
        if self.enterOnPoint == False:
            self.parent.selectCancel()
            self.parent.setPointTrace(None, None)


    def selecOutputPoint(self, event):

        self.enterOnPoint = False


    def selectInputPoint(self, event):
        if event.button() == Qt.LeftButton:
            self.parent.selectOutput(self)

        if event.button() == Qt.RightButton:
            self.parent.deleteOutputLink(self)


    def nodePress(self, event=None):

        if self.parent.selectionne !=None:
            try:
                self.parent.selectionne.ui.mLabel.setStyleSheet("\n""border: 1px solid black; background-color: rgba(100, 100, 100, 200);")
            except:
                pass

        self.ui.mLabel.setStyleSheet("\n""border: 1px solid red; background-color: rgba(100, 100, 100, 200);")
        self.parent.selectionne = self

        if event != None:
            if event.button() == Qt.LeftButton:
                self.parent.nodePress(event, self)


    def deselectNone(self, event):

        if self.parent.selectionne !=None:
            try:
                self.parent.selectionne.child.setSelect(selected=False)
                self.parent.selectionne.ui.mLabel.setStyleSheet("\n""border: 1px solid black; background-color: rgba(100, 100, 100, 200);")
            except:
                pass
        self.parent.selectionne = None

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id


    def getPrevious(self):
        return self.previous


    def setNext(self, next):
        if next != None and self.next != None:
            self.next.previous.append(self)
        elif self.next != None:
            self.next.previous = []

        if next != None and self.bot !=None:
            self.bot.setNext(next.child.bot)
        elif self.bot !=None:
            self.bot.setNext(None)

        self.next = next

    def getNext(self):
        return self.next

    def addPrevious(self, previous):
        if(previous != []):
            self.previous.next.append(previous)
            self.previous.append(previous)
        else:
            for prev in self.previous:
                prev.setNext(None)
            self.previous = []

    def getNext(self):
        return self.next

    def addNext(self, nextS):
        if self.next == None and nextS != self and nextS != None:
            self.setNext(nextS)
            self.next.previous.append(self)


    def run(self):

        if(not bots.Bot._arret):
            threading.Thread(target=self.child.bot.run).start()
            if(self.next==None):
                self.parent.uncheckButton("START")
        else:
            self.parent.uncheckButton("START")
