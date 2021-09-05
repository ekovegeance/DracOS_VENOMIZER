import os
from color import*
import Logo

def socialengineering():
    print(G(""" 
    1. ...
    2. ...
    0. back """))
    print('00. exit')
    menu = input(G('[')+R('DracOS')+G(']select>'))
    if menu == '1':
        print('')
    elif menu == '2':
        print('')
    elif menu == '0':
        os.system('python3 venomizer.py')
    elif menu == '00':
        exit()