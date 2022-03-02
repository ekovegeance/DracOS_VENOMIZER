#! /usr/share/bin/python3
#! -*- coding: utf-8 -*-
#! PasswordAttack.py
from json.tool import main
import os
from color import *
import Logo

def MaintiningF():
    os.system("clear")
    Logo.logo_19()
    print(
        G(
            """
    1.  Cryptcat
    2.  Cymothoa
    3.  Dbd
    4.  Dns2tcp
    5.  HTTPTunnel
    6.  Intersect
    7.  Nishang
    8.  Polenum
    9.  PowerSploit
    10. Pwnat
    11. RidEnum
    12. Sbd
    13. Shellter
    14. U3-Pwn
    15. Webshells
    16. Weevely
    17. Winexe
    0.  Back to Main Menu
            """
        )
    )
    print(R("    00. exit"))
    lists = ('cryptcat', 'cymothoa', 'dbd', 'dns2tcp', 'http-tunnel', 'intersect', 'nishang',
     'polenum', 'powersploit', 'pwnat', 'ridenum', 'sbd', 'shellter', 'u3-pwn', 'webshells', 'weevely', 'winexe')
    menu = int(input(G("[") + R("DracOS") + G("]select>")))
    if menu:
        menu -= 1
        # Call function
        maintaining_tool(lists[menu])
    elif menu == 0:
        os.system("python3 /usr/bin/DracOS_VENOMIZER/venomizer.py")  # //usr/bin/
    elif menu == 00:
        exit()
    else:
        print(R('Wrong Input!'))
        input()
        back()



def back():
    MaintiningF()

#Function
#maintaining_tool
def maintaining_tool(a):
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
            print(R(f"Not Installing {a}"))
        input()
        back()
        # end maintaining_tool