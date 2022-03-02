#!/usr/bin/python3

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

    lists = ('binwalk','bulk_extractor','capstone','chntpw','cuckoo','dc3dd','ddrescue','dff','distorm3',
    'dumpzilla','extundelete','foremost','galleta','guymager','iphonebackupanalyzer','p0f','pdf-parser',
    'pdfid','pdgmail','peepdf','regripper','volatility','xplico')

    menu = int(input(G("[") + R("DracOS") + G("]select>")))
    if menu:
        menu -= 1
        # Call function
        tool_forensic(lists[menu])
    
    elif menu == 0:
        os.system("python3 /usr/bin/DracOS_VENOMIZER/venomizer.py")  # //usr/bin/
    elif menu == 00:
        exit()
    else:
        print(R('Wrong Input!'))
        input()
        back()




def back():
    Forensics()

#Function
#tool forensic
def tool_forensic(a):
    if os.path.isfile(f"/usr/bin/{a}"):
        os.system("clear")
        print(B("Tools Available"))
        # input()
        # back()
    else:
        os.system(
            f'sudo apt install {a}'
        )
        os.system("clear")
        if os.path.isfile(f"/usr/bin/{a}"):
            print(B(f"{a} Already Installed"))
        else:
            print(R(f"Not Installing {a}"))
    input()
    back()
    # end tool forensic