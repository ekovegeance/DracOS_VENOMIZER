#! usr/share/bin/python3
#! -*- coding: utf-8 -*-
#! PasswordAttack.py
import os
from color import *
import Logo

def Reverse():
    os.system("clear")
    Logo.logo_20()
    print(
        G(
            """
    1.  Apktool
    2.  Dex2jar
    3.  Edb-debugger
    4.  Jad
    5.  Javasnoop
    6.  JD-GUI
    7.  OllyDbg
    8.  Smali
    9.  Valgrind
    10. YARA
    0.  Back to Main Menu
            """
        )
    )
    print(R("    00. exit"))
    menu = input(G("[") + R("DracOS") + G("]select>"))
    if menu == "1":
        # Call function
        Apktool()
    if menu == "2":
        # Call function
        Dex2jar()
    if menu == "3":
        # Call function
        Edb_debugger()
    if menu == "4":
        # Call function
        Jad()
    if menu == "5":
        # Call function
        Javasnoop()
    if menu == "6":
        # Call function
        JD_GUI()
    if menu == "7":
        # Call function
        OllyDbg()
    if menu == "8":
        # Call function
        Smali()
    if menu == "9":
        # Call function
        Valgrind()
    if menu == "10":
        # Call function
        YARA()
    elif menu == "0":
        os.system("python3 $HOME/git/DracOS_VENOMIZER/venomizer.py")  # /usr/bin/
    elif menu == "00":
        exit()



def back():
    Reverse()


#Function
#Apktool
def Apktool():
    if os.path.isfile("usr/bin/apktool"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Apktool ☣" -geometry 100x30 -e "sudo apt install apktool"'
        )
        os.system("clear")
        print(B("Apktool Already Installed"))
        input()
        back()
    # end Apktool

#Dex2jar
def Dex2jar():
    if os.path.isfile("usr/bin/dex2jar"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Dex2jar ☣" -geometry 100x30 -e "sudo apt install dex2jar"'
        )
        os.system("clear")
        print(B("Dex2jar Already Installed"))
        input()
        back()
    # end Dex2jar

#Edb-debugger
def Edb_debugger():
    if os.path.isfile("usr/bin/edb-debugger"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Edb-debugger ☣" -geometry 100x30 -e "sudo apt install edb-debugger"'
        )
        os.system("clear")
        print(B("Edb-debugger Already Installed"))
        input()
        back()
    # end Edb-debugger

#Jad
def Jad():
    if os.path.isfile("usr/bin/jad"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Jad ☣" -geometry 100x30 -e "sudo apt install jad"'
        )
        os.system("clear")
        print(B("Jad Already Installed"))
        input()
        back()
    # end Jad

#Javasnoop
def Javasnoop():
    if os.path.isfile("usr/bin/javasnoop"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Javasnoop ☣" -geometry 100x30 -e "sudo apt install javasnoop"'
        )
        os.system("clear")
        print(B("Javasnoop Already Installed"))
        input()
        back()
    # end Javasnoop

#JD-GUI
def JD_GUI():
    if os.path.isfile("usr/bin/jd-gui"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL JD-GUI ☣" -geometry 100x30 -e "sudo apt install jd-gui"'
        )
        os.system("clear")
        print(B("JD-GUI Already Installed"))
        input()
        back()
    # end JD-GUI

#OllyDbg
def OllyDbg():
    if os.path.isfile("usr/bin/ollydbg"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL OllyDbg ☣" -geometry 100x30 -e "sudo apt install ollydbg"'
        )
        os.system("clear")
        print(B("OllyDbg Already Installed"))
        input()
        back()
    # end OllyDbg

#Smali
def Smali():
    if os.path.isfile("usr/bin/smali"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Smali ☣" -geometry 100x30 -e "sudo apt install smali"'
        )
        os.system("clear")
        print(B("Smali Already Installed"))
        input()
        back()
    # end Smali

#Valgrind
def Valgrind():
    if os.path.isfile("usr/bin/valgrind"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Valgrind ☣" -geometry 100x30 -e "sudo apt install valgrind"'
        )
        os.system("clear")
        print(B("Valgrind Already Installed"))
        input()
        back()
    # end Valgrind

#YARA
def YARA():
    if os.path.isfile("usr/bin/yara"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL YARA ☣" -geometry 100x30 -e "sudo apt install yara"'
        )
        os.system("clear")
        print(B("YARA Already Installed"))
        input()
        back()
    # end YARA





# Looping
# while True:
#     Reverse()