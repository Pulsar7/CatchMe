"""
CatchMe/Backend/Rest-API-Server/Database
"""
import sys,pymongo,random,string
sys.dont_write_bytecode = True

class DATABASE():
    def __init__(self,conf,logger):
        (self.conf,self.logger) = (conf,logger)
        db_connection_url = conf.get('Database','connection_url')
        client = pymongo.MongoClient(db_connection_url)
        db = client[conf.get('Database','name')]
        self.game_data_col = db[conf.get('Database','columns')['game_data_col']]

    def generate_game_id(self):
        generated_game_id = None
        while True:
            game_id_elements = []
            for i in range(0,self.conf.get('Game','settings')['game_id']['len']):
                number = random.randint(
                    self.conf.get('Game','settings')['game_id']['min'],
                    self.conf.get('Game','settings')['game_id']['max']
                )
                game_id_elements.append(str(number))
            generated_game_id = "#"+"".join(game_id_elements)
            elements = self.game_data_col.find({'game_id':generated_game_id})
            if (len(elements) == 0):
                break
            else:
                print(elements,"FOUND")
        return generated_game_id

    