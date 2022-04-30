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
    lists = ('casefile','cherrytree','cutycapt','dos2unix','dradis','magic-tree','metagoofil','nipper-ng','pipal','rdpy')
    menu = int(input(G("[")+R("DracOS")+G("]select> ")))
    if menu:
        menu -= 1
        # Call Function
        reporting_tools(list[menu])
    elif menu == '0':
        os.system('python3 /usr/bin/DracOS_VENOMIZER/venomizer.py')
    elif menu == '00':
        exit()
    else:
        print(R('Wrong Input!'))
        input()
        back()

#Function
#CaseFile
def reporting_tools(a):
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
    # end CaseFile


def back():
    Report()