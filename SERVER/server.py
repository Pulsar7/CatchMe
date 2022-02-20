from http import client
import socket,sys,platform,os,threading
sys.dont_write_bytecode = True
from __server__.modules import (config,printout,database)

class SERVER:
    def __init__(self,p,conf):
        self.conf = conf
        self.p = p
        self.max_incoming_connections = conf.get('server','max_incoming_connections')
        self.server_host = conf.get('server','host')
        self.server_port = conf.get('server','port')
        self.database = database.DATABASE(conf,p)
        self.up_state = True
        self.connections = {}
        self.error_counter = 0

    def run(self):
        (state,server) = self.create_socket()
        if (state == True):
            self.server = server
            while (self.up_state == True):
                try:
                    (
                    client_socket,client_addr
                    ) = self.server.accept()
                    self.p.load("New incoming connection")
                    self.p.ok("%s:%s"%(client_addr[0],client_addr[1]))
                    client_thread = threading.Thread(
                        target = CLIENTS().client,
                        args = (client_socket,client_addr)
                    )
                    client_thread.start()
                except Exception as error:
                    self.error_counter += 1
                    self.p.error(error)
                    if (self.error_counter > 5):
                        self.p.warning("To much errors appeared!")
                        self.up_state = False
                        break
                    else:
                        self.p.warning(
                            "Could not handle new incoming connection!"
                        )
        else:
            self.p.warning("Could not start server.")
        if (self.up_state == True and state == True):
            self.close_server()
            self.database.close()
    
    def close_server(self):
        self.server.close()
        self.p.info("Closed server")

    def create_socket(self):
        self.p.load(f"Creating Server-Socket...")
        try:
            server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP
            server.bind((
                self.server_host,self.server_port
            ))
            server.listen(self.max_incoming_connections)
            state = True
            self.p.ok(f"{self.server_host}:{self.server_port}")
            self.p.info(
                f"Listening for max {self.max_incoming_connections} connections"
            )
        except Exception as error:
            self.p.failed(),self.p.error(error)
            state = False
        return (state,server)

class CLIENTS(SERVER):
    def __init__(self):
        super(SERVER).__init__(self)
    
    def client(self,client_socket,client_addr):
        self.p.info(f"[{client_socket}]")
        client_data = {"socket":client_socket,"addr":client_addr}
        self.close_connection_to_client(client_data)
        sys.exit()
    
    def close_connection_to_client(self,client_data):
        self.p.load("Closing connection to %s:%s..."%(
            client_data['addr'][0],client_data['addr'][1]
        ))
        try:
            client_data['socket'].close()
            self.p.ok("")
        except Exception as error:
            self.p.failed(),self.p.error(error)

p = printout.PRINTOUT()
conf = config.CONFIGURER(p)

if (__name__ == '__main__'):
    if (platform.system() == "Windows"):
        os.system("cls")
    else:
        os.system("clear")
    server = SERVER(p,conf)
    server.run()