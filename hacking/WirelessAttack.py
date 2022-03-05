#!/usr/bin/python3
#! -*- coding: utf-8 -*-
import os
from color import*
import Logo

def WireAttack():
    Logo.logo_17()
    print(G(""" 
    1.  Airbase-ng
    2.  Aircrack-ng
    3.  Airdecap-ng and Airdeclock-ng
    4.  Aireplay-ng
    5.  airgraph-ng
    6.  Airmon-ng
    7.  Airodump-ng
    8.  airodump-ng-oui-update
    9.  Airolib-ng
    10. Airserv-ng
    11. Airtun-ng
    12. Asleap
    13. Besside-ng
    14. Bluelog
    15. BlueMaho
    16. Bluepot
    17. BlueRanger
    18. Bluesnarfer
    19. Bully
    20. coWPAtty
    21. crackle
    22. eapmd5pass
    23. Easside-ng
    24. Fern Wifi Cracker
    25. FreeRADIUS-WPE
    26. Ghost Phiser
    27. GISKismet
    28. Gqrx
    29. gr-scan
    30. hostapd-wpe
    31. ivstools
    32. kalibrate-rtl
    33. KillerBee
    34. Kismet
    35. makeivs-ng
    36. mdk3
    37. mfcuk
    38. mfoc
    39. mfterm
    40. Multimon-NG
    41. Packetforge-ng
    42. PixieWPS
    43. Pyrit
    44. Reaver    
    45. redfang
    46. RTLSDR Scanner
    47. spooftooph
    48. Tkiptun-ng
    49. Wesside-ng
    50. Wifi Honey
    51. wifiphiser
    52. wifitap
    53. wifite
    54. wpaclean
    55. Airgeddon (New Update)
    0.  back
     """))
    print(R('00. exit'))
    lists = ()
    menu = input(G('[')+R("DracOS")+G("]select> "))
    if menu:
        menu -= 1
        # Call Function
        wireless_tool(lists[name])
    elif menu == 0:
        os.system('python3 /usr/bin/DracOS_VENOMIZER/venomizer.py')
    elif menu == 00:
        exit()
    else:
        print(R('Wrong Input!'))
        input()
        back()


#Function
#wireless tool
def wireless_tool(a):
    if os.path.isfile(f"/usr/bin/{a}") or os.path.isfile(f'/usr/sbin/{a}'):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            f'xterm -T "☣ INSTALL {a} ☣" -geometry 100x30 -e "sudo apt install {a}"'
        )
        os.system("clear")
        if os.path.isfile(f"/usr/bin/{a}") or os.path.isfile(f'/usr/sbin/{a}'):
            print(B(f"{a} Already Installed"))
        else:
            print(R(f"{a} Not Installed"))
        input()
        back()
    # end wireless tool

def back():
    WireAttack()


