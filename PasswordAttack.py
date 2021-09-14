#! usr/share/bin/python3
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
        os.system("python3 $HOME/git/DracOS_VENOMIZER/venomizer.py")  # /usr/bin/
    elif menu == "00":
        exit()


#Funciton
#BruteSpray
def BruteSpray():
    if os.path.isfile("usr/bin/brutespray"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL BruteSpray ☣" -geometry 100x30 -e "sudo apt install brutespray"'
        )
        os.system("clear")
        print(B("BruteSpray Already Installed"))
        input()
    # end BruteSpray

#Brup Suite
def BrupSuite():
    if os.path.isfile("usr/bin/brup"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Brup Suite ☣" -geometry 100x30 -e "sudo apt install burpsuite"'
        )
        os.system("clear")
        print(B("Brup Suite Already Installed"))
        input()
    # end BrupSuite

#CeWL
def CeWL():
    if os.path.isfile("usr/bin/cewl"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL CeWL ☣" -geometry 100x30 -e "sudo apt install cewl"'
        )
        os.system("clear")
        print(B("CeWL Already Installed"))
        input()
    # end CeWL

#chntpw
def chntpw():
    if os.path.isfile("usr/bin/chntpw"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL chntpw ☣" -geometry 100x30 -e "sudo apt install chntpw"'
        )
        os.system("clear")
        print(B("chntpw Already Installed"))
        input()
    # end chntpw

#cisco-auditing-tool
def cisco_auditing_tool():
    if os.path.isfile("usr/bin/cisco-auditing-tool"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL cisco-auditing-tool ☣" -geometry 100x30 -e "sudo apt install cisco-auditing-tool"'
        )
        os.system("clear")
        print(B("cisco-auditing-tool Already Installed"))
        input()
    # end cisco-auditing-tool

#CmosPwd
def CmosPwd():
    if os.path.isfile("usr/bin/cmos-pwd"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL CmosPwd ☣" -geometry 100x30 -e "sudo apt install cmos-pwd"'
        )
        os.system("clear")
        print(B("CmosPwd Already Installed"))
        input()
    # end CmosPwd

#Creddump
def Creddump():
    if os.path.isfile("usr/bin/creddump"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Creddump ☣" -geometry 100x30 -e "sudo apt install creddump"'
        )
        os.system("clear")
        print(B("Creddump Already Installed"))
        input()
    # end Creddump

#Crowbar
def Crowbar():
    if os.path.isfile("usr/bin/crowbar"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Crowbar ☣" -geometry 100x30 -e "sudo apt install crowbar"'
        )
        os.system("clear")
        print(B("Crowbar Already Installed"))
        input()
    # end Crowbar

#Crunch
def Crunch():
    if os.path.isfile("usr/bin/crunch"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Crunch ☣" -geometry 100x30 -e "sudo apt install crunch"'
        )
        os.system("clear")
        print(B("Crunch Already Installed"))
        input()
    # end Crunch

#Findmyhash
def Findmyhash():
    if os.path.isfile("usr/bin/findmyhash"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Findmyhash ☣" -geometry 100x30 -e "sudo apt install findmyhash"'
        )
        os.system("clear")
        print(B("Findmyhash Already Installed"))
        input()
    # end Findmyhash

#Gpp-decrypt
def Gpp_decrypt():
    if os.path.isfile("usr/bin/gpp-decrypt"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Gpp-decrypt ☣" -geometry 100x30 -e "sudo apt install gpp-decrypt"'
        )
        os.system("clear")
        print(B("Gpp-decrypt Already Installed"))
        input()
    # end Gpp-decrypt

#Hash-identifier
def Hash_identifier():
    if os.path.isfile("usr/bin/hash-identifier"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Hash-identifier ☣" -geometry 100x30 -e "sudo apt install hash-identifier"'
        )
        os.system("clear")
        print(B("Hash-identifier Already Installed"))
        input()
    # end Hash-identifier

#Hashcat
def Hashcat():
    if os.path.isfile("usr/bin/hashcat"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Hashcat ☣" -geometry 100x30 -e "sudo apt install hashcat"'
        )
        os.system("clear")
        print(B("Hashcat Already Installed"))
        input()
    # end Hashcat

