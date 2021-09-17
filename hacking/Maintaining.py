#! /usr/share/bin/python3
#! -*- coding: utf-8 -*-
#! PasswordAttack.py
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
    menu = input(G("[") + R("DracOS") + G("]select>"))
    if menu == "1":
        # Call function
        Cryptcat()
    elif menu == "2":
        # Call function
        Cymothoa()
    elif menu == "3":
        # Call function
        Dbd()
    elif menu == "4":
        # Call function
        Dns2tcp()
    elif menu == "5":
        # Call function
        HTTPTunnel()
    elif menu == "6":
        # Call function
        Intersect()
    elif menu == "7":
        # Call function
        Nishang()
    elif menu == "8":
        # Call function
        Polenum()
    elif menu == "9":
        # Call function
        PowerSploit()
    elif menu == "10":
        # Call function
        Pwnat()
    elif menu == "11":
        # Call function
        RidEnum()
    elif menu == "12":
        # Call function
        Sbd()
    elif menu == "13":
        # Call function
        Shellter()
    elif menu == "14":
        # Call function
        U3Pwn()
    elif menu == "15":
        # Call function
        Webshells()
    elif menu == "16":
        # Call function
        Weevely()
    elif menu == "17":
        # Call function
        Winexe()
    elif menu == "0":
        os.system("python3 /usr/bin/DracOS_VENOMIZER/venomizer.py")  # //usr/bin/
    elif menu == "00":
        exit()



def back():
    MaintiningF()

#Function
#Cryptcat
def Cryptcat():
    if os.path.isfile("/usr/bin/cryptcat"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Cryptcat ☣" -geometry 100x30 -e "sudo apt install cryptcat"'
        )
        os.system("clear")
        print(B("Cryptcat Already Installed"))
        input()
        back()
    # end Cryptcat

#Cymothoa
def Cymothoa():
    if os.path.isfile("/usr/bin/cymothoa"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Cymothoa ☣" -geometry 100x30 -e "sudo apt install cymothoa"'
        )
        os.system("clear")
        print(B("Cymothoa Already Installed"))
        input()
        back()
    # end Cymothoa

#Dbd
def Dbd():
    if os.path.isfile("/usr/bin/dbd"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Dbd ☣" -geometry 100x30 -e "sudo apt install dbd"'
        )
        os.system("clear")
        print(B("Dbd Already Installed"))
        input()
        back()
    # end Dbd

#Dns2tcp
def Dns2tcp():
    if os.path.isfile("/usr/bin/dns2tcp"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Dns2tcp ☣" -geometry 100x30 -e "sudo apt install dns2tcp"'
        )
        os.system("clear")
        print(B("Dns2tcp Already Installed"))
        input()
        back()
    # end Dns2tcp
    
#HTTPTunnel
def HTTPTunnel():
    if os.path.isfile("/usr/bin/http-tunnel"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL HTTPTunnel ☣" -geometry 100x30 -e "sudo apt install http-tunnel"'
        )
        os.system("clear")
        print(B("HTTPTunnel Already Installed"))
        input()
        back()
    # end HTTPTunnel

#Intersect
def Intersect():
    if os.path.isfile("/usr/bin/intersect"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Intersect ☣" -geometry 100x30 -e "sudo apt install intersect"'
        )
        os.system("clear")
        print(B("Intersect Already Installed"))
        input()
        back()
    # end Intersect

#Nishang
def Nishang():
    if os.path.isfile("/usr/bin/nishang"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Nishang ☣" -geometry 100x30 -e "sudo apt install nishang"'
        )
        os.system("clear")
        print(B("Nishang Already Installed"))
        input()
        back()
    # end Nishang

#Polenum
def Polenum():
    if os.path.isfile("/usr/bin/polenum"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Polenum ☣" -geometry 100x30 -e "sudo apt install polenum"'
        )
        os.system("clear")
        print(B("Polenum Already Installed"))
        input()
        back()
    # end Polenum

#PowerSploit
def PowerSploit():
    if os.path.isfile("/usr/bin/powersploit"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL PowerSploit ☣" -geometry 100x30 -e "sudo apt install powersploit"'
        )
        os.system("clear")
        print(B("PowerSploit Already Installed"))
        input()
        back()
    # end PowerSploit

#Pwnat
def Pwnat():
    if os.path.isfile("/usr/bin/pwnat"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Pwnat ☣" -geometry 100x30 -e "sudo apt install pwnat"'
        )
        os.system("clear")
        print(B("Pwnat Already Installed"))
        input()
        back()
    # end Pwnat

#RidEnum
def RidEnum():
    if os.path.isfile("/usr/bin/ridenum"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL RidEnum ☣" -geometry 100x30 -e "sudo apt install ridenum"'
        )
        os.system("clear")
        print(B("RidEnum Already Installed"))
        input()
        back()
    # end RidEnum

#Sbd
def Sbd():
    if os.path.isfile("/usr/bin/sbd"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Sbd ☣" -geometry 100x30 -e "sudo apt install sbd"'
        )
        os.system("clear")
        print(B("Sbd Already Installed"))
        input()
        back()
    # end Sbd

#Shellter
def Shellter():
    if os.path.isfile("/usr/bin/shellter"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Shellter ☣" -geometry 100x30 -e "sudo apt install shellter"'
        )
        os.system("clear")
        print(B("Shellter Already Installed"))
        input()
        back()
    # end Shellter

#U3-Pwn
def U3Pwn():
    if os.path.isfile("/usr/bin/u3-pwn"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL U3-Pwn ☣" -geometry 100x30 -e "sudo apt install u3-pwn"'
        )
        os.system("clear")
        print(B("U3-Pwn Already Installed"))
        input()
        back()
    # end U3-Pwn

#Webshells
def Webshells():
    if os.path.isfile("/usr/bin/webshells"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Webshells ☣" -geometry 100x30 -e "sudo apt install webshells"'
        )
        os.system("clear")
        print(B("Webshells Already Installed"))
        input()
        back()
    # end Webshells

#Weevely
def Weevely():
    if os.path.isfile("/usr/bin/weevely"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Weevely ☣" -geometry 100x30 -e "sudo apt install weevely"'
        )
        os.system("clear")
        print(B("Weevely Already Installed"))
        input()
        back()
    # end Weevely

#Winexe
def Winexe():
    if os.path.isfile("/usr/bin/winexe"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Winexe ☣" -geometry 100x30 -e "sudo apt install winexe"'
        )
        os.system("clear")
        print(B("Winexe Already Installed"))
        input()
        back()
    # end Winexe




# Looping
# while True:
#     Maintining()