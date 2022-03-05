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
    lists = ('airbase-ng','aircrack-ng','aircrack-ng','aircrack-ng','airgraph-ng','aircrack-ng','aireplay-ng','aircrack-ng',
    'airolib-ng','aircrack-ng','aircrack-ng','asleap')
    menu = int(input(G('[')+R("DracOS")+G("]select> ")))
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
#Airbase-ng 1
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
    # end Airbase-ng

#Aircrack-ng 2
def Aircrack_ng():
    if os.path.isfile("/usr/bin/aircrack-ng") or os.path.isfile('/usr/include/aircrack-ng'):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Aircrack-ng ☣" -geometry 100x30 -e "sudo apt install aircrack-ng"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/aircrack-ng") or os.path.isfile('/usr/include/aircrack-ng'):
            print(B("Aircrack-ng Already Installed"))
        else:
            print(R("Aircrack-ng Not Installed"))
        input()
        back()
    # end Aircrack-ng

#Airdecap-ng and Airdeclock-ng 3
def Airdecap_ng():
    if os.path.isfile("/usr/bin/airdecap-ng"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Airdecap-ng ☣" -geometry 100x30 -e "sudo apt install aircrack-ng"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/airdecap-ng"):
            print(B("Airdecap-ng Already Installed"))
        else:
            print(R("Airdecap-ng Not Installed"))
        input()
        back()
    # end Airdecap-ng

#Aireplay-ng 4
def Aireplay_ng():
    if os.path.isfile("/usr/bin/aireplay-ng") or os.path.isfile('/usr/sbin/aireplay-ng'):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Aireplay-ng ☣" -geometry 100x30 -e "sudo apt install aircrack-ng"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/aireplay-ng") or os.path.isfile('/usr/sbin/aireplay-ng'):
            print(B("Aireplay-ng Already Installed"))
        else:
            print(R("Aireplay-ng Not Installed"))
        input()
        back()
    # end Aireplay-ng

#airgraph-ng 5
def airgraph_ng():
    if os.path.isfile("/usr/bin/airgraph-ng"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL airgraph-ng ☣" -geometry 100x30 -e "sudo apt install airgraph-ng"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/airgraph-ng"):
            print(B("airgraph-ng Already Installed"))
        else:
            print(R("airgraph-ng Not Installed"))
        input()
        back()
    # end airgraph-ng

#Airmon-ng 6
def Airmon_ng():
    if os.path.isfile("/usr/sbin/airmon-ng"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Airmon-ng ☣" -geometry 100x30 -e "sudo apt install aircrack-ng"'
        )
        os.system("clear")
        if os.path.isfile("/usr/sbin/airmon-ng"):
            print(B("Airmon-ng Already Installed"))
        else:
            print(R("Airmon-ng Not Installed"))
        input()
        back()
    # end Airmon-ng

#Airodump-ng 7
def Airodump_ng():
    if os.path.isfile("/usr/sbin/airodump-ng"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Airodump-ng ☣" -geometry 100x30 -e "sudo apt install aircrack-ng"'
        )
        os.system("clear")
        if os.path.isfile("/usr/sbin/airodump-ng"):
            print(B("airodump-ng Already Installed"))
        else:
            print(R("airodump-ng Not Installed"))
        input()
        back()
    # end Airodump-ng

#airodump-ng-oui-update
def airodump_ng_oui_update():
    if os.path.isfile("/usr/sbin/airodump-ng-oui-update"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Airodump-ng-oui-update ☣" -geometry 100x30 -e "sudo apt install aircrack-ng'
        )
        os.system("clear")
        if os.path.isfile("/usr/sbin/airodump-ng-oui-update"):
            print(B("airodump-ng-oui-update Already Installed"))
        else:
            print(R("airodump-ng-oui-update Not Installed"))
        input()
        back()
    # end airodump-ng-oui-update

#Airolib-ng
def Airolib_ng():
    if os.path.isfile("/usr/bin/airolib-ng"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Airolib-ng ☣" -geometry 100x30 -e "sudo apt install airolib-ng"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/airolib-ng"):
            print(B("Airolib-ng Already Installed"))
        else:
            print(R("Airolib-ng Not Installed"))
        input()
        back()
    # end Airolib-ng

