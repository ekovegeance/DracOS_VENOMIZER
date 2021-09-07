import os.path
from os import*
from color import*
def I():
    print(G('[OK!]installed'))
def N():
    print(R('[NO!]installed'))
#cek folder 
if os.path.isfile('/home/faiz/git/DracOS_VENOMIZER/hack.p'):
    system('clear')
    I()
else:
    system('clear')
    N()
    a = input('Do you want to install pygame(y/n)? ')
    if a == 'y' or a == 'Y':
        system('pip install pygame')
    else:
        print('Not installed')