#HexorBase
def HexorBase():
    if os.path.isfile("usr/bin/hexorbase"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL HexorBase ☣" -geometry 100x30 -e "sudo apt install hexorbase"'
        )
        os.system("clear")
        print(B("HexorBase Already Installed"))
        input()
    # end HexorBase

#THC-Hydra
def THC_Hydra():
    if os.path.isfile("usr/bin/hydra"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL THC-Hydra ☣" -geometry 100x30 -e "sudo apt install hydra"'
        )
        os.system("clear")
        print(B("THC-Hydra Already Installed"))
        input()
    # end THC-Hydra

#John the Ripper
def John_the_Ripper():
    if os.path.isfile("usr/bin/john"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL John the Ripper ☣" -geometry 100x30 -e "sudo apt install john"'
        )
        os.system("clear")
        print(B("John the Ripper Already Installed"))
        input()
    # end John the Ripper

#Johnny
def Johnny():
    if os.path.isfile("usr/bin/johnny"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Johnny ☣" -geometry 100x30 -e "sudo apt install johnny"'
        )
        os.system("clear")
        print(B("Johnny Already Installed"))
        input()
    # end Johnny

#keimpx
def keimpx():
    if os.path.isfile("usr/bin/keimpx"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL keimpx ☣" -geometry 100x30 -e "sudo apt install keimpx"'
        )
        os.system("clear")
        print(B("keimpx Already Installed"))
        input()
    # end keimpx

#Maltego Teeth
def Maltego_Teeth():
    if os.path.isfile("usr/bin/maltego"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Maltego Teeth ☣" -geometry 100x30 -e "sudo apt install maltego"'
        )
        os.system("clear")
        print(B("Maltego Teeth Already Installed"))
        input()
    # end Maltego Teeth

#Maskprocessor
def Maskprocessor():
    if os.path.isfile("usr/bin/maskprocessor"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Maskprocessor ☣" -geometry 100x30 -e "sudo apt install maskprocessor"'
        )
        os.system("clear")
        print(B("Maskprocessor Already Installed"))
        input()
    # end Maskprocessor

#Multiforcer
def Multiforcer():
    if os.path.isfile("usr/bin/multiforcer"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Multiforcer ☣" -geometry 100x30 -e "sudo apt install multiforcer"'
        )
        os.system("clear")
        print(B("Multiforcer Already Installed"))
        input()
    # end Multiforcer

#Ncrack
def Ncrack():
    if os.path.isfile("usr/bin/ncrack"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Ncrack ☣" -geometry 100x30 -e "sudo apt install ncrack"'
        )
        os.system("clear")
        print(B("Ncrack Already Installed"))
        input()
    # end Ncrack

#Oclgausscrack
def Oclgausscrack():
    if os.path.isfile("usr/bin/oclgausscrack"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Oclgausscrack ☣" -geometry 100x30 -e "sudo apt install oclgausscrack"'
        )
        os.system("clear")
        print(B("Oclgausscrack Already Installed"))
        input()
    # end Oclgausscrack

#Ophcrack
def Ophcrack():
    if os.path.isfile("usr/bin/ophcrack"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Ophcrack ☣" -geometry 100x30 -e "sudo apt install ophcrack"'
        )
        os.system("clear")
        print(B("Ophcrack Already Installed"))
        input()
    # end Ophcrack

#PACK
def PACK():
    if os.path.isfile("usr/bin/pack"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL PACK ☣" -geometry 100x30 -e "sudo apt install pack"'
        )
        os.system("clear")
        print(B("PACK Already Installed"))
        input()
    # end PACK

#patator
def Patator():
    if os.path.isfile("usr/bin/patator"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Patator ☣" -geometry 100x30 -e "sudo apt install patator"'
        )
        os.system("clear")
        print(B("Patator Already Installed"))
        input()
    # end Patator

