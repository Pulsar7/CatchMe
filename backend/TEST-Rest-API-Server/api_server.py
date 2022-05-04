"""
CatchMe/API-Server
"""
from flask import (
    Flask, request, jsonify
)
import sys,json,os
from data.modules import (config,database)

conf = config.CONFIG('data/conf/config.json')
name = conf.get('ApiServer','name')
db = database.DATABASE(conf)
api = Flask(name)

@api.route('/create_game', methods=['POST'])
def create_game():
    pass

@api.route('/participate_game', methods=['POST'])
def participate_game():
    pass

@api.route('/send_coordinate', methods=['POST'])
def send_coordinate():
    pass

@api.route('/get_coordinate', methods=['POST'])
def get_coordinate():
    pass

if (__name__ == '__main__'):
    os.system("clear") # Linux
    api.run(
        host = conf.get('ApiServer','host'),
        port = conf.get('ApiServer','port'),
        debug = True
    )
