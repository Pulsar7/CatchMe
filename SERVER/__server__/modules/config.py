import sys,json

sys.dont_write_bytecode = True

class CONFIGURER:
    def __init__(self,p):
        self.p = p
        self.path = "__server__/conf/config.json"
        self.data = self.get_config_data()
    
    def get_config_data(self):
        self.p.load(f"Get data from config-file...")
        try:
            with open(self.path) as json_file_data:
                data = json.load(json_file_data)
            self.p.ok(self.path)
        except Exception as error:
            self.p.failed(),self.p.error(error)
        return data

    def get(self,categorie,name):
        config_data = None
        try:
            config_data = self.data[categorie][name]
        except Exception as error:
            self.p.error(error)
        return config_data