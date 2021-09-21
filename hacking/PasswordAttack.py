#! /usr/share/bin/python3
#! -*- coding: utf-8 -*-
#! PasswordAttack.py
import os
from color import *
import Logo


def PassAtck():
    os.system("clear")
    Logo.logo_15()
    print(
        G(
            """
    1.  BruteSpray        
    2.  Brup Suite
    3.  CeWL
    4.  chntpw
    5.  cisco-auditing-tool
    6.  CmosPwd
    7.  Creddump
    8.  Crowbar
    9.  Crunch
    10. Findmyhash
    11. Gpp-decrypt
    12. Hash-identifier
    13. Hashcat
    14. HexorBase
    15. THC-Hydra
    16. John the Ripper
    17. Johnny
    18. keimpx
    19. Maltego Teeth
    20. Maskprocessor
    21. Multiforcer
    22. Ncrack
    23. Oclgausscrack
    24. Ophcrack
    26. PACK
    27. patator
    28. Phrasendrescher
    29. Polenum
    30. RainbowCrack
    31. Rcracki-mt
    32. RSMangler
    33. SecLists
    34. SQLdict
    35. Statsprocessor
    36. THC-pptp-bruter
    37. TrueCrack
    38. WebScarab
    39. Wordlists
    40. zaproxy        
    0.  Back to Main Menu        
            """
                )
    )
    print(R("    00. exit"))
    menu = input(G("[") + R("DracOS") + G("]select>"))
    if menu == "1":
        # Call function
        BruteSpray()
    elif menu == "2":
        # Call function
        BrupSuite()
    elif menu == "3":
        # Call function
        CeWL()
    elif menu == "4":
        # Call function
        chntpw()
    elif menu == "5":
        # Call function
        cisco_auditing_tool()
    elif menu == "6":
        # Call function
        CmosPwd()
    elif menu == "7":
        # Call function
        Creddump()
    elif menu == "8":
        # Call function
        Crowbar()
    elif menu == "9":
        # Call function
        Crunch()
    elif menu == "10":
        # Call function
        Findmyhash()
    elif menu == "11":
        # Call function
        Gpp_decrypt()
    elif menu == "12":
        # Call function
        Hash_identifier()
    elif menu == "13":
        # Call function
        Hashcat()
    elif menu == "14":
        # Call function
        HexorBase()
    elif menu == "15":
        # Call function
        THC_Hydra()
    elif menu == "16":
        # Call function
        John_the_Ripper()
    elif menu == "17":
        # Call function
        Johnny()
    elif menu == "18":
        # Call function
        keimpx()
    elif menu == "19":
        # Call function
        Maltego_Teeth()
    elif menu == "20":
        # Call function
        Maskprocessor()
    elif menu == "21":
        # Call function
        Multiforcer()
    elif menu == "22":
        # Call function
        Ncrack()
    elif menu == "23":
        # Call function
        Oclgausscrack()
    elif menu == "24":
        # Call function
        Ophcrack()
    elif menu == "25":
        # Call function
        PACK()
    elif menu == "26":
        # Call function
        Patator()
    elif menu == "27":
        # Call function
        Phrasendrescher()
    elif menu == "28":
        # Call function
        Polenum()
    elif menu == "29":
        # Call function
        RainbowCrack()
    elif menu == "30":
        # Call function
        Rcracki_mt()
    elif menu == "31":
        # Call function
        RSMangler()
    elif menu == "32":
        # Call function
        SecLists()
    elif menu == "33":
        # Call function
        SQLdict()
    elif menu == "34":
        # Call function
        Statsprocessor()
    elif menu == "35":
        # Call function
        THC_pptp_bruter()
    elif menu == "36":
        # Call function
        TrueCrack()
    elif menu == "37":
        # Call function
        WebScarab()
    elif menu == "38":
        # Call function
        Wordlists()
    elif menu == "39":
        # Call function
        zaproxy()
    elif menu == "0":
        os.system("python3 /usr/bin/DracOS_VENOMIZER/venomizer.py")  # //usr/bin/
    elif menu == "00":
        exit()
    else:
        print(R('Wrong Input!'))

def back():
    PassAtck()
#Funciton
#BruteSpray
def BruteSpray():
    if os.path.isfile("/usr/bin/brutespray"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL BruteSpray ☣" -geometry 100x30 -e "sudo apt install brutespray"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/brutespray"):
            print(B("brutespray Already Installed"))
        else:
            print(R("BruteSpray Not Installed"))
        input()
        back()
        # end BruteSpray

