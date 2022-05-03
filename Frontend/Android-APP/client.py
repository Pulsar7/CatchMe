"""
FOS-BOS/Informatik/CatchMe/Client
"""
import sys,requests,config
sys.dont_write_bytecode = True

class CLIENT():
    def __init__(self):
        conf = config.CONFIG()
        self.server_url = conf.get('Server','url')
        self.conf = conf
    
    def check_connection_to_server(self):
        response = requests.get(self.server_url)
        if (response.status_code == 200):
            status = True
        else:
            status = False
        return status

    def participate_game(self,data):
        pass # Sending data to server requests.post()

    def create_game(self,game_data):
        pass # Sending data to server requests.post()