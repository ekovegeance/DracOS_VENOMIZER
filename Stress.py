#! usr/share/bin/python3
#! -*- coding: utf-8 -*-
#! Stress.py
import os
from color import *
import Logo

def Stress():
    os.system("clear")
    Logo.logo_14()
    print(
        G(
            """
    1.  DHCPig
    2.  FunkLoad
    3.  iaxflood
    4.  Inundator
    5.  inviteflood
    6.  ipv6toolkit
    7.  mdk3
    8.  Reaver
    9.  rtpflood
    10. SlowHTTPTest
    11. t50
    12. Termineter
    13. THC-IPV6
    14. THC-SSL-DOS
    0.  Back to main menu        
            """
        )
    )
    print(R("    00. exit"))
    menu = input(G("[") + R("DracOS") + G("]select>"))
    if menu == "1":
        # Call function
        DHCPig()
    elif menu == "2":
        # Call function
        FunkLoad()
    elif menu == "3":
        # Call function
        iaxflood()
    elif menu == "4":
        # Call function
        Inundator()
    elif menu == "5":
        # Call function
        inviteflood()
    elif menu == "6":
        # Call function
        ipv6toolkit()
    elif menu == "7":
        # Call function
        mdk3()
    elif menu == "8":
        # Call function
        Reaver()
    elif menu == "9":
        # Call function
        rtpflood()
    elif menu == "10":
        # Call function
        SlowHTTPTest()
    elif menu == "11":
        # Call function
        t50()
    elif menu == "12":
        # Call function
        Termineter()
    elif menu == "13":
        # Call function
        THC_IPV6()
    elif menu == "14":
        # Call function
        THC_SSL_DOS()
    elif menu == "0":
        os.system("python3 $HOME/git/DracOS_VENOMIZER/venomizer.py")  # /usr/bin/
    elif menu == "00":
        exit()




#Funciton
# DHCPig
def DHCPig():
    if os.path.isfile("usr/bin/dhcpig"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL DHCPig ☣" -geometry 100x30 -e "sudo apt install dhcpig"'
        )
        os.system("clear")
        print(B("DHCPig Already Installed"))
        input()
    # end DHCPig

#FunkLoad
def FunkLoad():
    if os.path.isfile("usr/bin/funkload"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL FunkLoad ☣" -geometry 100x30 -e "sudo apt install funkload"'
        )
        os.system("clear")
        print(B("FunkLoad Already Installed"))
        input()
    # end FunkLoad

#iaxflood
def iaxflood():
    if os.path.isfile("usr/bin/iaxflood"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL iaxflood ☣" -geometry 100x30 -e "sudo apt install iaxflood"'
        )
        os.system("clear")
        print(B("iaxflood Already Installed"))
        input()
    # end iaxflood

#Inundator
def Inundator():
    if os.path.isfile("usr/bin/inundator"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Inundator ☣" -geometry 100x30 -e "sudo apt install inundator"'
        )
        os.system("clear")
        print(B("Inundator Already Installed"))
        input()
    # end Inundator

#inviteflood
def inviteflood():
    if os.path.isfile("usr/bin/inviteflood"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL inviteflood ☣" -geometry 100x30 -e "sudo apt install inviteflood"'
        )
        os.system("clear")
        print(B("inviteflood Already Installed"))
        input()
    # end inviteflood

#ipv6toolkit
def ipv6toolkit():
    if os.path.isfile("usr/bin/ipv6toolkit"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL ipv6toolkit ☣" -geometry 100x30 -e "sudo apt install ipv6toolkit"'
        )
        os.system("clear")
        print(B("ipv6toolkit Already Installed"))
        input()
    # end ipv6toolkit

#mdk3
def mdk3():
    if os.path.isfile("usr/bin/mdk3"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL mdk3 ☣" -geometry 100x30 -e "sudo apt install mdk3"'
        )
        os.system("clear")
        print(B("mdk3 Already Installed"))
        input()
    # end mdk3

#Reaver
def Reaver():
    if os.path.isfile("usr/bin/reaver"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Reaver ☣" -geometry 100x30 -e "sudo apt install reaver"'
        )
        os.system("clear")
        print(B("Reaver Already Installed"))
        input()
    # end Reaver

#rtpflood
def rtpflood():
    if os.path.isfile("usr/bin/rtpflood"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL rtpflood ☣" -geometry 100x30 -e "sudo apt install rtpflood"'
        )
        os.system("clear")
        print(B("rtpflood Already Installed"))
        input()
    # end rtpflood

#SlowHTTPTest
def SlowHTTPTest():
    if os.path.isfile("usr/bin/slowhttptest"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL SlowHTTPTest ☣" -geometry 100x30 -e "sudo apt install slowhttptest"'
        )
        os.system("clear")
        print(B("SlowHTTPTest Already Installed"))
        input()
    # end SlowHTTPTest

#t50
def t50():
    if os.path.isfile("usr/bin/t50"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL t50 ☣" -geometry 100x30 -e "sudo apt install t50"'
        )
        os.system("clear")
        print(B("t50 Already Installed"))
        input()
    # end t50

#Termineter
def Termineter():
    if os.path.isfile("usr/bin/termineter"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Termineter ☣" -geometry 100x30 -e "sudo apt install termineter"'
        )
        os.system("clear")
        print(B("Termineter Already Installed"))
        input()
    # end Termineter

#THC-IPV6
def THC_IPV6():
    if os.path.isfile("usr/bin/thc-ipv6"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL THC-IPV6 ☣" -geometry 100x30 -e "sudo apt install thc-ipv6"'
        )
        os.system("clear")
        print(B("THC-IPV6 Already Installed"))
        input()
    # end THC-IPV6

#THC-SSL-DOS
def THC_SSL_DOS():
    if os.path.isfile("usr/bin/thc-ssl-dos"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL THC-SSL-DOS ☣" -geometry 100x30 -e "sudo apt install thc-ssl-dos"'
        )
        os.system("clear")
        print(B("THC-SSL-DOS Already Installed"))
        input()
    # end THC-SSL-DOS          


while True:
    Stress()