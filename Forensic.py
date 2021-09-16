#! usr/share/bin/python3
#! -*- coding: utf-8 -*-
#! PasswordAttack.py
import os
from color import *
import Logo

def Forensics():
    os.system("clear")
    Logo.logo_18()
    print(
        G(
            """
    1.  Binwalk
    2.  Bulk Extractor
    3.  Capstone
    4.  Chntpw
    5.  Cuckoo
    6.  Dc3dd
    7.  DDrescue
    8.  DFF
    9.  DiStorm3
    10. Dumpzilla
    11. Extundelete
    12. Foremost
    13. Galleta
    14. Guymager
    15. IPhone Backup Analyzer
    16. P0f
    17. Pdf-parser
    18. Pdfid
    19. Pdgmail
    20. Peepdf
    21. RegRipper
    22. Volatility
    23. Xplico
    0.  Back to Main Menu
            """
        )
    )
    print(R("    00. exit"))
    menu = input(G("[") + R("DracOS") + G("]select>"))
    if menu == "1":
        # Call function
        Binwalk()
    elif menu == "2":
        # Call function
        BulkExtractor()
    elif menu == "3":
        # Call function
        Capstone()
    elif menu == "4":
        # Call function
        Chntpw()
    elif menu == "5":
        # Call function
        Cuckoo()
    elif menu == "6":
        # Call function
        Dc3dd()
    elif menu == "7":
        # Call function
        DDrescue()
    elif menu == "8":
        # Call function
        DFF()
    elif menu == "9":
        # Call function
        DiStorm3()
    elif menu == "10":
        # Call function
        Dumpzilla()
    elif menu == "11":
        # Call function
        Extundelete()
    elif menu == "12":
        # Call function
        Foremost()
    elif menu == "13":
        # Call function
        Galleta()
    elif menu == "14":
        # Call function
        Guymager()
    elif menu == "15":
        # Call function
        IPhone()
    elif menu == "16":
        # Call function
        P0f()
    elif menu == "17":
        # Call function
        Pdf()
    elif menu == "18":
        # Call function
        Pdfid()
    elif menu == "19":
        # Call function
        Pdgmail()
    elif menu == "20":
        # Call function
        Peepdf()
    elif menu == "21":
        # Call function
        Regripper()
    elif menu == "22":
        # Call function
        Volatility()
    elif menu == "23":
        # Call function
        Xplico()
    elif menu == "0":
        os.system("python3 $HOME/git/DracOS_VENOMIZER/venomizer.py")  # /usr/bin/
    elif menu == "00":
        exit()






#Function
#Binwalk
def Binwalk():
    if os.path.isfile("usr/bin/binwalk"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Binwalk ☣" -geometry 100x30 -e "sudo apt install binwalk"'
        )
        os.system("clear")
        print(B("Binwalk Already Installed"))
        input()
    # end Binwalk

#Bulk Extractor
def BulkExtractor():
    if os.path.isfile("usr/bin/bulk_extractor"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Bulk Extractor ☣" -geometry 100x30 -e "sudo apt install bulk_extractor"'
        )
        os.system("clear")
        print(B("Bulk Extractor Already Installed"))
        input()
    # end Bulk Extractor

#Capstone
def Capstone():
    if os.path.isfile("usr/bin/capstone"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Capstone ☣" -geometry 100x30 -e "sudo apt install capstone"'
        )
        os.system("clear")
        print(B("Capstone Already Installed"))
        input()
    # end Capstone

#Chntpw
def Chntpw():
    if os.path.isfile("usr/bin/chntpw"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Chntpw ☣" -geometry 100x30 -e "sudo apt install chntpw"'
        )
        os.system("clear")
        print(B("Chntpw Already Installed"))
        input()
    # end Chntpw

#Cuckoo
def Cuckoo():
    if os.path.isfile("usr/bin/cuckoo"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Cuckoo ☣" -geometry 100x30 -e "sudo apt install cuckoo"'
        )
        os.system("clear")
        print(B("Cuckoo Already Installed"))
        input()
    # end Cuckoo

#Dc3dd
def Dc3dd():
    if os.path.isfile("usr/bin/dc3dd"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Dc3dd ☣" -geometry 100x30 -e "sudo apt install dc3dd"'
        )
        os.system("clear")
        print(B("Dc3dd Already Installed"))
        input()
    # end Dc3dd

#DDrescue
def DDrescue():
    if os.path.isfile("usr/bin/ddrescue"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL DDrescue ☣" -geometry 100x30 -e "sudo apt install ddrescue"'
        )
        os.system("clear")
        print(B("DDrescue Already Installed"))
        input()
    # end DDrescue

