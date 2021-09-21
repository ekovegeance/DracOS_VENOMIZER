import os
from color import*
import Logo

def Report():
    os.system("clear")
    Logo.logo_21()
    print(G(""" 
    1.  CaseFile
    2.  cherrytree
    3.  CutyCapt
    4.  dos2unix
    5.  Dradis
    6.  MagicTree
    7.  Metagoofil
    8.  Nipper-ng
    9.  pipal
    10. RDPY
     0.  back
     """))
    print(R('00. exit'))
    menu = input(G("[")+R("DracOS")+G("]select> "))
    if menu == '1':
        # Call Function
        CaseFile()
    elif menu == '2':
        # Call Function
        cherrytree()
    elif menu == '3':
        # Call Function
        CutyCapt()
    elif menu == '4':
        # Call Function
        dos2unix()
    elif menu == '5':
        # Call Function
        Dradis()
    elif menu == '6':
        # Call Function
        MagicTree()
    elif menu == '7':
        # Call Function
        Metagoofil()
    elif menu == '8':
        # Call Function
        Nipper_ng()
    elif menu == '9':
        #Call Function
        pipal()
    elif menu == '10':
        #Call Function
        RDPY()
    elif menu == '0':
        os.system('python3 /usr/bin/DracOS_VENOMIZER/venomizer.py')
    elif menu == '00':
        exit()
    else:
        print(R('Wrong Input!'))

#Function
#CaseFile
def CaseFile():
    if os.path.isfile("/usr/bin/casefile"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL CaseFile ☣" -geometry 100x30 -e "sudo apt install casefile"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/casefile"):
            print(B("CaseFile Already Installed"))
        else:
            print(R("CaseFile Not Installed"))
        input()
        back()
    # end CaseFile

# cherrytree
def cherrytree():
    if os.path.isfile("/usr/bin/cherrytree"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL CherryTree ☣" -geometry 100x30 -e "sudo apt install cherrytree"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/cherrytree"):
            print(B("CherryTree Already Installed"))
        else:
            print(R("CherryTree Not Installed"))
        input()
        back()
    # end cherrytree

# CutyCapt
def CutyCapt():
    if os.path.isfile("/usr/bin/cutycapt"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL CutyCapt ☣" -geometry 100x30 -e "sudo apt install cutycapt"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/cutycapt"):
            print(B("CutyCapt Already Installed"))
        else:
            print(R("CutyCapt Not Installed"))
        input()
        back()
    # end CutyCapt

# dos2unix
def dos2unix():
    if os.path.isfile("/usr/bin/dos2unix"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL dos2unix ☣" -geometry 100x30 -e "sudo apt install dos2unix"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/dos2unix"):
            print(B("dos2unix Already Installed"))
        else:
            print(R("dos2unix Not Installed"))
        input()
        back()
    # end dos2unix

# Dradis
def Dradis():
    if os.path.isfile("/usr/bin/dradis"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Dradis ☣" -geometry 100x30 -e "sudo apt install dradis"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/dradis"):
            print(B("dradis Already Installed"))
        else:
            print(R("dradis Not Installed"))
        input()
        back()
    # end dos2unix

# MagicTree
def MagicTree():
    if os.path.isfile("/usr/bin/magic-tree"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL MagicTree ☣" -geometry 100x30 -e "sudo apt install magic-tree"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/magic-tree"):
            print(B("MagicTree Already Installed"))
        else:
            print(R("MagicTree Not Installed"))
        input()
        back()
    # end dos2unix

# Metagoofil
def Metagoofil():
    if os.path.isfile("/usr/bin/metagoofil"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Metagoofil ☣" -geometry 100x30 -e "sudo apt install metagoofil"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/metagoofil"):
            print(B("Metagoofil Already Installed"))
        else:
            print(R("Metagoofil Not Installed"))
        input()
        back()
    # end Metagoofil

# Nipper-ng
def Nipper_ng():
    if os.path.isfile("/usr/bin/nipper-ng"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Nipper-ng ☣" -geometry 100x30 -e "sudo apt install nipper-ng"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/nipper-ng"):
            print(B("Nipper-ng Already Installed"))
        else:
            print(R("Nipper-ng Not Installed"))
        input()
        back()
    # end Nipper-ng

# pipal
def pipal():
    if os.path.isfile("/usr/bin/pipal"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL pipal ☣" -geometry 100x30 -e "sudo apt install pipal"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/pipal"):
            print(B("pipal Already Installed"))
        else:
            print(R("pipal Not Installed"))
        input()
        back()
    # end pipal

# RDPY
def RDPY():
    if os.path.isfile("/usr/bin/rdpy"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL RDPY ☣" -geometry 100x30 -e "sudo apt install rdpy"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/rdpy"):
            print(B("RDPY Already Installed"))
        else:
            print(R("RDPY Not Installed"))
        input()
        back()
    # end RDPY

def back():
    Report()