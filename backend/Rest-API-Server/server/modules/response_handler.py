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
    def __init__(self,conf,logger,db):
        (self.conf,self.logger,self.db) = (conf,logger,db)
        self.timezone = conf.get('APIServer','timezone')
    
    def date(self):
        now = datetime.now(pytz.timezone(self.timezone))
        return (f"{now.day}.{now.month}.{now.year}")
    
    def time(self):
        now = datetime.now(pytz.timezone(self.timezone))
        return (f"{now.hour}:{now.minute}:{now.second}")

    def create_game_route(self):
        if (request.method == "GET"):
            pass
        else:
            pass

    def participate_game_route(self):
        if (request.method == "GET"):
            pass
        else:
            pass

    def send_coordinates_route(self):
        if (request.method == "GET"):
            pass
        else:
            pass