#DFF
def DFF():
    if os.path.isfile("usr/bin/dff"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL DFF ☣" -geometry 100x30 -e "sudo apt install dff"'
        )
        os.system("clear")
        print(B("DFF Already Installed"))
        input()
    # end DFF

#DiStorm3
def DiStorm3():
    if os.path.isfile("usr/bin/distorm3"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL DiStorm3 ☣" -geometry 100x30 -e "sudo apt install distorm3"'
        )
        os.system("clear")
        print(B("DiStorm3 Already Installed"))
        input()
    # end DiStorm3

#Dumpzilla
def Dumpzilla():
    if os.path.isfile("usr/bin/dumpzilla"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Dumpzilla ☣" -geometry 100x30 -e "sudo apt install dumpzilla"'
        )
        os.system("clear")
        print(B("Dumpzilla Already Installed"))
        input()
    # end Dumpzilla

#Extundelete
def Extundelete():
    if os.path.isfile("usr/bin/extundelete"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Extundelete ☣" -geometry 100x30 -e "sudo apt install extundelete"'
        )
        os.system("clear")
        print(B("Extundelete Already Installed"))
        input()
    # end Extundelete

#Foremost
def Foremost():
    if os.path.isfile("usr/bin/foremost"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Foremost ☣" -geometry 100x30 -e "sudo apt install foremost"'
        )
        os.system("clear")
        print(B("Foremost Already Installed"))
        input()
    # end Foremost

#Galleta
def Galleta():
    if os.path.isfile("usr/bin/galleta"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Galleta ☣" -geometry 100x30 -e "sudo apt install galleta"'
        )
        os.system("clear")
        print(B("Galleta Already Installed"))
        input()
    # end Galleta

#Guymager
def Guymager():
    if os.path.isfile("usr/bin/guymager"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Guymager ☣" -geometry 100x30 -e "sudo apt install guymager"'
        )
        os.system("clear")
        print(B("Guymager Already Installed"))
        input()
    # end Guymager

#IPhone Backup Analyzer
def IPhone():
    if os.path.isfile("usr/bin/iphonebackupanalyzer"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL IPhone Backup Analyzer ☣" -geometry 100x30 -e "sudo apt install iphonebackupanalyzer"'
        )
        os.system("clear")
        print(B("IPhone Backup Analyzer Already Installed"))
        input()
    # end IPhone Backup Analyzer

#P0f
def P0f():
    if os.path.isfile("usr/bin/p0f"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL P0f ☣" -geometry 100x30 -e "sudo apt install p0f"'
        )
        os.system("clear")
        print(B("P0f Already Installed"))
        input()
    # end P0f

#Pdf-parser
def Pdf():
    if os.path.isfile("usr/bin/pdf-parser"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Pdf-parser ☣" -geometry 100x30 -e "sudo apt install pdf-parser"'
        )
        os.system("clear")
        print(B("Pdf-parser Already Installed"))
        input()
    # end Pdf-parser

#Pdfid
def Pdfid():
    if os.path.isfile("usr/bin/pdfid"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Pdfid ☣" -geometry 100x30 -e "sudo apt install pdfid"'
        )
        os.system("clear")
        print(B("Pdfid Already Installed"))
        input()
    # end Pdfid

#Pdgmail
def Pdgmail():
    if os.path.isfile("usr/bin/pdgmail"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Pdgmail ☣" -geometry 100x30 -e "sudo apt install pdgmail"'
        )
        os.system("clear")
        print(B("Pdgmail Already Installed"))
        input()
    # end Pdgmail

#Peepdf
def Peepdf():
    if os.path.isfile("usr/bin/peepdf"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Peepdf ☣" -geometry 100x30 -e "sudo apt install peepdf"'
        )
        os.system("clear")
        print(B("Peepdf Already Installed"))
        input()
    # end Peepdf

#RegRipper
def Regripper():
    if os.path.isfile("usr/bin/regripper"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL RegRipper ☣" -geometry 100x30 -e "sudo apt install regripper"'
        )
        os.system("clear")
        print(B("RegRipper Already Installed"))
        input()
    # end RegRipper

#Volatility
def Volatility():
    if os.path.isfile("usr/bin/volatility"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Volatility ☣" -geometry 100x30 -e "sudo apt install volatility"'
        )
        os.system("clear")
        print(B("Volatility Already Installed"))
        input()
    # end Volatility

#Xplico
def Xplico():
    if os.path.isfile("usr/bin/xplico"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Xplico ☣" -geometry 100x30 -e "sudo apt install xplico"'
        )
        os.system("clear")
        print(B("Xplico Already Installed"))
        input()
    # end Xplico





# Looping
while True:
    Forensics()