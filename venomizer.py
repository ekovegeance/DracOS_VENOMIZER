#! usr/share/bin/python3
#! -*- coding: utf-8 -*-
#! venomizer.py

from color import R
from termcolor import colored as c
import sys
import Logo
import hack#, eksploit #, InformatingGathering #, VulnerabilityAssesment, webAttack, dll
import os.path
import os
from install import install

if os.path.isfile('sudo /usr/local/lib/python3.7/dist-packages/termcolor.py'):
    print()
else:
    os.system('xterm -T " INSTALL TERMCOLOR " -geometry 100x30 -e "sudo pip install termcolor -y"')
#check if root (Masih ada bug) mohon di perbaiki )
def checkroot():
    if os.geteuid() != 0:
        print(c("[-]", 'red')+c(" You must be root to run this script", 'red'))
        sys.exit()
# cek apakah file git sudah ada!
# jika sudah ada maka kita lewati
if os.path.isfile('/usr/bin/git'):
    print()
else:
    # jika belum install dulu
    os.system('xterm -T "☣ INSTALL GIT ☣" -geometry 100x30 -e "sudo apt-get install git -y"')

# 
# logo
def LOGO():
    os.system("clear")
    print(c("        -os:",'red'))
    print("            "+c("-os/`", 'red'))
    print("            "+c("  :s", 'red')+c("y+-`",'red'))
    print("            "+c("   `/y", 'red')+c("yyy+.",'red'))
    print("            "+c("     `+y", 'red')+c("yyyo-",'red'))
    print("            "+c("       `/y", 'red')+c("yyys:",'red'))
    print(c("`:osssoo",'red')+c("oo++-",'red'),c("        +y", 'red')+c("yyyyy/`",'red'))
    print(c("   ./yyyy",'red')+c("yyo ",'red'),c("        yo`", 'red')+c(":syyyy+.",'red'))
    print(c("      -oyy",'red')+c("y+ ",'red')+c("        +-   :y", 'red')+c("yyyyo-",'red'))
    print(c("        `:s",'red')+c("y:",'red')+c("        `.    `/y", 'red')+c("yyyys:",'red'))
    print(c("           .",'red')+c("/o')+/.`",'red')+c("           .oyy", 'red')+c("so+oo:`",'red'))
    print(c("              :+oo+//::::///:-.`",'red')+c("     `.`",'red'))
    print(c('=================================================================', 'green'))
    print("__      _______ __   __  _____  ___  ___ _____ ___________ _____   ")
    print("\ \    / / ____|  \  | |/ ___ \|   \/   |_   _|___  |  ___| __   \ ")
    print(" \ \  / /| |__ |   \ | | |   | | |\  /| | | |    / /| |__ | |__) / ")
    print("  \ \/ / |  __|| |\ \| | |   | | | \/ | | | |   / / |  __||  _  /  ")
    print("   \  /  | |___| | \   | |___| | |    | |_| |_ / /__| |___| | \ \  ") 
    print("    \/   |_____|_|  \__|\_____/|_|    |_|_____/_____|_____|_|  \_\ ")
    print(c('[(c) 2018 |', 'red'), c('dracos-linux.org | https://github.com/dracos-linux', 'red')+c(']', 'red'))


# menu
global DracOS
DracOS = c('[','green')+c('DracOS','red')+c(']> ','green')

def menu():
    checkroot()
    # call logo
    os.system('clear')
    LOGO()
    # print(c('[PERHATIAN UNTUK PERTAMA KALI LAKUKAN SETUP!!!] klik Y', 'green'))
    print(c('0.  sudo apt update', 'green'))
    print(c('1.  sudo apt upgrade', 'green'))
    print(c('2.  Install', 'green'))
    print(c('3.  Check Update Tools', 'green'))
    print(c('4.  Hacking', 'green'))
    print(c('5.  Informating gathering', 'green'))
    print(c('6.  Vulnerability Assessment', 'green'))
    print(c('7.  Web Attack', 'green'))
    print(c('8.  Exploitation Tools', 'green'))
    print(c('9.  Privilege Escalation', 'green'))
    print(c('10. Password Attack', 'green'))
    print(c('11. Social Engineering', 'green'))
    print(c('12. Man In The Middle attack', 'green'))
    print(c('13. Stress Testing', 'green'))
    print(c('14. Wireless Attack', 'green'))
    print(c('15. Maintining Access', 'green'))
    print(c('16. Forensic Tools', 'green'))
    print(c('17. Reverse Engineering', 'green'))
    print(c('18. Malware Analysis', 'green'))
    print(c('19. Covering Track', 'green'))
    print(c('00. exit'))
    menu = input(DracOS)
    if menu == '0':
        var = input('sudo apt update(y/n)? ')
        if var == 'y': 
                os.system('sudo apt update')
                back()
        else:
            back()
    elif menu == '1':
        var = input('sudo apt upgrade(y/n)? ')
        if var == 'y':
            os.system('sudo apt upgrade')
            back()
        else:
            back()
    elif menu == '2':
        install()
    # elif menu == '3':
    #     check_update_tools()
    elif menu == '4':
        hack.hacking()
    elif menu == '5':
        os.system('python3 $HOME/git/DracOS_VENOMIZER/InformatingGathering.py')
    elif menu == '6':
        os.system('python3 $HOME/git/DracOS_VENOMIZER/VulnerabilityAssesment.py')
    # elif menu == '7':
    #     WebAttack()
    elif menu == '8':
        os.system('python3 $HOME/git/DracOS_VENOMIZER/exploit.py')
    # # elif menu == '9':
    #     PrivilegeEscalation()
    elif menu == '10':
        os.system('python3 $HOME/git/DracOS_VENOMIZER/PasswordAttack.py')
    # elif menu == '11':
    #     SocialEngineering()
    # elif menu == '12':
    #     ManInTheMiddleAttack()
    elif menu == '13':
        os.system('python3 $HOME/git/DracOS_VENOMIZER/Stress.py')
    # elif menu == '14':
    #     WirelessAttack()
    elif menu == '15':
        os.system('python3 $HOME/git/DracOS_VENOMIZER/Maintaining.py')
    elif menu == '16':
        os.system('python3 $HOME/git/DracOS_VENOMIZER/Forensic.py')
    elif menu == '17':
        os.system('python3 $HOME/git/DracOS_VENOMIZER/reverse.py')
    # elif menu == '18':
    #     MalwareAnalysis()
    # elif menu == '19':
    #     CoveringTrack()
    elif menu == '00':
        print(R("Thanks for using venomizer "))
        os.system('exit')
        sys.exit()
        exit()
    elif menu == 'clear':
        os.system('clear')
        back()


def back():
    menu()


while menu():
    menu()
