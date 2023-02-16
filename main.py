import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import widgetMain as widgetMain
from node.node import Node
from node.image.image import Image
from node.delay.delay import Delay
from node.start.start import Start
from node.position.position import Position
from keyboardGestion import KeyboardGestion
import threading
import bots
import random
import json
import webbrowser


class Interface(QWidget):

    keyPressed = pyqtSignal(QEvent)

    def __init__(self, *args):

        super(Interface, self).__init__(*args)

        self.setGeometry(200, 200, 2000, 1200)

        self.setWindowTitle('Bot manager')
        self.ui= widgetMain.Ui_Form()
        self.ui.setupUi(self)
        self.path = "/"
        self.keyboard = KeyboardGestion(app, self)
        self.numeroImage = 0

        self.mouseClickPosition = None
        self.selectionne = None
        self.selections = []
        self.listNodes = [Node(self, self, id=0)]
        self.AddingNode = Image
        self.listNodes[0].setChild(Start(self.listNodes[0], self.listNodes[0]), self.keyboard)

        self.linkTrace = False
        self.fenetreTouch = None
        self.pointTouch = None

        self.setWindowIcon(QIcon("logo.png"))
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        #menu
        self.menuBar = QMenuBar()
        self.fileMenu = QMenu("File")
        self.menuBar.addMenu(self.fileMenu)
        self.layout.setMenuBar(self.menuBar)
        #actions du menu
        self.fileMenu.addAction("Save", self.Save)
        self.fileMenu.addAction("Load", self.Load)
        self.fileMenu.addAction("New", self.NewProject)
        self.menuBar.addAction("GitHub", lambda : webbrowser.open("https://github.com/leteemo"))

        for interface in self.listNodes:
            interface.lower()


    def setFenetreTouch(self, fenetre):
        self.fenetreTouch = fenetre

    def setPointTrace(self, fenetre, node):
        self.fenetreTouch = fenetre
        self.pointTouch = node

    def getFenetreTouch(self):
        return self.fenetreTouch

    def getPointTouch(self):
        return self.pointTouch

    def getLinkTrace(self):
        return self.linkTrace

    def setLinkTrace(self, val):
        self.linkTrace = val

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setPen(Qt.red)
        if( self.pointTouch != None and self.fenetreTouch != None):

            point1 = QPoint(self.pointTouch.x() + self.fenetreTouch.x(), self.pointTouch.y() + self.fenetreTouch.y())
            point2 = QCursor.pos() - QPoint(0, 25) - self.pos()
            coords = [point1, point2]
            painter.drawPolyline(QPolygon(coords))

        #pour tous les noeuds crees dans le projet
        for interface in self.listNodes:

            #on verifie les connection
            if interface.getNext() != None:
                try:
                    pointInterface1 = interface
                    pointInterface2 = interface.getNext()
                    pointLabel1 = interface.ui.outputPoint
                    pointLabel2 = interface.getNext().ui.inputPoint
                    point1 = QPoint(pointInterface1.x() + pointLabel1.x(), pointInterface1.y() + pointLabel1.y())
                    point2 = QPoint(pointInterface2.x() + pointLabel2.x(), pointInterface2.y() + pointLabel2.y())
                    coords = [point1, point2]
                    #trace une simple ligne entre les 2 points
                    painter.drawPolyline(QPolygon(coords))
                except:
                    pass

        self.update()

    #remet la couleur initial du point a rouge
    def resetPoint(self):
        for interface in self.selections:
            if(interface.id != 0):
                interface.ui.inputPoint.setStyleSheet("\n""background-color: rgb(255, 0, 0);")
            interface.ui.outputPoint.setStyleSheet("\n""background-color: rgb(255, 0, 0);")


    def selectEntry(self, Node):

        #met la couleur du point a vert
        if(len(self.selections) == 0):
            self.selections.append(Node)
            Node.ui.outputPoint.setStyleSheet("\n""background-color: rgb(0, 255, 0);")
        else:
            self.selections = []
            self.selectCancel()


    def selectOutput(self, Node):

        if(Node.getId() != 0 and len(self.selections) == 1):
            self.selections.append(Node)
            self.selections[0].addNext(self.selections[1])
            self.resetPoint()
            self.selections = []

        else:
            self.selections = []
            self.selectCancel()

    def selectCancel(self):
        self.resetPoint()
        self.selections = []

    def deleteInputLink(self, node):
        node.setNext(None)

    def deleteOutputLink(self, node):
        node.addPrevious([])

    def nodePress(self, event, fenetreTouch):
        self.setFenetreTouch(fenetreTouch)
        if(self.fenetreTouch != None and self.pointTouch == None):
            self.mouseClickPosition = QPoint(event.x()+10, event.y()+10)


    def mouseMoveEvent(self, event):

        if(self.fenetreTouch != None and self.pointTouch == None):
            self.fenetreTouch.move(QPoint(event.x(), event.y())-self.mouseClickPosition)


    def checkButton(self, message="None"):
        self.ui.pushButton.setChecked(True)
        self.ui.pushButton.setText(message)

    def uncheckButton(self, message="None"):
        self.ui.pushButton.setChecked(False)
        self.ui.pushButton.setText(message)

    #appel clavier hors zone text
    def keyPressEvent(self, event):
        super(Interface, self).keyPressEvent(event)
        if event.key() == Qt.Key_X:
            if self.selectionne != None and self.selectionne.getId() != 0:
                index = self.listNodes.index(self.selectionne)
                for node in self.listNodes[index].getPrevious():
                    node.addPrevious([])
                    node.setNext(None)
                self.listNodes[index].deleteLater()
                self.listNodes.pop(index)
                self.selectionne = None

        if event.key() == Qt.Key_H:
            self.verification()

        self.keyPressed.emit(event)

    def NewProject(self):
        self.clearAllNode()
        self.listNodes.append(Node(self, self, id=len(self.listNodes), coords=[0, 0]))
        self.listNodes[-1].setChild(Start(self.listNodes[-1], self.listNodes[-1]), self.keyboard)
        self.listNodes[-1].lower()
        self.listNodes[-1].show()


    def clearAllNode(self):
        for node in self.listNodes:
            node.deleteLater()
            self.update()
        self.listNodes = []

    #quand le bouton est appuye
    def Start(self):

        if self.ui.pushButton.isChecked():
            self.ui.pushButton.setText("STOP")
            bots.Bot._arret = False
            self.listNodes[0].run()

        else:
            self.ui.pushButton.setText("START")
            bots.Bot._arret = True


    def newNode(self, ev=None):
        pos = [int(random.randrange(-5, 5))*10+400, int(random.randrange(-5, 5))*10]
        self.listNodes.append(Node(self, self, id=len(self.listNodes), coords=pos))
        self.listNodes[-1].setChild(self.AddingNode(self.listNodes[-1], self.listNodes[-1]), self.keyboard)
        self.listNodes[-1].lower()
        self.listNodes[-1].show()


    def getNodeById(self, id):
        for node in self.listNodes:
            if node.getId() == id:
                return node


    def loadNextAll(self, data):
        for i in data:
            node = self.getNodeById(int(i))
            if(data[str(i)]["next"] != None):
                next = self.getNodeById(int(data[str(i)]["next"]))
                node.addNext(next)


    def createListNodes(self, data):
        listeNodes = []
        for i in data:
            classChild = self.str_to_class(data[str(i)]["class"])
            pos = data[str(i)]["location"]
            input = data[str(i)]["input"]
            listeNodes.append(Node(self, self, id=int(i), coords=pos))
            listeNodes[-1].setChild(classChild(listeNodes[-1], listeNodes[-1]), self.keyboard)
            listeNodes[-1].child.loadData(input)

        return listeNodes


    def Load(self):
        frame = QFileDialog.getOpenFileName(self, "Open File", "", "JSON File (*.json)")
        if len(frame[0]) > 0:

            self.clearAllNode()

            with open(frame[0]) as json_file:
                data = json.load(json_file)
            listeNodes = self.createListNodes(data)

            for node in listeNodes:
                node.child.loadData(None)
                self.listNodes.append(node)
                node.lower()
                node.show()
            self.loadNextAll(data)


    def Save(self):
        filename, _ = QFileDialog.getSaveFileName()

        if filename:
            f = open(filename, "w")
            data = {}
            n = 0
            for node in self.listNodes:
                next = lambda x: None if x == None else node.getNext().getId()
                data[n] = ({"location": [node.x()-200, node.y()-250] , "next": next(node.getNext()), "input": node.child.getInput(), "class": str(node.child.getClassName())})
                n += 1

            data = json.dumps(data)
            f.write(data)
            f.close()

    def setNode(self):
        node = self.ui.box.currentText()
        self.AddingNode = self.str_to_class(node)

    def closeEvent(self, e):
        bots.Bot._arret = True

    def str_to_class(self, classname):
        return getattr(sys.modules[__name__], classname)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = Interface()
    w.show()
    sys.exit(app.exec_())
    detect_key_press()
