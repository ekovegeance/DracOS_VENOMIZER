import os
from color import*
import Logo

# 
def InfoGat():
    os.system('clear')
    print(G(""" 
    1. ...
    2. ...
    0. back """))
    print('00. exit')
    menu = input(G('[')+R('DracOS')+G(']select>'))
    if menu == '1':
        print('')
        # fungsi yang dipanggil
    elif menu == '2':
        print('')
        # fungsi yang dipanggil
    elif menu == '0':
        os.system('python3 $HOME/git/DracOS_VENOMIZER/venomizer.py') # /usr/bin/
    elif menu == '00':
        exit()

# tambah fungsi tools lalu panggil ke dalam fungsi InfoGat


while True:
    InfoGat()
        