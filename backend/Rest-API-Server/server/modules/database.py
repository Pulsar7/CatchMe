"""
CatchMe/Backend/Rest-API-Server/Database
"""
import sys,pymongo,random,string
sys.dont_write_bytecode = True

class DATABASE():
    def __init__(self,conf,logger):
        (self.conf,self.logger) = (conf,logger)
        db_connection_url = conf.get('Database','connection_url')
        client = pymongo.MongoClient(db_connection_url) # connect to pymongo-service
        db = client[conf.get('Database','name')]
        self.game_data_col = db[conf.get('Database','columns')['game_data_col']]
        self.player_modi = conf.get('Game','settings')['player_modi']

    def add_game(self,game_data):
        status = True
        try:
            game_data['game_id'] = self.generate_game_id()
            self.game_data_col.insert_one(game_data)
        except Exception as error:
            status = False
            self.logger.error(error)
        return status

    def select_player_mode(self):
        player_mode = random.choice(self.player_modi)
        return player_mode

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

    
