import sys,sqlite3

sys.dont_write_bytecode = True

class DATABASE:
    def __init__(self,conf,p):
        self.conf = conf
        self.p = p
        self.db_path = self.conf.get('database','path')
        self.db_connection = sqlite3.connect(self.db_path)
        self.db = self.db_connection.cursor()
        #
        self.table_name = "GAMES"
        self.table_values = [
            "ID","NAME","MEMBERS","TIME"
        ]
        self.table_values_string = "".join(self.table_values)
        #
        self.create_tables()
    
    def create_tables(self):
        command = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name}({self.table_values})
        """
        try:
            self.db.execute(command)
        except Exception as error:
            self.p.error(error)
        self.db_connection.commit()
    
    def close(self):
        self.db_connection.close()
        self.p.info("Closed connection to the database")
