"""
FOS-BOS/Informatik/CatchMe/Config
"""
import sys
import json
sys.dont_write_bytecode = True


class CONFIG():
    def __init__(self,path):
        self.path = path

    def get(self, cat, name):
        with open(self.path, 'r') as json_file_data:
            data = json.load(json_file_data)
        return data[cat][name]
