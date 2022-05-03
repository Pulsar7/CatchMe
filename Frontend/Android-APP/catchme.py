"""
FOS-BOS/Informatik/CatchMe
"""
from kivymd.uix.snackbar import Snackbar
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
import kivy,sys
from kivymd.icon_definitions import md_icons
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDFillRoundFlatButton
sys.dont_write_bytecode = True
import client,config

class HomeWindow(Screen):
    def __init__(self,**kwargs):
        super(Screen,self).__init__(**kwargs)
        self.info_text = config.CONFIG().get('Window','Home')['info_text']

class SearcherWindow(Screen):
    def __init__(self,**kwargs):
        super(Screen,self).__init__(**kwargs)

class SeekerWindow(Screen):
    def __init__(self,**kwargs):
        super(Screen,self).__init__(**kwargs)

class CreateWindow(Screen):
    def __init__(self,**kwargs):
        super(Screen,self).__init__(**kwargs)
        self.wrong_textfield_elements = config.CONFIG().get('Window','Textfields')['wrong_textfeld_elements']

    def create(self,game_name_textfield,game_password_textfield):
        game_name = game_name_textfield.text
        game_password = game_password_textfield.text
        wrong_element_state = False
        for element in self.wrong_textfield_elements:
            if (game_name == element or game_password == element):
                wrong_element_state = True
                break
        if (wrong_element_state == True):
            self.dialog = MDDialog(
				title = config.CONFIG().get('Messages','error')['dialog_title_wrong_element_state'],
				text = config.CONFIG().get('Messages','error')['dialog_text_wrong_element_state'],
                radius=config.CONFIG().get('Window','DialogBoxes')['radius'],
				buttons = [
					MDFillRoundFlatButton(
						text=config.CONFIG().get('Window', 'OkBtn')['text'],
                        on_release = self.close_dialog
						),
					],	
			)
            self.dialog.open()
        else:
            game_data = {
                'game_name': game_name,
                'game_password': game_password
            }
            resp = client.CLIENT().create_game(game_data)
            if (resp['code'] == True):
                pass
            else:
                self.dialog = MDDialog(
                    title = config.CONFIG().get('Messages','error')['dialog_title_couldnt_create_game'],
                    text = resp['msg'],
                    radius=config.CONFIG().get('Window','DialogBoxes')['radius'],
                    buttons = [
                        MDFillRoundFlatButton(
                            text = config.CONFIG().get('Window', 'OkBtn')['text'], 
                            on_release = self.close_dialog
                            ),
                        ]
			    )
                self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

class ParticipateWindow(Screen):
    def __init__(self,**kwargs):
        super(Screen,self).__init__(**kwargs)
        self.wrong_textfield_elements = config.CONFIG().get('Window','Textfields')['wrong_textfeld_elements']

    def participate(self,game_password_textfield,game_id_textfield,player_nickname_textfield):
        wrong_element_state = False
        game_id = game_id_textfield.text
        game_password = game_password_textfield.text
        player_nickname = player_nickname_textfield.text
        for element in self.wrong_textfield_elements:
            if (game_id == element or game_password == element 
                or player_nickname == element
            ):
                wrong_element_state = True
                break
        if (wrong_element_state == True):
            self.dialog = MDDialog(
				title = config.CONFIG().get('Messages','error')['dialog_title_wrong_element_state'],
				text = config.CONFIG().get('Messages','error')['dialog_text_wrong_element_state'],
                radius=config.CONFIG().get('Window','DialogBoxes')['radius'],
				buttons = [
					MDFillRoundFlatButton(
						text=config.CONFIG().get('Window', 'OkBtn')['text'],
                        on_release = self.close_dialog
						),
					],	
			)
            self.dialog.open()
        else:
            game_data = {
                'game_id': game_id,
                'game_password': game_password,
                'player_nickname': player_nickname
            }
            resp = client.CLIENT().participate_to_game(game_data)
            if (resp['code'] == True):
                pass
            else:
                self.dialog = MDDialog(
				title = config.CONFIG().get('Messages','error')['dialog_title_couldnt_participate_game'],
				text = resp['msg'],
                radius=config.CONFIG().get('Window','DialogBoxes')['radius'],
				buttons = [
					MDFillRoundFlatButton(
						text=config.CONFIG().get('Window', 'OkBtn')['text'],
                        on_release = self.close_dialog
						),
					],	
			    )
                self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

class WindowManager(Screen):
    pass

class CatchMe(MDApp):

    def build(self):
        screen = Builder.load_file(config.CONFIG().get('Window','kv_filepath'))
        self.theme_cls.primary_palette = config.CONFIG().get('Window','primary_palette')
        return screen

    def on_start(self, **kwargs):
        state = client.CLIENT().check_connection_to_server()
        if (state == False):
            self.dialog = MDDialog(
				title = config.CONFIG().get('Messages','error')['dialog_title_server_connection_problems'],
				text = config.CONFIG().get('Messages','error')['dialog_text_server_connection_problems'],
				radius=config.CONFIG().get('Window','DialogBoxes')['radius'],
                buttons = [
					MDFillRoundFlatButton(
						text=config.CONFIG().get('Window', 'OkBtn')['text'],
                        on_release = self.close_dialog
						),
					]	
			)
            self.dialog.open()
        else:
            pass

    def close_dialog(self, obj):
        self.dialog.dismiss()

if (__name__ == '__main__'):
    CatchMe().run()
