"""
CatchMe/Backend/Rest-API-Server
"""
import sys,os,argparse,logging
sys.dont_write_bytecode = True
from server.modules import (config,database,response_handler)
from flask import (Flask)

conf = config.CONFIG('server/conf/config.json')
server_name = conf.get('APIServer', 'name')
db = database.DATABASE(conf)
catchme_api = Flask(server_name)

# Argparse
parser = argparse.ArgumentParser(description=server_name)
parser.add_argument('-d', '--debug',
    action='store_true',
    dest='debug',
    help='Activates debug mode'
)
args = parser.parse_args()

# Logging
logger = logging.getLogger(server_name)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(conf.get('Logging','format'))
ch.setFormatter(formatter)
logger.addHandler(ch)

# Response-Handler
db = database.DATABASE(conf,logger)
responder = response_handler.HANDLER(conf,logger,db)

# API-Routes
catchme_api.add_url_rule('/create_game',view_func=responder.create_game_route,methods=['POST','GET'])
catchme_api.add_url_rule('/participate_game',view_func=responder.participate_game_route,methods=['POST','GET'])
catchme_api.add_url_rule('/send_coordinates',view_func=responder.send_coordinates_route,methods=['POST','GET'])


if (__name__ == '__main__'):
    os.system("clear") #Linux
    logger.info(f"Debug mode: {args.debug}")
    catchme_api.run(
        host = conf.get('APIServer','host'),
        port = conf.get('APIServer','port'),
        debug = args.debug
    )
