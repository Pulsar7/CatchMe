"""
CatchMe/Backend/Rest-API-Server/Config
"""
import sys,json
sys.dont_write_bytecode = True

class CONFIG():
    def __init__(self,path):
        self.path = path
    
    def get(self,category,name):
        try:
            with open(self.path,'r') as json_file_data:
                data = json.load(json_file_data)
            return data[category][name]
        except Exception as error:
            print("[!] =>",error)