#Airserv-ng
def Airserv_ng():
    if os.path.isfile("/usr/sbin/airserv-ng"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Airserv-ng ☣" -geometry 100x30 -e "sudo apt install aircrack-ng"'
        )
        os.system("clear")
        if os.path.isfile("/usr/sbin/airserv-ng"):
            print(B("Airserv-ng Already Installed"))
        else:
            print(R("Airserv-ng Not Installed"))
        input()
        back()
    # end Airserv-ng

#Airtun-ng
def Airtun_ng():
    if os.path.isfile("/usr/sbin/airtun-ng"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Airtun-ng ☣" -geometry 100x30 -e "sudo apt install aircrack-ng"'
        )
        os.system("clear")
        if os.path.isfile("/usr/sbin/airtun-ng"):
            print(B("Airtun-ng Already Installed"))
        else:
            print(R("Airtun-ng Not Installed"))
        input()
        back()
    # end Airtun-ng

#Asleap
def Asleap():
    if os.path.isfile("/usr/bin/asleap"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Asleap ☣" -geometry 100x30 -e "sudo apt install asleap"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/asleap"):
            print(B("Asleap Already Installed"))
        else:
            print(R("Asleap Not Installed"))
        input()
        back()
    # end Asleap

#Besside-ng
def Besside_ng():
    if os.path.isfile("/usr/sbin/besside-ng"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Besside-ng ☣" -geometry 100x30 -e "sudo apt install aircrack-ng"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/besside-ng"):
            print(B("Besside-ng Already Installed"))
        else:
            print(R("Besside-ng Not Installed"))
        input()
        back()
    # end Besside-ng

#Bluelog
def Bluelog():
    if os.path.isfile("/usr/bin/bluelog"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Bluelog ☣" -geometry 100x30 -e "sudo apt install bluelog"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/bluelog"):
            print(B("Bluelog Already Installed"))
        else:
            print(R("Bluelog Not Installed"))
        input()
        back()
    # end Bluelog

#BlueMaho
def BlueMaho():
    if os.path.isfile("/usr/bin/blue-maho"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL BlueMaho ☣" -geometry 100x30 -e "sudo apt install blue-maho"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/blue-maho"):
            print(B("BlueMaho Already Installed"))
        else:
            print(R("BlueMaho Not Installed"))
        input()
        back()
    # end BlueMaho

#Bluepot
def Bluepot():
    if os.path.isfile("/usr/bin/bluepot"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Bluepot ☣" -geometry 100x30 -e "sudo apt install bluepot"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/bluepot"):
            print(B("Bluepot Already Installed"))
        else:
            print(R("Bluepot Not Installed"))
        input()
        back()
    # end Bluepot

#BlueRanger
def BlueRanger():
    if os.path.isfile("/usr/bin/blue-ranger"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL BlueRanger ☣" -geometry 100x30 -e "sudo apt install blue-ranger"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/blue-ranger"):
            print(B("BlueRanger Already Installed"))
        else:
            print(R("BlueRanger Not Installed"))
        input()
        back()
    # end BlueRanger

#Bluesnarfer
def Bluesnarfer():
    if os.path.isfile("/usr/bin/bluesnarfer"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Bluesnarfer ☣" -geometry 100x30 -e "sudo apt install bluesnarfer"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/bluesnarfer"):
            print(B("Bluesnarfer Already Installed"))
        else:
            print(R("Bluesnarfer Not Installed"))
        input()
        back()
    # end Bluesnarfer

#Bully
def Bully():
    if os.path.isfile("/usr/bin/bully"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Bully ☣" -geometry 100x30 -e "sudo apt install bully"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/bully"):
            print(B("Bully Already Installed"))
        else:
            print(R("Bully Not Installed"))
        input()
        back()
    # end Bully

#coWPAtty
def coWPAtty():
    if os.path.isfile("/usr/bin/coWPAtty"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL coWPAtty ☣" -geometry 100x30 -e "sudo apt install coWPAtty"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/coWPAtty"):
            print(B("coWPAtty Already Installed"))
        else:
            print(R("coWPAtty Not Installed"))
        input()
        back()
    # end coWPAtty

#crackle
def crackle():
    if os.path.isfile("/usr/bin/crackle"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL crackle ☣" -geometry 100x30 -e "sudo apt install crackle"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/crackle"):
            print(B("crackle Already Installed"))
        else:
            print(R("crackle Not Installed"))
        input()
        back()
    # end crackle

