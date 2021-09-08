from os import path
import os
from color import*

def install():
    print(G(""" 
    menu:
    1. hacking
    2. eksploit
    3. forensic
    4. social engineering
    5. informating gathering
    6. password attack
    7. web application analysis
    8. database assesment
    9. wireeless attacks
    10. post exsploitation
    0. back
    """))
    print('00. exit')
    menu = input(G('[')+R('DracOS')+G(']select> '))
    if menu == '1':
        print(G(""" 
        [ HACKING ]
        MENU:
        1. install fatrat
        2. install fluxion
        0. back """))
        menu = input(G('[')+R('DracOS')+G(']select> '))
        if menu == '1':
            if os.path.isdir('/usr/bin/')