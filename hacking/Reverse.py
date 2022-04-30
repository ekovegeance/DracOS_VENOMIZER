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
    lists = ('apktool','dex2jar','edb-debugger','jad','javasnoop','jd-gui','ollydbg','smali','yara')
    menu = int(input(G("[") + R("DracOS") + G("]select>")))
    if menu:
        menu -= 1
        # Call function
        reverse_tool(lists[menu])
    elif menu == "0":
        os.system("python3 /usr/bin/DracOS_VENOMIZER/venomizer.py")  # /usr/bin/
    elif menu == "00":
        exit()
    else:
        print(R('Wrong Input!'))
        input()
        back()



def back():
    Reverse()


#Function
#Apktool
def reverse_tool():
    if os.path.isfile(f"/usr/bin/{a}") or os.path.isfile(f'/usr/share/{a}'):
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
    # end Apktool