#Brup Suite
def BrupSuite():
    if os.path.isfile("/usr/bin/brup"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Brup Suite ☣" -geometry 100x30 -e "sudo apt install burpsuite"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/brup"):
            print(B("Brup Suite Already Installed"))
        else:
            print(R("Brup Suite Not Installed"))
        input()
        back()
    # end BrupSuite

#CeWL
def CeWL():
    if os.path.isfile("/usr/bin/cewl"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL CeWL ☣" -geometry 100x30 -e "sudo apt install cewl"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/cewl"):
            print(B("CeWL Already Installed"))
        else:
            print(R("CeWL Not Installed"))
        input()
        back()
    # end CeWL

#chntpw
def chntpw():
    if os.path.isfile("/usr/bin/chntpw"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL chntpw ☣" -geometry 100x30 -e "sudo apt install chntpw"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/chntpw"):
            print(B("chntpw Already Installed"))
        else:
            print(R("chntpw Not Installed"))
        input()
        back()
    # end chntpw

#cisco-auditing-tool
def cisco_auditing_tool():
    if os.path.isfile("/usr/bin/cisco-auditing-tool"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL cisco-auditing-tool ☣" -geometry 100x30 -e "sudo apt install cisco-auditing-tool"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/cisco-auditing-tool"):
            print(B("cisco-auditing-tool Already Installed"))
        else:
            print(R("cisco-auditing-tool Not Installed"))
        input()
        back()
    # end cisco-auditing-tool

#CmosPwd
def CmosPwd():
    if os.path.isfile("/usr/bin/cmos-pwd"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL CmosPwd ☣" -geometry 100x30 -e "sudo apt install cmos-pwd"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/cmos-pwd"):
            print(B("CmosPwd Already Installed"))
        else:
            print(R("CmosPwd Not Installed"))
        input()
        back()
    # end CmosPwd

#Creddump
def Creddump():
    if os.path.isfile("/usr/bin/creddump"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Creddump ☣" -geometry 100x30 -e "sudo apt install creddump"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/creddump"):
            print(B("Creddump Already Installed"))
        else:
            print(R("Creddump Not Installed"))
        input()
        back()
    # end Creddump

#Crowbar
def Crowbar():
    if os.path.isfile("/usr/bin/crowbar"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Crowbar ☣" -geometry 100x30 -e "sudo apt install crowbar"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/crowbar"):
            print(B("Crowbar Already Installed"))
        else:
            print(R("Crowbar Not Installed"))
        input()
        back()
    # end Crowbar

#Crunch
def Crunch():
    if os.path.isfile("/usr/bin/crunch"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Crunch ☣" -geometry 100x30 -e "sudo apt install crunch"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/crunch"):
            print(B("Crunch Already Installed"))
        else:
            print(R("Crunch Not Installed"))
        input()
        back()
    # end Crunch

#Findmyhash
def Findmyhash():
    if os.path.isfile("/usr/bin/findmyhash"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Findmyhash ☣" -geometry 100x30 -e "sudo apt install findmyhash"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/findmyhash"):
            print(B("Findmyhash Already Installed"))
        else:
            print(R("Findmyhash Not Installed"))
        input()
        back()
    # end Findmyhash

#Gpp-decrypt
def Gpp_decrypt():
    if os.path.isfile("/usr/bin/gpp-decrypt"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Gpp-decrypt ☣" -geometry 100x30 -e "sudo apt install gpp-decrypt"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/gpp-decrypt"):
            print(B("Gpp-decrypt Already Installed"))
        else:
            print(R("Gpp-decrypt Not Installed"))
        input()
        back()
    # end Gpp-decrypt

#Hash-identifier
def Hash_identifier():
    if os.path.isfile("/usr/bin/hash-identifier"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Hash-identifier ☣" -geometry 100x30 -e "sudo apt install hash-identifier"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/hash-identifier"):
            print(B("Hash-identifier Already Installed"))
        else:
            print(R("Hash-identifier Not Installed"))
        input()
        back()
    # end Hash-identifier

#Hashcat
def Hashcat():
    if os.path.isfile("/usr/bin/hashcat"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Hashcat ☣" -geometry 100x30 -e "sudo apt install hashcat"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/hashcat"):
            print(B("Hashcat Already Installed"))
        else:
            print(R("Hashcat Not Installed"))
        input()
        back()
    # end Hashcat

#HexorBase
def HexorBase():
    if os.path.isfile("/usr/bin/hexorbase"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL HexorBase ☣" -geometry 100x30 -e "sudo apt install hexorbase"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/hexorbase"):
            print(B("HexorBase Already Installed"))
        else:
            print(R("HexorBase Not Installed"))
        input()
        back()
    # end HexorBase

