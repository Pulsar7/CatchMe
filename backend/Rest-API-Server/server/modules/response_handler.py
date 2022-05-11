"""
CatchMe/Backend/Response-Handler
"""
import sys,json,pytz
from datetime import datetime
sys.dont_write_bytecode = True
from flask import (
    jsonify, render_template, redirect, request
)

class HANDLER():
    def __init__(self,conf,logger,db,log_messages):
        (self.conf,self.logger,self.db,self.log_messages) = (conf,logger,db,log_messages)
        self.timezone = conf.get('APIServer','timezone')
    
    def date(self):
        now = datetime.now(pytz.timezone(self.timezone))
        return (f"{now.day}.{now.month}.{now.year}")
    
    def time(self):
        now = datetime.now(pytz.timezone(self.timezone))
        return (f"{now.hour}:{now.minute}:{now.second}")

    def bad_request_route(self,*args):
        self.logger.warning(self.log_messages['warning']['bad_request'])
        return jsonify(self.conf.get('Game','responses')['bad_request_route']['get_method'])

    def not_found_route(self,*args):
        self.logger.warning(self.log_messages['warning']['not_found'])
        return jsonify(self.conf.get('Game','responses')['not_found_route']['get_method'])

    def index_route(self):
        return jsonify(self.conf.get('Game','responses')['index_route']['get_method'])

    def create_game_route(self):
        if (request.method == "GET"):
            return jsonify(self.conf.get('Game', 'responses')['create_game_route']['get_method'])
        else:
            pass

    def participate_game_route(self):
        if (request.method == "GET"):
            return jsonify(self.conf.get('Game', 'responses')['participate_game_route']['get_method'])
        else:
            pass

    def send_coordinates_route(self):
        if (request.method == "GET"):
            return jsonify(self.conf.get('Game', 'responses')['send_coordinates_route']['get_method'])
        else:
            pass
