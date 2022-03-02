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
    lists = ('brutespray', 'brup', 'cewl', 'chntpw', 'cisco-auditing-tool', 'cmospwd', 'creddump',
     'crowbar', 'crunch', 'findmyhash', 'gpp-decrypt', 'hash-identifier', 'hashcat', 'hexorbase', 
     'thc-hydra', 'john the ripper', 'johnny', 'keimpx', 'maltego teeth', 'maskprocessor', 'multiforcer', 
     'ncrack', 'oclgausscrack', 'ophcrack', 'pack', 'patator', 'phrasendrescher', 'polenum', 'rainbowcrack', 
     'rcracki-mt', 'rsmangler', 'seclists', 'sqldict', 'statsprocessor', 'thc-pptp-bruter', 'truecrack', 
     'webscarab', 'wordlists', 'zaproxy')
    menu = int(input(G("[") + R("DracOS") + G("]select>")))
    if menu:
        menu -= 1
        # Call function
        passwordATK_tool(lists[menu])
    elif menu == 0:
        os.system("python3 /usr/bin/DracOS_VENOMIZER/venomizer.py")  # //usr/bin/
    elif menu == 00:
        exit()
    else:
        print(R('Wrong Input!'))
        input()
        back()

def back():
    PassAtck()
#Funciton
# passwordATK_tool
def passwordATK_tool(a):
    if os.path.isfile(f"/usr/bin/{a}"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            f'xterm -T "☣ INSTALL {a} ☣" -geometry 100x30 -e "sudo apt install {a}"'
        )
        os.system("clear")
        if os.path.isfile(f"/usr/bin/{a}"):
            print(B(f"{a} Already Installed"))
        else:
            print(R(f"{a} Not Installed"))
        input()
        back()
        # end passwordATK_tool

