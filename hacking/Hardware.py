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
    menu = input(G("[") + R("DracOS") + G("]select>"))
    if menu == "1":
        # Call function
        Android_sdk()
    elif menu == "2":
        # Call function
        Apktool()
    elif menu == "3":
        # Call function
        Arduino()
    elif menu == "4":
        # Call function
        Dex2jar()
    elif menu == "5":
        # Call function
        Sakis3G()
    elif menu == "6":
        # Call function
        Smalis()
    elif menu == "0":
        os.system("python3 /usr/bin/DracOS_VENOMIZER/venomizer.py")  # //usr/bin/
    elif menu == "00":
        exit()
    else:
        print(R('Wrong Input!'))
        input()
        back()



def back():
    Hardware()

#Function
#Android-sdk
def Android_sdk():
    if os.path.isfile("/usr/bin/android-sdk"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Android-sdk ☣" -geometry 100x30 -e "sudo apt install android-sdk"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/android-sdk"):
            print(B("Android-sdk Already Installed"))
        else:
            print(R("Android-sdk Not Installed"))
    input()
    back()
        # end android-sdk

#Apktool
def Apktool():
    if os.path.isfile("/usr/bin/apktool"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Apktool ☣" -geometry 100x30 -e "sudo apt install apktool"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/apktool"):
            print(B("Apktool Already Installed"))
        else:
            print(R("Apktool Not Installed"))
    input()
    back()
    # end apktool

#Arduino
def Arduino():
    if os.path.isfile("/usr/bin/arduino"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Arduino ☣" -geometry 100x30 -e "sudo apt install arduino"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/arduino"):
            print(B("Arduino Already Installed"))
        else:
            print(R("Arduino Not Installed"))
    input()
    back()
    # end arduino

#Dex2jar
def Dex2jar():
    if os.path.isfile("/usr/bin/dex2jar"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Dex2jar ☣" -geometry 100x30 -e "sudo apt install dex2jar"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/dex2jar"):
            print(B("Dex2jar Already Installed"))
        else:
            print(R("Dex2jar Not Installed"))
    input()
    back()
    # end dex2jar

#Sakis3G
def Sakis3G():
    if os.path.isfile("/usr/bin/sakis3g"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Sakis3G ☣" -geometry 100x30 -e "sudo apt install sakis3g"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/sakis3g"):
            print(B("Sakis3G Already Installed"))
        else:
            print(R("Sakis3G Not Installed"))
    input()
    back()
    # end sakis3g

#Smalis
def Smalis():
    if os.path.isfile("/usr/bin/smali"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Smalis ☣" -geometry 100x30 -e "sudo apt install smali"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/smali"):
            print(B("Smalis Already Installed"))
        else:
            print(R("Smalis Not Installed"))
    input()
    back()
    # end smalis





# Looping
# while True:
#     Hardware()