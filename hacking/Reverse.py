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
        os.system("python3 /usr/bin/DracOS_VENOMIZER/venomizer.py")  # /usr/bin/
    elif menu == "00":
        exit()
    else:
        print(R('Wrong Input!'))



def back():
    Reverse()


#Function
#Apktool
def Apktool():
    if os.path.isfile("/usr/bin/apktool") or os.path.isfile('/usr/share/apktool'):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Apktool ☣" -geometry 100x30 -e "sudo apt install apktool"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/apktool"):
            print(B("Apktool Already Installed"))
        else:
            print(R("apktool Not Installed"))
        input()
        back()
    # end Apktool

#Dex2jar
def Dex2jar():
    if os.path.isfile("/usr/share/dex2jar"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Dex2jar ☣" -geometry 100x30 -e "sudo apt install dex2jar"'
        )
        os.system("clear")
        if os.path.isfile("/usr/share/dex2jar"):
            print(B("Dex2jar Already Installed"))
        else:
            print(R("dex2jar Not Installed"))
        input()
        back()
    # end Dex2jar

#Edb-debugger
def Edb_debugger():
    if os.path.isfile("/usr/bin/edb"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Edb-debugger ☣" -geometry 100x30 -e "sudo apt install edb-debugger"'
        )
        os.system("clear")
        if os.path.isfile('/usr/bin/edb'):
            print(B("Edb-debugger Already Installed"))
        else:
            print(R('edb-debugger Not Installed'))
        input()
        back()
    # end Edb-debugger

#Jad
def Jad():
    if os.path.isfile("/usr/bin/jad"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Jad ☣" -geometry 100x30 -e "sudo apt install jad"'
        )
        os.system("clear")
        if os.path.isfile('/usr/bin/jad'):
            print(B("Jad Already Installed"))
        else:
            print(R('jad Not Installed'))
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
        if os.path.isfile('usr/bin/javasnoop'):
            print(B("Javasnoop Already Installed"))
        else:
            print(R('javasnoop Not Installed'))
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
        if os.path.isfile('usr/bin/jd-gui'):
            print(B("JD-GUI Already Installed"))
        else:
            print(R('jd-gui Not Installed'))
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
        if os.path.isfile('usr/bin/ollydbg'):
            print(B("ollydbg Already Installed"))
        else:
            print(R('ollydbg Not Installed'))
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
        if os.path.isfile('usr/bin/smali'):
            print(B("Smali Already Installed"))
        else:
            print(R('smali Not Installed'))
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
        if os.path.isfile('usr/bin/valgrind'):
            print(B("Valgrind Already Installed"))
        else:
            print(R('Valgrind Not Installed'))
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
        if os.path.isfile('usr/bin/yara'):
            print(B("YARA Already Installed"))
        else:
            print(R('YARA not Installed'))
        input()
        back()
    # end YARA





# Looping
# while True:
#     Reverse()