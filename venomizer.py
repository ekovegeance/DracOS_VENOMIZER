from termcolor import colored as c
import os
import sys
import os.path
from os import path


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
    print(c('[(c) 2018 |', 'red'), c('dracos-linux.org | https://github.com/DracOS-Remaster', 'red')+c(']', 'red'))

def data():
    # os.system("clear")
    LOGO()
    print(c('0. sudo apt update && sudo apt upgrade', 'green'))
    print(c('1. install', 'green'))
    print(c('2. check update tools', 'green'))
    print(c('3. hacking', 'green'))
    print(c('4. exploit', 'green'))
    print(c('5. forensic', 'green'))
    print(c('00. exit'))
    menu = input(DracOS)
    if menu == '4':
    	fluxion()
    elif menu == '0':
        var = input('sudo apt update && sudo apt upgrade(y/n)? ')
        if var == 'y': 
                os.system('sudo apt update && sudo apt upgrade')
        else:
            back()
    elif menu == '1':
    	print()
    	back()
    elif menu == '3':
        hacking()
        # back()
        
    elif menu == '00':
    	sys.exit()    
    elif menu == 'clear':
    	os.system('clear')
    	back()	
        # os.system("python3 sh/a.py")
        # os.system('mkdir tools')
        # os.system('cd tools')
        # os.system('sudo apt update')
        # os.system
        # os.system('')
        # os.system("sudo bash /home/faiz/hacking/fluxionOLD/fluxion")
        
        #else:
        #	print('your failed!')

global DracOS
DracOS = (c('[','green')+c('DracOS','red')+c(']select>','green'))

def hacking():
    LOGO()
    print(c('MENU:\n'
    '1. fluxion\n'
    '2. The Fatrat', 'green'
    ))
    print('00. exit')
    menu = input(DracOS)
    if menu == '1':
        print('fluxionOLD')
    elif menu == '2':
        print('the fatrat')
    elif menu == '0':
        exit()
    
def fluxion():
    os.system('''
    cd fluxionOLD/
    sudo ./fluxion
    ''')


def back():
    data()

while True:
	data()
