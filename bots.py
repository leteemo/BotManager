from pynput.mouse import Button, Controller
from time import sleep
import keyboard
import pyautogui
import threading
import random

class Bot:

    _arret = False

    def __init__(self, parent=None, file=None, position=None, nextBot=None, delay=None, click=False):
        self.file = file
        self.position = position
        self.click = click
        self.precision = 0.7
        self.mouse = Controller()
        self.continuer = True
        self.nextBot = nextBot
        self.delay = delay
        self.keyboard = keyboard
        self.parent = parent

    def setNext(self, nextBot):
        self.nextBot = nextBot

    def getNext(self):
        return self.nextBot

    def getBot(self):
        return self

    def setDelay(self, delay):
        self.delay = delay

    def setPosition(self, coords):
        self.position = coords

    def setFile(self, file):
        self.file = file

    def getFile(self):
        return self.file

    def setCkick(self, click):
        self.click = click

    def persoImage(self):
        positions = pyautogui.locateCenterOnScreen(self.file,  confidence=self.precision)
        if(positions != None):
            arriere = (self.mouse.position[0], self.mouse.position[1])
            self.mouse.position = (positions[0], positions[1])

    def persoCoords(self):
        arriere = (self.mouse.position[0], self.mouse.position[1])
        self.mouse.position = (self.position[0], self.position[1])

    def run(self):
        if Bot._arret == True:
            quit()

        try:
            if(self.file != None):
                self.persoImage()

            elif(self.position != None):
                self.persoCoords()

            if self.click:
                self.mouse.press(Button.left)
                sleep(0.1)
                self.mouse.release(Button.left)

            if self.delay != None:
                sleep(self.delay)

        except Exception as e:
            print(e)

        if self.nextBot != None:
            threading.Thread(target=self.nextBot.run).start()

        else:
            self.parent.getKeyboard().stopBot()





#fin