#THC-Hydra
def THC_Hydra():
    if os.path.isfile("/usr/bin/hydra"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL THC-Hydra ☣" -geometry 100x30 -e "sudo apt install hydra"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/hydra"):
            print(B("THC-Hydra Already Installed"))
        else:
            print(R("THC-Hydra Not Installed"))
        input()
        back()
    # end THC-Hydra

#John the Ripper
def John_the_Ripper():
    if os.path.isfile("/usr/bin/john"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL John the Ripper ☣" -geometry 100x30 -e "sudo apt install john"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/john"):
            print(B("John the Ripper Already Installed"))
        else:
            print(R("John the Ripper Not Installed"))
        input()
        back()
    # end John the Ripper

#Johnny
def Johnny():
    if os.path.isfile("/usr/bin/johnny"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Johnny ☣" -geometry 100x30 -e "sudo apt install johnny"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/johnny"):
            print(B("Johnny Already Installed"))
        else:
            print(R("Johnny Not Installed"))
        input()
        back()
    # end Johnny

#keimpx
def keimpx():
    if os.path.isfile("/usr/bin/keimpx"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL keimpx ☣" -geometry 100x30 -e "sudo apt install keimpx"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/keimpx"):
            print(B("keimpx Already Installed"))
        else:
            print(R("keimpx Not Installed"))
        input()
        back()
    # end keimpx

#Maltego Teeth
def Maltego_Teeth():
    if os.path.isfile("/usr/bin/maltego"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Maltego Teeth ☣" -geometry 100x30 -e "sudo apt install maltego"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/maltego"):
            print(B("Maltego Teeth Already Installed"))
        else:
            print(R("Maltego Teeth Not Installed"))
        input()
        back()
    # end Maltego Teeth

#Maskprocessor
def Maskprocessor():
    if os.path.isfile("/usr/bin/maskprocessor"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Maskprocessor ☣" -geometry 100x30 -e "sudo apt install maskprocessor"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/maskprocessor"):
            print(B("Maskprocessor Already Installed"))
        else:
            print(R("Maskprocessor Not Installed"))
        input()
        back()
    # end Maskprocessor

#Multiforcer
def Multiforcer():
    if os.path.isfile("/usr/bin/multiforcer"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Multiforcer ☣" -geometry 100x30 -e "sudo apt install multiforcer"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/multiforcer"):
            print(B("Multiforcer Already Installed"))
        else:
            print(R("Multiforcer Not Installed"))
        input()
        back()
    # end Multiforcer

#Ncrack
def Ncrack():
    if os.path.isfile("/usr/bin/ncrack"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Ncrack ☣" -geometry 100x30 -e "sudo apt install ncrack"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/ncrack"):
            print(B("Ncrack Already Installed"))
        else:
            print(R("Ncrack Not Installed"))
        input()
        back()
    # end Ncrack

#Oclgausscrack
def Oclgausscrack():
    if os.path.isfile("/usr/bin/oclgausscrack"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Oclgausscrack ☣" -geometry 100x30 -e "sudo apt install oclgausscrack"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/oclgausscrack"):
            print(B("Oclgausscrack Already Installed"))
        else:
            print(R("Oclgausscrack Not Installed"))
        input()
        back()
    # end Oclgausscrack

#Ophcrack
def Ophcrack():
    if os.path.isfile("/usr/bin/ophcrack"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Ophcrack ☣" -geometry 100x30 -e "sudo apt install ophcrack"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/ophcrack"):
            print(B("Ophcrack Already Installed"))
        else:
            print(R("Ophcrack Not Installed"))
        input()
        back()
    # end Ophcrack

#PACK
def PACK():
    if os.path.isfile("/usr/bin/pack"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL PACK ☣" -geometry 100x30 -e "sudo apt install pack"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/pack"):
            print(B("PACK Already Installed"))
        else:
            print(R("PACK Not Installed"))
        input()
        back()
    # end PACK

#patator
def Patator():
    if os.path.isfile("/usr/bin/patator"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Patator ☣" -geometry 100x30 -e "sudo apt install patator"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/patator"):
            print(B("Patator Already Installed"))
        else:
            print(R("Patator Not Installed"))
        input()
        back()
    # end Patator

#Phrasendrescher
def Phrasendrescher():
    if os.path.isfile("/usr/bin/phrasendrescher"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Phrasendrescher ☣" -geometry 100x30 -e "sudo apt install phrasendrescher"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/phrasendrescher"):
            print(B("Phrasendrescher Already Installed"))
        else:
            print(R("Phrasendrescher Not Installed"))
        input()
        back()
    # end Phrasendrescher

