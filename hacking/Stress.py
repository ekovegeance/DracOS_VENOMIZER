#! /usr/share/bin/python3
#! -*- coding: utf-8 -*-
#! Stress.py
import os
from color import *
import Logo

def Stress():
    os.system("clear")
    Logo.logo_14()
    print(
        G(
            """
    1.  DHCPig
    2.  FunkLoad
    3.  iaxflood
    4.  Inundator
    5.  inviteflood
    6.  ipv6toolkit
    7.  mdk3
    8.  Reaver
    9.  rtpflood
    10. SlowHTTPTest
    11. t50
    12. Termineter
    13. THC-IPV6
    14. THC-SSL-DOS
    0.  Back to main menu        
            """
        )
    )
    print(R("    00. exit"))
    lists = ('dhcpig','funkload','iaxflood','inundator','inviteflood','ipv6toolkit','mdk3','reaver','rtpflood','slowhttptest','t50','termineter','thc-ipv6',
    'thc-ssl-dos')
    menu = int(input(G("[") + R("DracOS") + G("]select>")))
    if menu:
        menu -= 1
        # Call function
        stress_tool(lists[name])
    elif menu == "0":
        os.system("python3 /usr/bin/DracOS_VENOMIZER/venomizer.py")  # //usr/bin/
    elif menu == "00":
        exit()
    else:
        print(R('Wrong Input!'))
        input()
        back()




#Funciton
# stress tool
def stress_tool(a):
    if os.path.isfile(f"/usr/bin/{a}"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            f'xterm -T "☣ INSTALL {a} ☣" -geometry 100x30 -e "sudo apt install {a}"'
        )
        os.system("clear")
        if os.path.isfile(f"/usr/bin/{a}"):
            print(B(f"{a} Already Installed"))
        else:
            print(R(f"{a} Not Installed"))
        input()
        back()
    # end stress tool

def back():
    Stress()
# while True:
#     Stress()