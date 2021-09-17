#! usr/share/bin/python3
#! -*- coding: utf-8 -*-
import os
from color import*
import Logo

def WireAttack():
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
    45. Reaver
    46. redfang
    47. RTLSDR Scanner
    48. spooftooph
    49. Tkiptun-ng
    50. Wesside-ng
    51. Wifi Honey
    52. wifiphiser
    53. wifitap
    54. wifite
    55. wpaclean
    0.  back
     """))
    print(R('00. exit'))

    menu = input(G('[')+R("DracOS")+G("]select> "))
    if menu == '1':
        print()
    elif menu == '0':
        os.system('python3 $HOME/git/DracOS_VENOMIZER/venomizer.py')
    elif menu == '00':
        exit()
