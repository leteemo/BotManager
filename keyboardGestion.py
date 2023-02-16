import threading
import keyboard
import bots


class KeyboardGestion:

    def __init__(self, app, parent):
        self.continuer = True
        thread = threading.Thread(target=self.detect_key_press)
        thread.start()
        app.aboutToQuit.connect(self.stop_detect_key_press)
        self.app = app
        self.parent = parent


    def detect_key_press(self):
        while self.continuer:
            keyboard.add_hotkey('escape', lambda:self.stopBot())
            if self.continuer:
                break
            keyboard.wait()

    def stop_detect_key_press(self):
        self.continuer = False

    def stopBot(self=None):
        bots.Bot._arret = True
        self.parent.uncheckButton("START")
