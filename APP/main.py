"""
> Catch-Me / Project
> Python: 3.8.2
> Author: Pulsar
"""
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen

class HomeWindow(Screen):
    def __init__(self,**kwargs):
        super(Screen,self).__init__(**kwargs)

        self.info_text_one = """Lorem ipsum dolor sit amet, consetetur sadipscing
        \nelitr, sed diam nonumy eirmod tempor invidunt ut 
        \nlabore et dolore magna aliquyam erat, sed diam voluptua. 
        \nAt vero eos et accusam et justo duo dolores et ea rebum. 
        \nStet clita kasd gubergren, no sea takimata sanctus est
        """
        self.info_text_two = """Lorem ipsum dolor sit amet, consetetur sadipscing
        \nelitr, sed diam nonumy eirmod tempor invidunt ut 
        \nlabore et dolore magna aliquyam erat, sed diam voluptua. 
        \nAt vero eos et accusam et justo duo dolores et ea rebum. 
        \nStet clita kasd gubergren, no sea takimata sanctus est
        """
        self.error_msg = ""

class CreateGameWindow(Screen):
    def create_group(self):
        pass

class ParticipateGameWindow(Screen):
    def participate(self):
        pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("catchme.kv")

class CatchMe(App):
    def build(self):
        return kv

if (__name__ == "__main__"):
    CatchMe().run()
    
