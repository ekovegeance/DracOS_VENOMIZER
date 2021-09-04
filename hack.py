# from termcolor import colored as c
import os
import sys
import Logo
from color import*
# import os.path
# from os import path


# def LOGO_hacking():
#     os.system('clear')
#     Logo.logo_8()
    # print(c('____   ____     _____      _______  ___  _______ __    ___________   ','red'))
    # print(c('|   |  |   |   /  _   \   /  ___  /|  | / |_   _|  \  |  |   _____ \ ','red'))
    # print(c('|   |__|   |  /  /__\  \ |  |   |  |  |/  / | | |   \ |  |  /   ___  ','red'))
    # print(c('|    __    | /   ____   \|  |   |  |     x  | | |    \|  |  |  |_  \ ','red'))
    # print(c('|   |  |   |/   /    \   \   \__---|  |\  \_| |_|  |\    |   \__|  | ','red'))
    # print(c('|___|  |___|___/      \___\_______/|__| \__\____|__| \__ |\______  / ','red'))


def hacking():
    # LOGO_hacking()
    Logo.logo_8()
    print(G('1. fluxion\n'
    '2. the fatrat\n'
    '0. back'))
    print('00. exit')
    menu = input(G('[')+R('DracOS')+G(']select> '))
    if menu == '1':
        fluxion()
    elif menu == '2':
        fatrat()
    elif menu == '0':
        os.system('python3 venomizer.py')
        

def fatrat():
    os.system('sudo fatrat')


def fluxion():
    os.system('''
    cd fluxionOLD/
    sudo ./fluxion
    ''')



