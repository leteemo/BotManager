from PyQt5.QtWidgets import *

class BaseNode():

    def setSelect(self, event=None, selected=True):
        self.selected = selected

    def getFileRep(self):
        return None

    def setKeyboard(self, keyboard):
        self.keyboard = keyboard

    def getKeyboard(self):
        return self.keyboard

    def getClassName(self):
        return "None"

    def getBot(self):
        return self.bot

    def loadData(self, extra=None):
        return None

    def getInput(self):
        return None