#Polenum
def Polenum():
    if os.path.isfile("/usr/bin/polenum"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Polenum ☣" -geometry 100x30 -e "sudo apt install polenum"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/polenum"):
            print(B("Polenum Already Installed"))
        else:
            print(R("Polenum Not Installed"))
        input()
        back()
    # end Polenum

#RainbowCrack
def RainbowCrack():
    if os.path.isfile("/usr/bin/rainbowcrack"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL RainbowCrack ☣" -geometry 100x30 -e "sudo apt install rainbowcrack"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/rainbowcrack"):
            print(B("RainbowCrack Already Installed"))
        else:
            print(R("RainbowCrack Not Installed"))
        input()
        back()
    # end RainbowCrack

#Rcracki-mt
def Rcracki_mt():
    if os.path.isfile("/usr/bin/rcracki-mt"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Rcracki-mt ☣" -geometry 100x30 -e "sudo apt install rcracki-mt"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/rcracki-mt"):
            print(B("Rcracki-mt Already Installed"))
        else:
            print(R("Rcracki-mt Not Installed"))
        input()
        back()
    # end Rcracki-mt

#RSMangler
def RSMangler():
    if os.path.isfile("/usr/bin/rsmangler"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL RSMangler ☣" -geometry 100x30 -e "sudo apt install rsmangler"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/rsmangler"):
            print(B("RSMangler Already Installed"))
        else:
            print(R("RSMangler Not Installed"))
        input()
        back()
    # end RSMangler

#SecLists
def SecLists():
    if os.path.isfile("/usr/bin/secLists"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL SecLists ☣" -geometry 100x30 -e "sudo apt install secLists"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/secLists"):
            print(B("SecLists Already Installed"))
        else:
            print(R("SecLists Not Installed"))
        input()
        back()
    # end SecLists

#SQLdict
def SQLdict():
    if os.path.isfile("/usr/bin/sqldict"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL SQLdict ☣" -geometry 100x30 -e "sudo apt install sqldict"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/sqldict"):
            print(B("SQLdict Already Installed"))
        else:
            print(R("SQLdict Not Installed"))
        input()
        back()
    # end SQLdict

#Statsprocessor
def Statsprocessor():
    if os.path.isfile("/usr/bin/statsprocessor"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Statsprocessor ☣" -geometry 100x30 -e "sudo apt install statsprocessor"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/statsprocessor"):
            print(B("Statsprocessor Already Installed"))
        else:
            print(R("Statsprocessor Not Installed"))
        input()
        back()
    # end Statsprocessor

#THC-pptp-bruter
def THC_pptp_bruter():
    if os.path.isfile("/usr/bin/thc-pptp-bruter"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL THC-pptp-bruter ☣" -geometry 100x30 -e "sudo apt install thc-pptp-bruter"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/thc-pptp-bruter"):
            print(B("THC-pptp-bruter Already Installed"))
        else:
            print(R("THC-pptp-bruter Not Installed"))
        input()
        back()
    # end THC-pptp-bruter

#TrueCrack
def TrueCrack():
    if os.path.isfile("/usr/bin/truecrack"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL TrueCrack ☣" -geometry 100x30 -e "sudo apt install truecrack"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/truecrack"):
            print(B("TrueCrack Already Installed"))
        else:
            print(R("TrueCrack Not Installed"))
        input()
        back()
    # end TrueCrack
    
#WebScarab
def WebScarab():
    if os.path.isfile("/usr/bin/webscarab"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL WebScarab ☣" -geometry 100x30 -e "sudo apt install webscarab"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/webscarab"):
            print(B("WebScarab Already Installed"))
        else:
            print(R("WebScarab Not Installed"))
        input()
        back()
    # end WebScarab

#Wordlists
def Wordlists():
    if os.path.isfile("/usr/bin/wordlists"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Wordlists ☣" -geometry 100x30 -e "sudo apt install wordlists"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/wordlists"):
            print(B("Wordlists Already Installed"))
        else:
            print(R("Wordlists Not Installed"))
        input()
        back()
    # end Wordlists

#zaproxy
def zaproxy():
    if os.path.isfile("/usr/bin/zaproxy"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL zaproxy ☣" -geometry 100x30 -e "sudo apt install zaproxy"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/zaproxy"):
            print(B("zaproxy Already Installed"))
        else:
            print(R("zaproxy Not Installed"))
        input()
        back()
    # end zaproxy        




# while True:
#     PassAtck()