#eapmd5pass
def eapmd5pass():
    if os.path.isfile("/usr/bin/eapmd5pass"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL eapmd5pass ☣" -geometry 100x30 -e "sudo apt install eapmd5pass"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/eapmd5pass"):
            print(B("eapmd5pass Already Installed"))
        else:
            print(R("eapmd5pass Not Installed"))
        input()
        back()
    # end eapmd5pass

#Easside-ng
def Easside_ng():
    if os.path.isfile("/usr/bin/easside-ng"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Easside-ng ☣" -geometry 100x30 -e "sudo apt install easside-ng"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/easside-ng"):
            print(B("Easside-ng Already Installed"))
        else:
            print(R("Easside-ng Not Installed"))
        input()
        back()
    # end Easside_ng

#Fern Wifi Cracker
def Fern_Wifi_Cracker():
    if os.path.isfile("/usr/bin/fern-wifi-cracker"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Fern Wifi Cracker ☣" -geometry 100x30 -e "sudo apt install fern-wifi-cracker"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/fern-wifi-cracker"):
            print(B("Fern Wifi Cracker Already Installed"))
        else:
            print(R("Fern Wifi Cracker Not Installed"))
        input()
        back()
    # end Fern_Wifi_Cracker

#FreeRADIUS-WPE
def FreeRADIUS_WPE():
    if os.path.isfile("/usr/bin/freeradius-wpe") or os.path.isfile('/usr/sbin/freeradius-wpe') or os.path.isfile('/usr/lib/freeradius-wpe') or os.path.isfile('/etc/freeradius-wpe'):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL FreeRADIUS-WPE ☣" -geometry 100x30 -e "sudo apt install freeradius-wpe"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/freeradius-wpe"):
            print(B("FreeRADIUS-WPE Already Installed"))
        else:
            print(R("FreeRADIUS-WPE Not Installed"))
        input()
        back()
    # end FreeRADIUS_WPE

#Ghost Phiser
def Ghost_Phiser():
    if os.path.isfile("/usr/bin/ghost-phiser"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Ghost Phiser ☣" -geometry 100x30 -e "sudo apt install ghost-phiser"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/ghost-phiser"):
            print(B("Ghost Phiser Already Installed"))
        else:
            print(R("Ghost Phiser Not Installed"))
        input()
        back()
    # end Ghost_Phiser

#GISKismet
def GISKismet():
    if os.path.isfile("/usr/bin/giskismet"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL GISKismet ☣" -geometry 100x30 -e "sudo apt install giskismet"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/giskismet"):
            print(B("GISKismet Already Installed"))
        else:
            print(R("GISKismet Not Installed"))
        input()
        back()
    # end GISKismet

#Gqrx
def Gqrx():
    if os.path.isfile("/usr/bin/gqrx"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Gqrx ☣" -geometry 100x30 -e "sudo apt install gqrx"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/gqrx"):
            print(B("Gqrx Already Installed"))
        else:
            print(R("Gqrx Not Installed"))
        input()
        back()
    # end Gqrx

#gr-scan
def gr_scan():
    if os.path.isfile("/usr/bin/gr-scan"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL gr-scan ☣" -geometry 100x30 -e "sudo apt install gr-scan"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/gr-scan"):
            print(B("gr-scan Already Installed"))
        else:
            print(R("gr-scan Not Installed"))
        input()
        back()
    # end gr_scan

#hostapd-wpe
def hostapd_wpe():
    if os.path.isfile("/usr/bin/hostapd-wpe"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL hostapd-wpe ☣" -geometry 100x30 -e "sudo apt install hostapd-wpe"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/hostapd-wpe"):
            print(B("hostapd-wpe Already Installed"))
        else:
            print(R("hostapd-wpe Not Installed"))
        input()
        back()
    # end hostapd_wpe

#ivstools
def ivstools():
    if os.path.isfile("/usr/bin/ivstools"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL ivstools ☣" -geometry 100x30 -e "sudo apt install ivstools"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/ivstools"):
            print(B("ivstools Already Installed"))
        else:
            print(R("ivstools Not Installed"))
        input()
        back()
    # end ivstools

