"""
> Catch-Me / Project
> Python: 3.8.2
> Author: Pulsar
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import socket

class SERVER:
    def __init__(self):
        self.own_bdaddr = ""
        self.channel = 4
    
    def create_socket(self):
        state = True
        try:
            server = socket.socket(socket.AF_BLUETOOTH, 
                socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
            server.bind((self.own_bdaddr,self.channel))
        except Exception as error:
            state = False
            server = error
        return (server,state)

class CLIENT:
    def __init__(self):
        pass
    
class MainWindow(Screen):

    def generate_room(self):
        (server,state) = SERVER.create_socket()
        if (state == False):
            self.ids.error_label.text = self.server
        else:
            self.ids.error_label.text = "All good"


class GameWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("catchme.kv")

class CatchMe(App):
    def build(self):
        return kv

if (__name__ == "__main__"):
    CatchMe().run()
    
