import os
from color import*
import Logo
import sys
# menu/eksploit--5
# os.system('clear')
def eksploit():
    os.system('clear')
    Logo.logo_9()
    # while True:
    print(G('menu\n1. tools\n2. tools2\n0. back'))
    print('00. exit')
    menu = input(G('[')+R('DracOS')+G(']> '))
    if menu == '1':
        print()
    elif menu == '2':
        print()
    elif menu == '0':
        # sys.exit()
        os.system('python3 venomizer.py')
    elif menu == '00':
        exit()