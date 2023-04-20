from pynput.mouse import Button, Controller
from time import sleep
import keyboard
import pyautogui
import threading
import random
from PIL import ImageGrab
import cv2 as cv
import numpy as np


class Bot:

    _arret = False

    def __init__(self, parent=None, nextBot=None, type=None, data=None):
        self.precision = 0.7
        self.mouse = Controller()
        self.continuer = True
        self.nextBot = nextBot
        self.data = data
        self.type = type
        self.parent = parent

    #seters et getters
    def setNext(self, nextBot):
        self.nextBot = nextBot

    def getNext(self):
        return self.nextBot

    def getBot(self):
        return self

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data


    #les différents types de bots

    def persoImage(self):
        positions = pyautogui.locateCenterOnScreen(self.data,  confidence=self.precision)
        if(positions != None):
            arriere = (self.mouse.position[0], self.mouse.position[1])
            self.mouse.position = (positions[0], positions[1])


    def persoCoords(self):
        arriere = (self.mouse.position[0], self.mouse.position[1])
        self.mouse.position = (self.data[0], self.data[1])


    def Cascade(self, file):
        frame = np.array(ImageGrab.grab())
        net = cv.CascadeClassifier(file)
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame_gray = cv.equalizeHist(frame_gray)
        detected = net.detectMultiScale3(frame_gray, outputRejectLevels=True)
        i = 0

        for (x,y,w,h) in detected[0]:

            center = (x + w//2, y + h//2)

            ROI = frame_gray[y:y+h, x:x+w]

            cv.imwrite("img/roi.jpg", ROI)

            arriere = (self.mouse.position[0], self.mouse.position[1])
            self.mouse.position = (center[0], center[1])
            sleep(1)


    def keyboard(self):
        print(self.data)
        for letter in self.data[0]:
            pyautogui.typewrite(letter)
            sleep(float(self.data[1]))

    def click(self):
        pyautogui.click(button=self.data)


    def run(self):
        if Bot._arret == True:
            quit()

        try:
            if(self.type == "Image"):
                self.persoImage()

            elif(self.type == "Position"):
                self.persoCoords()

            elif self.type == "Cascade":
                self.Cascade(self.data)

            elif self.type == "Keyboard":
                self.keyboard()

            elif self.type == "Delay":
                sleep(self.data)

            elif self.type == "Click":
                self.click()


        except Exception as e:
            print(e)

        if self.nextBot != None:
            threading.Thread(target=self.nextBot.run).start()

        else:
            self.parent.getKeyboard().stopBot()





#fin
