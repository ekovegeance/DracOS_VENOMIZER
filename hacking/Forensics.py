#!/usr/bin/python3
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
        os.system("python3 /usr/bin/DracOS_VENOMIZER/venomizer.py")  # //usr/bin/
    elif menu == "00":
        exit()
    else:
        print(R('Wrong Input!'))
        input()
        back()




def back():
    Forensics()

#Function
#Binwalk
def Binwalk():
    if os.path.isfile("/usr/bin/binwalk"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Binwalk ☣" -geometry 100x30 -e "sudo apt install binwalk"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/binwalk"):
            print(B("Binwalk Already Installed"))
        else:
            print(R("Not Installing Binwalk"))
    input()
    back()
    # end Binwalk

#Bulk Extractor
def BulkExtractor():
    if os.path.isfile("/usr/bin/bulk_extractor"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Bulk Extractor ☣" -geometry 100x30 -e "sudo apt install bulk_extractor"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/bulk_extractor"):
            print(B("Bulk Extractor Already Installed"))
        else:
            print(R("Not Installing Bulk Extractor"))
    input()
    back()
    # end Bulk Extractor

#Capstone
def Capstone():
    if os.path.isfile("/usr/bin/capstone"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Capstone ☣" -geometry 100x30 -e "sudo apt install capstone"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/capstone"):
            print(B("Capstone Already Installed"))
        else:
            print(R("Not Installing Capstone"))
    input()
    back()
        # end Capstone

#Chntpw
def Chntpw():
    if os.path.isfile("/usr/bin/chntpw"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Chntpw ☣" -geometry 100x30 -e "sudo apt install chntpw"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/chntpw"):
            print(B("Chntpw Already Installed"))
        else:
            print(R("Not Installing Chntpw"))
    input()
    back()

#Cuckoo
def Cuckoo():
    if os.path.isfile("/usr/bin/cuckoo"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Cuckoo ☣" -geometry 100x30 -e "sudo apt install cuckoo"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/cuckoo"):
            print(B("Cuckoo Already Installed"))
        else:
            print(R("Not Installing Cuckoo"))
    input()
    back()
    # end Cuckoo

#Dc3dd
def Dc3dd():
    if os.path.isfile("/usr/bin/dc3dd"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Dc3dd ☣" -geometry 100x30 -e "sudo apt install dc3dd"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/dc3dd"):
            print(B("Dc3dd Already Installed"))
        else:
            print(R("Not Installing Dc3dd"))
    input()
    back()
        # end Dc3dd

#DDrescue
def DDrescue():
    if os.path.isfile("/usr/bin/ddrescue"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL DDrescue ☣" -geometry 100x30 -e "sudo apt install ddrescue"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/ddrescue"):
            print(B("DDrescue Already Installed"))
        else:
            print(R("Not Installing DDrescue"))
    input()
    back()
    # end DDrescue

#DFF
def DFF():
    if os.path.isfile("/usr/bin/dff"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL DFF ☣" -geometry 100x30 -e "sudo apt install dff"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/dff"):
            print(B("DFF Already Installed"))
        else:
            print(R("Not Installing DFF"))
    input()
    back()
    # end DFF

#DiStorm3
def DiStorm3():
    if os.path.isfile("/usr/bin/distorm3"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL DiStorm3 ☣" -geometry 100x30 -e "sudo apt install distorm3"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/distorm3"):
            print(B("DiStorm3 Already Installed"))
        else:
            print(R("Not Installing DiStorm3"))
    input()
    back()
    # end DiStorm3

#Dumpzilla
def Dumpzilla():
    if os.path.isfile("/usr/bin/dumpzilla"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Dumpzilla ☣" -geometry 100x30 -e "sudo apt install dumpzilla"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/dumpzilla"):
            print(B("Dumpzilla Already Installed"))
        else:
            print(R("Not Installing Dumpzilla"))
    input()
    back()
    # end Dumpzilla

#Extundelete
def Extundelete():
    if os.path.isfile("/usr/bin/extundelete"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Extundelete ☣" -geometry 100x30 -e "sudo apt install extundelete"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/extundelete"):
            print(B("Extundelete Already Installed"))
        else:
            print(R("Not Installing Extundelete"))
    input()
    back()
    # end Extundelete