#kalibrate-rtl
def kalibrate_rtl():
    if os.path.isfile("/usr/bin/kalibrate-rtl"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL kalibrate-rtl ☣" -geometry 100x30 -e "sudo apt install kalibrate-rtl"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/kalibrate-rtl"):
            print(B("kalibrate-rtl Already Installed"))
        else:
            print(R("kalibrate-rtl Not Installed"))
        input()
        back()
    # end kalibrate_rtl

#KillerBee
def KillerBee():
    if os.path.isfile("/usr/bin/killerbee"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL KillerBee ☣" -geometry 100x30 -e "sudo apt install killerbee"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/killerbee"):
            print(B("KillerBee Already Installed"))
        else:
            print(R("KillerBee Not Installed"))
        input()
        back()
    # end KillerBee

#Kismet
def Kismet():
    if os.path.isfile("/usr/bin/kismet"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Kismet ☣" -geometry 100x30 -e "sudo apt install kismet"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/kismet"):
            print(B("Kismet Already Installed"))
        else:
            print(R("Kismet Not Installed"))
        input()
        back()
    # end Kismet

#makeivs-ng
def makeivs_ng():
    if os.path.isfile("/usr/bin/makeivs-ng"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL makeivs-ng ☣" -geometry 100x30 -e "sudo apt install makeivs-ng"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/makeivs-ng"):
            print(B("makeivs-ng Already Installed"))
        else:
            print(R("makeivs-ng Not Installed"))
        input()
        back()
    # end makeivs_ng
#mdk3
def mdk3():
    if os.path.isfile("/usr/bin/mdk3"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL mdk3 ☣" -geometry 100x30 -e "sudo apt install mdk3"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/mdk3"):
            print(B("mdk3 Already Installed"))
        else:
            print(R("mdk3 Not Installed"))
        input()
        back()
    # end mdk3

#mfcuk
def mfcuk():
    if os.path.isfile("/usr/bin/mfcuk"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL mfcuk ☣" -geometry 100x30 -e "sudo apt install mfcuk"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/mfcuk"):
            print(B("mfcuk Already Installed"))
        else:
            print(R("mfcuk Not Installed"))
        input()
        back()
    # end mfcuk

#mfoc
def mfoc():
    if os.path.isfile("/usr/bin/mfoc"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL mfoc ☣" -geometry 100x30 -e "sudo apt install mfoc"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/mfoc"):
            print(B("mfoc Already Installed"))
        else:
            print(R("mfoc Not Installed"))
        input()
        back()
    # end mfoc

#mfterm
def mfterm():
    if os.path.isfile("/usr/bin/mfterm"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL mfterm ☣" -geometry 100x30 -e "sudo apt install mfterm"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/mfterm"):
            print(B("mfterm Already Installed"))
        else:
            print(R("mfterm Not Installed"))
        input()
        back()
    # end mfterm

#Multimon-NG
def multimon_ng():
    if os.path.isfile("/usr/bin/multimon-ng"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL multimon-ng ☣" -geometry 100x30 -e "sudo apt install multimon-ng"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/multimon-ng"):
            print(B("multimon-ng Already Installed"))
        else:
            print(R("multimon-ng Not Installed"))
        input()
        back()
    # end multimon_ng

#Packetforge-ng
def packetforge_ng():
    if os.path.isfile("/usr/bin/packetforge-ng"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL packetforge-ng ☣" -geometry 100x30 -e "sudo apt install packetforge-ng"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/packetforge-ng"):
            print(B("packetforge-ng Already Installed"))
        else:
            print(R("packetforge-ng Not Installed"))
        input()
        back()
    # end packetforge_ng

#PixieWPS
def pixiewps():
    if os.path.isfile("/usr/bin/pixiewps"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL pixiewps ☣" -geometry 100x30 -e "sudo apt install pixiewps"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/pixiewps"):
            print(B("pixiewps Already Installed"))
        else:
            print(R("pixiewps Not Installed"))
        input()
        back()
    # end pixiewps

#Pyrit
def pyrit():
    if os.path.isfile("/usr/bin/pyrit"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL pyrit ☣" -geometry 100x30 -e "sudo apt install pyrit"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/pyrit"):
            print(B("pyrit Already Installed"))
        else:
            print(R("pyrit Not Installed"))
        input()
        back()
    # end pyrit

