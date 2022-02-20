import sys
from colorama import (Fore,Style)

sys.dont_write_bytecode = True

class PRINTOUT:
    def __init__(self):
        self.red = Style.BRIGHT+Fore.RED
        self.green = Style.BRIGHT+Fore.GREEN
        self.blue = Style.BRIGHT+Fore.BLUE
        self.reset_all = Style.RESET_ALL+Fore.RESET
        self.white = Style.BRIGHT+Fore.WHITE
        self.yellow = Style.BRIGHT+Fore.YELLOW
        self.cyan = Style.BRIGHT+Fore.CYAN
        self.magenta = Style.BRIGHT+Fore.MAGENTA
        self.begin = "  "

    def info(self,msg):
        sys.stdout.write(
            self.begin+self.white+"["+self.yellow+"INFO"+self.white+"]: "+msg+self.reset_all+"\n"
        )

    def load(self,msg):
        sys.stdout.write(
            "\r"+self.begin+self.white+"["+self.cyan+"INFO"+self.white+"]: "+msg+self.reset_all
        )
        sys.stdout.flush()

    def error(self,error_msg):
        sys.stdout.write(
            self.begin+self.white+"["+self.red+"ERROR"+self.white+"]: %s"%(error_msg)+self.reset_all+"\n"
        )
    
    def failed(self):
        sys.stdout.write(
            self.red+"FAILED"+self.reset_all+"\n"
        )

    def ok(self,msg):
        if (msg == None or len(msg) == 0):
            sys.stdout.write(
                self.green+"O.K."+self.reset_all+"\n"
            )
        else:
            sys.stdout.write(
                self.green+"O.K. (%s)"%(msg)+self.reset_all+"\n"
            )

    def warning(self,warning_msg):
        sys.stdout.write(
            self.begin+self.white+"["+self.magenta+"WARNING"+self.white+"]: %s"%(warning_msg)+self.reset_all+"\n"
        )