#Foremost
def Foremost():
    if os.path.isfile("/usr/bin/foremost"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Foremost ☣" -geometry 100x30 -e "sudo apt install foremost"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/foremost"):
            print(B("Foremost Already Installed"))
        else:
            print(R("Not Installing Foremost"))
    input()
    back()
    # end Foremost

#Galleta
def Galleta():
    if os.path.isfile("/usr/bin/galleta"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Galleta ☣" -geometry 100x30 -e "sudo apt install galleta"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/galleta"):
            print(B("Galleta Already Installed"))
        else:
            print(R("Not Installing Galleta"))
    input()
    back()
    # end Galleta

#Guymager
def Guymager():
    if os.path.isfile("/usr/bin/guymager"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Guymager ☣" -geometry 100x30 -e "sudo apt install guymager"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/guymager"):
            print(B("Guymager Already Installed"))
        else:
            print(R("Not Installing Guymager"))
    input()
    back()
    # end Guymager

#IPhone Backup Analyzer
def IPhone():
    if os.path.isfile("/usr/bin/iphonebackupanalyzer"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL IPhone Backup Analyzer ☣" -geometry 100x30 -e "sudo apt install iphonebackupanalyzer"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/iphonebackupanalyzer"):
            print(B("IPhone Backup Analyzer Already Installed"))
        else:
            print(R("Not Installing IPhone Backup Analyzer"))
    input()
    back()
    # end IPhone Backup Analyzer

#P0f
def P0f():
    if os.path.isfile("/usr/bin/p0f"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL P0f ☣" -geometry 100x30 -e "sudo apt install p0f"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/p0f"):
            print(B("P0f Already Installed"))
        else:
            print(R("Not Installing P0f"))
    input()
    back()
    # end P0f

#Pdf-parser
def Pdf():
    if os.path.isfile("/usr/bin/pdf-parser"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Pdf-parser ☣" -geometry 100x30 -e "sudo apt install pdf-parser"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/pdf-parser"):
            print(B("Pdf-parser Already Installed"))
        else:
            print(R("Not Installing Pdf-parser"))
    input()
    back()
    # end Pdf-parser

#Pdfid
def Pdfid():
    if os.path.isfile("/usr/bin/pdfid"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Pdfid ☣" -geometry 100x30 -e "sudo apt install pdfid"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/pdfid"):
            print(B("Pdfid Already Installed"))
        else:
            print(R("Not Installing Pdfid"))
    input()
    back()
    # end Pdfid

#Pdgmail
def Pdgmail():
    if os.path.isfile("/usr/bin/pdgmail"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Pdgmail ☣" -geometry 100x30 -e "sudo apt install pdgmail"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/pdgmail"):
            print(B("Pdgmail Already Installed"))
        else:
            print(R("Not Installing Pdgmail"))
    input()
    back()
    # end Pdgmail

#Peepdf
def Peepdf():
    if os.path.isfile("/usr/bin/peepdf"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Peepdf ☣" -geometry 100x30 -e "sudo apt install peepdf"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/peepdf"):
            print(B("Peepdf Already Installed"))
        else:
            print(R("Not Installing Peepdf"))
    input()
    back()
    # end Peepdf

#RegRipper
def Regripper():
    if os.path.isfile("/usr/bin/regripper"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL RegRipper ☣" -geometry 100x30 -e "sudo apt install regripper"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/regripper"):
            print(B("RegRipper Already Installed"))
        else:
            print(R("Not Installing RegRipper"))
    input()
    back()
    # end RegRipper

#Volatility
def Volatility():
    if os.path.isfile("/usr/bin/volatility"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Volatility ☣" -geometry 100x30 -e "sudo apt install volatility"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/volatility"):
            print(B("Volatility Already Installed"))
        else:
            print(R("Not Installing Volatility"))
    input()
    back()
    # end Volatility

#Xplico
def Xplico():
    if os.path.isfile("/usr/bin/xplico"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Xplico ☣" -geometry 100x30 -e "sudo apt install xplico"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/xplico"):
            print(B("Xplico Already Installed"))
        else:
            print(R("Not Installing Xplico"))
    input()
    back()
    # end Xplico


# Looping
# while True:
#     Forensics()