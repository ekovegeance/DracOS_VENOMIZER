#! usr/share/bin/python3
from termcolor import colored as c
import os
import sys
# import os.path
# from os import path
import hack, eksploit#, forensic, SocialEngineering



global DracOS
DracOS = c('[','green')+c('DracOS','red')+c(']> ','green')
 
# logo constant
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


# def LOGO_hacking():
#     os.system('clear')
#     print(c('[','green')+c('GROUP', 'red')+c(']','green'))
#     print(c('____   ____     _____      _______  ___  _______ __    ___________   ','red'))
#     print(c('|   |  |   |   /  _   \   /  ___  /|  | / |_   _|  \  |  |   _____ \ ','red'))
#     print(c('|   |__|   |  /  /__\  \ |  |   |  |  |/  / | | |   \ |  |  /   ___  ','red'))
#     print(c('|    __    | /   ____   \|  |   |  |     x  | | |    \|  |  |  |_  \ ','red'))
#     print(c('|   |  |   |/   /    \   \   \__---|  |\  \_| |_|  |\    |   \__|  | ','red'))
#     print(c('|___|  |___|___/      \___\_______/|__| \__\____|__| \__ |\______  / ','red'))

def menu():
    # call logo
    LOGO()
    print(c('0. sudo apt update', 'green'))
    print(c('1. sudo apt upgrade', 'green'))
    print(c('2. Install', 'green'))
    print(c('3. Check Update Tools', 'green'))
    print(c('4. Hacking', 'green'))
    print(c('5. Exploit', 'green'))
    print(c('6. Forensic', 'green'))
    print(c('7. Social Engineering', 'green'))
    print(c('8. Informating Gathering', 'green'))
    print(c('9. Password Attack', 'green'))
    print(c('10. web application analysis', 'green'))
    print(c('11. database assesment', 'green'))
    print(c('12. wireless attacks', 'green'))
    print(c('13. post eksploitation', 'green'))
    print(c('00. exit'))
    menu = input(DracOS)
    if menu == '0':
        var = input('sudo apt update(y/n)? ')
        if var == 'y': 
                os.system('sudo apt update')
        else:
            back()
    elif menu == '1':
        var = input('sudo apt upgrade(y/n)? ')
        if var == 'y':
            os.system('sudo apt upgrade')
        else:
            back()
    # elif menu == '2':
        # install()
        # back()
    # elif menu == '3':
    #     check_update_tools()
    elif menu == '4':
        hack.hacking()
    elif menu == '5':
        eksploit.eksploit()
    # elif menu == '6':
    #     forensic()
    # elif menu == '7':
    #     forensic()
    # elif menu == '8':
    #     social_engineering()
    # elif menu == '9':
    #     informating_gathering()
    # elif menu == '10':
    #     password_attack()
    # elif menu == '11':
    #     web_application_analysis()
    # elif menu == '12':
    #     wireless_attack()
    # elif menu == '13':
    #     post_eksploitation()
    elif menu == '00':
        os.system('exit')
        sys.exit()
        exit()
    elif menu == 'clear':
        os.system('clear')
        back()


def back():
    menu()


while True:
    menu()