"""
CatchMe/API-Server/Database
"""
import json,sys,os,pymongo,hashlib
sys.dont_write_bytecode = True

class DATABASE():
    def __init__(self,conf):
        self.conf = conf
        db_connection_url = conf.get('Database','connection_url')
        client = pymongo.MongoClient(db_connection_url)
        db = client[conf.get('Database', 'name')]
        self.game_data_col = db[conf.get('Database','game_data_col_name')]
        self.coordinates_data_col = db[conf.get('Database','coordinates_data_col_name')]

    def create_game(self,game_data):
        status = True
        