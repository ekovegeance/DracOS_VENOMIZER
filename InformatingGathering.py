import os
from color import*
import Logo

# 
def InfoGat():
    os.system('clear')
    Logo.logo_5()
    print(G(""" 
    1.  Nmap
    2.  Amap
    3.  Whatweb
    4.  Sublist3r
    5.  Arp-scan
    6.  Automater
    7.  Braa
    8.  Casefile
    9.  Cdpsnarf
    10. Cisco-torch
    0.  back """))
    print(R('    00. exit'))
    menu = input(G('[')+R('DracOS')+G(']select>'))
    if menu == '1':
        # fungsi yang dipanggil
        nmap()              
    elif menu == '2':
        # fungsi yang dipanggil
        amap()
    elif menu == '3':
        # fungsi yang dipanggil
        whatweb()
    elif menu == '4':
        # fungsi yang dipanggil
        sublist3r()
    elif menu == '5':
        # fungsi yang dipanggil
        arp_scan()
    elif menu == '6':
        # fungsi yang dipanggil
        automater()
    elif menu == '7':
        # fungsi yang dipanggil
        braa()
    elif menu == '8':
        # fungsi yang dipanggil
        casefile()
    elif menu == '9':
        # fungsi yang dipanggil
        cdpsnarf()
    elif menu == '10':
        # fungsi yang dipanggil
        cisco_torch()        
    elif menu == '0':
        os.system('python3 $HOME/git/DracOS_VENOMIZER/venomizer.py') # /usr/bin/
    elif menu == '00':
        exit()

# tambah fungsi tools lalu panggil ke dalam fungsi InfoGat
#NMAP
def nmap():
    if os.path.isfile('/usr/bin/nmap'):
        os.system('clear')
        print(B("Tools Available"))
        input()
    else:
        os.system('xterm -T "☣ INSTALL NMAP ☣" -geometry 100x30 -e "sudo apt install nmap"')
        os.system('clear')
        print(B("NMAP Already Installed"))
        input()
    # end NMAP
#AMAP
def amap():
    if os.path.isfile('/usr/bin/amap'):
        os.system('clear')
        print(B("Tools Available"))
        input()
    else:
        os.system('xterm -T "☣ INSTALL AMAP ☣" -geometry 100x30 -e "sudo apt install amap"')
        os.system('clear')
        print(B("AMAP Already Installed"))
        input()
    # end AMAP

#WHATWEB
def whatweb():
    if os.path.isfile('/usr/bin/whatweb'):
        os.system('clear')
        print(B("Tools Available"))
        input()
    else:
        os.system('xterm -T "☣ INSTALL WHATWEB ☣" -geometry 100x30 -e "sudo apt install whatweb"')
        os.system('clear')
        print(B("WHATWEB Already Installed"))
        input()
    # end WHATWEB

#Sublist3r
def sublist3r():
    if os.path.isfile('/usr/bin/sublist3r'):
        os.system('clear')
        print(B("Tools Available"))
        input()
    else:
        os.system('xterm -T "☣ INSTALL Sublist3r ☣" -geometry 100x30 -e "sudo apt install sublist3r"')
        os.system('clear')
        print(B("Sublist3r Already Installed"))
        input()
    # end Sublist3r    

#arp-scan
def arp_scan():
    if os.path.isfile('/usr/bin/arp-scan'):
        os.system('clear')
        print(B("Tools Available"))
        input()
    else:
        os.system('xterm -T "☣ INSTALL ARP-SCAN ☣" -geometry 100x30 -e "sudo apt install arp-scan"')
        os.system('clear')
        print(B("ARP-SCAN Already Installed"))
        input()
    # end ARP-SCAN

#Automater
def automater():
    if os.path.isfile('/usr/bin/automater'):
        os.system('clear')
        print(B("Tools Available"))
        input()
    else:
        os.system('xterm -T "☣ INSTALL Automater ☣" -geometry 100x30 -e "sudo apt install automater"')
        os.system('clear')
        print(B("Automater Already Installed"))
        input()
    # end Automater

#Braa
def braa():
    if os.path.isfile('/usr/bin/braa'):
        os.system('clear')
        print(B("Tools Available"))
        input()
    else:
        os.system('xterm -T "☣ INSTALL Braa ☣" -geometry 100x30 -e "sudo apt install braa"')
        os.system('clear')
        print(B("Braa Already Installed"))
        input()
    # end Braa

#Casefile
def casefile():
    if os.path.isfile('/usr/bin/casefile'):
        os.system('clear')
        print(B("Tools Available"))
        input()
    else:
        os.system('xterm -T "☣ INSTALL Casefile ☣" -geometry 100x30 -e "sudo apt install casefile"')
        os.system('clear')
        print(B("Casefile Already Installed"))
        input()
    # end Casefile

#Cdpsnarf
def cdpsnarf():
    if os.path.isfile('/usr/bin/cdpsnarf'):
        os.system('clear')
        print(B("Tools Available"))
        input()
    else:
        os.system('xterm -T "☣ INSTALL Cdpsnarf ☣" -geometry 100x30 -e "sudo apt install cdpsnarf"')
        os.system('clear')
        print(B("Cdpsnarf Already Installed"))
        input()
    # end Cdpsnarf

#Cisco-torch
def cisco_torch():
    if os.path.isfile('/usr/bin/cisco-torch'):
        os.system('clear')
        print(B("Tools Available"))
        input()
    else:
        os.system('xterm -T "☣ INSTALL Cisco-torch ☣" -geometry 100x30 -e "sudo apt install cisco-torch"')
        os.system('clear')
        print(B("Cisco-torch Already Installed"))
        input()
    # end Cisco-torch




#Looping
while True:
    InfoGat()
        