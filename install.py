from os import path
import os
from color import*

def I():
    print(G('[OK!]installed'))
def N():
    print(R('[NO!]installed'))


global DracOS
DracOS = G('[')+R('DracOS')+G(']select> ')

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
    menu = input(DracOS)
    if menu == '1':
        print(G(""" 
        [ HACKING ]
        MENU:
        1. install fluxion
        2. install fatrat
        0. back """))
        menu = input(DracOS)
        if menu == '1':
            m = input('Do you want install FluxionOLD(y/n)? ')
            if m == 'y' or m == 'Y':
                # cek dulu ya! jika folder fluxion sudah ada, berarti sudah kita install
                # kenapa sudah diinstall karena folder tersebut hasil dari clone
                if os.path.isdir('/usr/bin/VENOMIZER/fluxion/'):
                    print(G('status installed!'))
                
                # jika folder kosong! 
                else:
                    # cek apakah folder VENOMIZER sudah dibuat?
                    # jika sudah langsung di clone dalam folder VENOMIZER
                    if os.path.isdir('/usr/bin/VENOMIZER'):
                        os.system(""" 
                        cd /usr/bin/VENOMIZER
                        sudo git clone https://github.com/FluxionNetwork/fluxion.git """)
                        print(G('success installed!'))
                    
                    # jika belum maka kita buat direktori terlebih dahulu
                    else:
                        # buat direktori VENOMIZER
                        os.system(""" 
                        mkdir /usr/bin/VENOMIZER """)
                        # masuk ke direktori lalu clone
                        os.system(""" 
                        cd /usr/bin/VENOMIZER
                        sudo git clone https://github.com/FluxionNetwork/fluxion.git """)
                        print(G('success installed!'))
            elif m == 'n' or m == 'N':
                print('')
                os.system('clear')
        
    elif menu == '0':
        os.system('python3 /home/faiz/git/DracOS_VENOMIZER/venomizer.py')