#Phrasendrescher
def Phrasendrescher():
    if os.path.isfile("usr/bin/phrasendrescher"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Phrasendrescher ☣" -geometry 100x30 -e "sudo apt install phrasendrescher"'
        )
        os.system("clear")
        print(B("Phrasendrescher Already Installed"))
        input()
    # end Phrasendrescher

#Polenum
def Polenum():
    if os.path.isfile("usr/bin/polenum"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Polenum ☣" -geometry 100x30 -e "sudo apt install polenum"'
        )
        os.system("clear")
        print(B("Polenum Already Installed"))
        input()
    # end Polenum

#RainbowCrack
def RainbowCrack():
    if os.path.isfile("usr/bin/rainbowcrack"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL RainbowCrack ☣" -geometry 100x30 -e "sudo apt install rainbowcrack"'
        )
        os.system("clear")
        print(B("RainbowCrack Already Installed"))
        input()
    # end RainbowCrack

#Rcracki-mt
def Rcracki_mt():
    if os.path.isfile("usr/bin/rcracki-mt"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Rcracki-mt ☣" -geometry 100x30 -e "sudo apt install rcracki-mt"'
        )
        os.system("clear")
        print(B("Rcracki-mt Already Installed"))
        input()
    # end Rcracki-mt

#RSMangler
def RSMangler():
    if os.path.isfile("usr/bin/rsmangler"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL RSMangler ☣" -geometry 100x30 -e "sudo apt install rsmangler"'
        )
        os.system("clear")
        print(B("RSMangler Already Installed"))
        input()
    # end RSMangler

#SecLists
def SecLists():
    if os.path.isfile("usr/bin/secLists"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL SecLists ☣" -geometry 100x30 -e "sudo apt install secLists"'
        )
        os.system("clear")
        print(B("SecLists Already Installed"))
        input()
    # end SecLists

#SQLdict
def SQLdict():
    if os.path.isfile("usr/bin/sqldict"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL SQLdict ☣" -geometry 100x30 -e "sudo apt install sqldict"'
        )
        os.system("clear")
        print(B("SQLdict Already Installed"))
        input()
    # end SQLdict

#Statsprocessor
def Statsprocessor():
    if os.path.isfile("usr/bin/statsprocessor"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Statsprocessor ☣" -geometry 100x30 -e "sudo apt install statsprocessor"'
        )
        os.system("clear")
        print(B("Statsprocessor Already Installed"))
        input()
    # end Statsprocessor

#THC-pptp-bruter
def THC_pptp_bruter():
    if os.path.isfile("usr/bin/thc-pptp-bruter"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL THC-pptp-bruter ☣" -geometry 100x30 -e "sudo apt install thc-pptp-bruter"'
        )
        os.system("clear")
        print(B("THC-pptp-bruter Already Installed"))
        input()
    # end THC-pptp-bruter

#TrueCrack
def TrueCrack():
    if os.path.isfile("usr/bin/truecrack"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL TrueCrack ☣" -geometry 100x30 -e "sudo apt install truecrack"'
        )
        os.system("clear")
        print(B("TrueCrack Already Installed"))
        input()
    # end TrueCrack
    
#WebScarab
def WebScarab():
    if os.path.isfile("usr/bin/webscarab"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL WebScarab ☣" -geometry 100x30 -e "sudo apt install webscarab"'
        )
        os.system("clear")
        print(B("WebScarab Already Installed"))
        input()
    # end WebScarab

#Wordlists
def Wordlists():
    if os.path.isfile("usr/bin/wordlists"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL Wordlists ☣" -geometry 100x30 -e "sudo apt install wordlists"'
        )
        os.system("clear")
        print(B("Wordlists Already Installed"))
        input()
    # end Wordlists

#zaproxy
def zaproxy():
    if os.path.isfile("usr/bin/zaproxy"):
        os.system("clear")
        print(B("Tools Available"))
        input()
    else:
        os.system(
            'xterm -T "☣ INSTALL zaproxy ☣" -geometry 100x30 -e "sudo apt install zaproxy"'
        )
        os.system("clear")
        print(B("zaproxy Already Installed"))
        input()
    # end zaproxy        




while True:
    PassAtck()