#Reaver
def reaver():
    if os.path.isfile("/usr/bin/reaver"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL reaver ☣" -geometry 100x30 -e "sudo apt install reaver"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/reaver"):
            print(B("reaver Already Installed"))
        else:
            print(R("reaver Not Installed"))
        input()
        back()
    # end reaver

#redfang
def redfang():
    if os.path.isfile("/usr/bin/redfang"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL redfang ☣" -geometry 100x30 -e "sudo apt install redfang"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/redfang"):
            print(B("redfang Already Installed"))
        else:
            print(R("redfang Not Installed"))
        input()
        back()
    # end redfang

#RTLSDR Scanner
def rtlsdr_scanner():
    if os.path.isfile("/usr/bin/rtl_scan"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL rtl_scan ☣" -geometry 100x30 -e "sudo apt install rtl_scan"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/rtl_scan"):
            print(B("rtl_scan Already Installed"))
        else:
            print(R("rtl_scan Not Installed"))
        input()
        back()
    # end rtlsdr_scanner

#spooftooph
def spooftooph():
    if os.path.isfile("/usr/bin/spooftooph"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL spooftooph ☣" -geometry 100x30 -e "sudo apt install spooftooph"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/spooftooph"):
            print(B("spooftooph Already Installed"))
        else:
            print(R("spooftooph Not Installed"))
        input()
        back()
    # end spooftooph

#Tkiptun-ng
def tkiptun_ng():
    if os.path.isfile("/usr/bin/tkiptun-ng"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL tkiptun-ng ☣" -geometry 100x30 -e "sudo apt install tkiptun-ng"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/tkiptun-ng"):
            print(B("tkiptun-ng Already Installed"))
        else:
            print(R("tkiptun-ng Not Installed"))
        input()
        back()
    # end tkiptun_ng

#Wesside-ng
def wesside_ng():
    if os.path.isfile("/usr/bin/wesside-ng"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL wesside-ng ☣" -geometry 100x30 -e "sudo apt install wesside-ng"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/wesside-ng"):
            print(B("wesside-ng Already Installed"))
        else:
            print(R("wesside-ng Not Installed"))
        input()
        back()
    # end wesside_ng

#Wifi Honey
def wifi_honey():
    if os.path.isfile("/usr/bin/wifiphisher"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL wifiphisher ☣" -geometry 100x30 -e "sudo apt install wifiphisher"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/wifiphisher"):
            print(B("wifiphisher Already Installed"))
        else:
            print(R("wifiphisher Not Installed"))
        input()
        back()
    # end wifi_honey

#wifiphiser
def wifiphiser():
    if os.path.isfile("/usr/bin/wifiphiser"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL wifiphiser ☣" -geometry 100x30 -e "sudo apt install wifiphiser"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/wifiphiser"):
            print(B("wifiphiser Already Installed"))
        else:
            print(R("wifiphiser Not Installed"))
        input()
        back()
    # end wifiphiser

#wifitap
def wifitap():
    if os.path.isfile("/usr/bin/wifitap"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL wifitap ☣" -geometry 100x30 -e "sudo apt install wifitap"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/wifitap"):
            print(B("wifitap Already Installed"))
        else:
            print(R("wifitap Not Installed"))
        input()
        back()
    # end wifitap

#wifite
def wifite():
    if os.path.isfile("/usr/bin/wifite"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL wifite ☣" -geometry 100x30 -e "sudo apt install wifite"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/wifite"):
            print(B("wifite Already Installed"))
        else:
            print(R("wifite Not Installed"))
        input()
        back()
    # end wifite

#wpaclean
def wpaclean():
    if os.path.isfile("/usr/bin/wpaclean"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL wpaclean ☣" -geometry 100x30 -e "sudo apt install wpaclean"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/wpaclean"):
            print(B("wpaclean Already Installed"))
        else:
            print(R("wpaclean Not Installed"))
        input()
        back()
    # end wpaclean
    
#Airgeddon
def airgeddon():
    if os.path.isfile("/usr/bin/airgeddon"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL airgeddon ☣" -geometry 100x30 -e "sudo apt install airgeddon"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/airgeddon"):
            print(B("airgeddon Already Installed"))
        else:
            print(R("airgeddon Not Installed"))
        input()
        back()
    # end airgeddon

def back():
    WireAttack()


