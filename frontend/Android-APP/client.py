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

    def participate_to_game(self,data):
        resp = {'code': None,'msg':"None"}
        
        return resp

    def create_game(self,game_data):
        resp = {'code':None,'msg':"None"}
        return resp