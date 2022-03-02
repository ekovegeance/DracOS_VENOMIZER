#!/usr/bin/python3
#! -*- coding: utf-8 -*-
#! PasswordAttack.py
import os
from color import *
import Logo

def Hardware():
    os.system("clear")
    Logo.logo_22()
    print(
        G(
            """
    1. Android-sdk
    2. Apktool
    3. Arduino
    4. Dex2jar
    5. Sakis3G
    6. Smalis
    0. Back to Main Menu
            """
        )
    )
    print(R("    00. exit"))

    lists = ('android-sdk', 'apktool', 'arduino', 'dex2jar', 'sakis3g', 'smali')

    menu = int(input(G("[") + R("DracOS") + G("]select>")))
    if menu:
        menu -= 1
        # Call function
        hardware_tool(lists[menu])
    elif menu == 0:
        os.system("python3 /usr/bin/DracOS_VENOMIZER/venomizer.py")  # //usr/bin/
    elif menu == 00:
        exit()
    else:
        print(R('Wrong Input!'))
        input()
        back()



def back():
    Hardware()

#Function
#hardware tool
def hardware_tool(a):
    if os.path.isfile(f"/usr/bin/{a}"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
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
        # end hardware_tool 