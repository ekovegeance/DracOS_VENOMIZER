#!/usr/bin/python3
import os
from color import *
import Logo

#
def InfoGat():
    os.system("clear")
    Logo.logo_10()
    print(
        G(
            """ 
    1.  Nmap
    2.  Amap
    3.  Whatweb
    4.  Sublist3r
    5.  Arp-scan
    6.  Automater
    7.  Braa
    8.  Casefile
    9.  Cdpsnarf (Not Found)
    10. Cisco-torch
    11. Dmitry
    12. Dnsenum
    13. Dnsmap
    14. DNSRecon
    15. Dnstracer
    16. Dnswalk
    17. python-faraday
    18. Fierce
    19. Firewalk
    20. Fragroute(Not Found)
    21. fragrouter
    22. Ghost-Phisher(Not Found)
    23. GoLismero(Not Found)
    24. Goofile
    25. Hping3
    26. Inspy
    27. Intrace
    28. iSMTP
    29. Maltego Teeth
    30. Masscan
    31. Metagoofil
    32. Miranda
    33. Nikto
    34. Ntop
    35. Recon-ng
    36. Smbmap
    37. Smtp-user-enum
    38  Snmp-check
    39. Sslcaudit
    40. SSLsplit
    0.  back """
        )
    )
    print(R("    00. exit"))
    menu = input(G("[") + R("DracOS") + G("]select>"))
    if menu == "1":
        # Call function
        nmap()
    elif menu == "2":
        # Call function
        amap()
    elif menu == "3":
        # Call function
        whatweb()
    elif menu == "4":
        # Call function
        sublist3r()
    elif menu == "5":
        # Call function
        arp_scan()
    elif menu == "6":
        # Call function
        automater()
    elif menu == "7":
        # Call function
        braa()
    elif menu == "8":
        # Call function
        casefile()
    elif menu == "9":
        # Call function
        cdpsnarf()
    elif menu == "10":
        # Call function
        cisco_torch()
    elif menu == "11":
        # Call function
        dmitry()
    elif menu == "12":
        # Call function
        dnsenum()
    elif menu == "13":
        # Call function
        dnsmap()
    elif menu == "14":
        # Call function
        dnsrecon()
    elif menu == "15":
        # Call function
        dnstracer()
    elif menu == "16":
        # Call function
        dnswalk()
    elif menu == "17":
        # Call function
        faraday()
    elif menu == "18":
        # Call function
        fierce()
    elif menu == "19":
        # Call function
        firewalk()
    elif menu == "20":
        # Call function
        fragroute()
    elif menu == "21":
        # Call function
        fragrouter()
    elif menu == "22":
        # Call function
        ghost_phisher()
    elif menu == "23":
        # Call function
        golismero()
    elif menu == "24":
        # Call function
        goofile()
    elif menu == "25":
        # Call function
        hping3()
    elif menu == "26":
        # Call function
        inspy()
    elif menu == "27":
        # Call function
        intrace()
    elif menu == "28":
        # Call function
        ismtp()
    elif menu == "29":
        # Call function
        maltego_teeth()
    elif menu == "30":
        # Call function
        masscan()
    elif menu == "31":
        # Call function
        metagoofil()
    elif menu == "32":
        # Call function
        miranda()
    elif menu == "33":
        # Call function
        nikto()
    elif menu == "34":
        # Call function
        ntop()
    elif menu == "35":
        # Call function
        recon_ng()
    elif menu == "36":
        # Call function
        smbmap()
    elif menu == "37":
        # Call function
        smtp_user_enum()
    elif menu == "38":
        # Call function
        snmp_check()
    elif menu == "39":
        # Call function
        sslcaudit_()
    elif menu == "40":
        # Call function
        sslsplit()
    elif menu == "0":
        os.system("python3 /usr/bin/DracOS_VENOMIZER/venomizer.py")  # /usr/bin/
    elif menu == "00":
        exit()
    else:
        print(R('Wrong Input!'))
        input()
        back()


# tambah fungsi tools lalu panggil ke dalam fungsi InfoGat
# NMAP
def nmap():
    if os.path.isfile("/usr/bin/nmap"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL NMAP ☣" -geometry 100x30 -e "sudo apt install nmap"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/nmap"):
            print(B("NMAP Already Installed"))
        else:
            print(R("Error Installing NMAP"))
        input()
        back()
        # end NMAP


# AMAP
def amap():
    if os.path.isfile("/usr/bin/amap"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL AMAP ☣" -geometry 100x30 -e "sudo apt install amap"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/amap"):
            print(B("AMAP Already Installed"))
        else:
            print(R("Error Installing AMAP"))
        input()
        back()
    # end AMAP


# WHATWEB
def whatweb():
    if os.path.isfile("/usr/bin/whatweb"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL WHATWEB ☣" -geometry 100x30 -e "sudo apt install whatweb"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/whatweb"):
            print(B("WHATWEB Already Installed"))
        else:
            print(R("Error Installing WHATWEB"))
        input()
        back()
    # end WHATWEB


# Sublist3r
def sublist3r():
    if os.path.isfile("/usr/bin/sublist3r"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Sublist3r ☣" -geometry 100x30 -e "sudo apt install sublist3r"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/sublist3r"):
            print(B("Sublist3r Already Installed"))
        else:
            print(R("Error Installing Sublist3r"))
        input()
        back()
    # end Sublist3r


# arp-scan
def arp_scan():
    if os.path.isfile("/usr/bin/arp-scan") or os.path.isfile('/usr/sbin/arp-scan') or os.path.isfile('/usr/share/arp-scan'):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL ARP-SCAN ☣" -geometry 100x30 -e "sudo apt install arp-scan"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/arp-scan") or os.path.isfile('/usr/sbin/arp-scan') or os.path.isfile('/usr/share/arp-scan'):
            print(B("ARP-SCAN Already Installed"))
        else:
            print(R("Error Installing ARP-SCAN"))
        input()
        back()
    # end ARP-SCAN


# Automater
def automater():
    if os.path.isfile("/usr/bin/automater"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Automater ☣" -geometry 100x30 -e "git clone https://gitlab.com/kalilinux/packages/automater.git"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/automater"):
            print(B("Automater Already Installed"))
        else:
            print(R("Error Installing Automater"))
        input()
        back()
    # end Automater


# Braa
def braa():
    if os.path.isfile("/usr/bin/braa"):
        
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Braa ☣" -geometry 100x30 -e "sudo apt install braa"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/braa"):
            print(B("Braa Already Installed"))
        else:
            print(R("Error Installing Braa"))
        input()
        back()
    # end Braa


# Casefile
def casefile():
    if os.path.isfile("/usr/bin/casefile"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Casefile ☣" -geometry 100x30 -e "sudo apt install casefile"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/casefile"):
            print(B("Casefile Already Installed"))
        else:
            print(R("Error Installing Casefile"))
        input()
        back()
    # end Casefile


# Cdpsnarf
def cdpsnarf():
    if os.path.isfile("/usr/bin/cdpsnarf"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Cdpsnarf ☣" -geometry 100x30 -e "sudo apt install cdpsnarf"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/cdpsnarf"):
            print(B("Cdpsnarf Already Installed"))
        else:
            print(R("Error Installing Cdpsnarf"))
        input()
        back()
    # end Cdpsnarf


# Cisco-torch
def cisco_torch():
    if os.path.isfile("/usr/bin/cisco-torch"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Cisco-torch ☣" -geometry 100x30 -e "sudo apt install cisco-torch"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/cisco-torch"):
            print(B("Cisco-torch Already Installed"))
        else:
            print(R("Error Installing Cisco-torch"))
        input()
        back()
    # end Cisco-torch


# Dmitry
def dmitry():
    if os.path.isfile("/usr/bin/dmitry"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Dmitry ☣" -geometry 100x30 -e "sudo apt install dmitry"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/dmitry"):
            print(B("Dmitry Already Installed"))
        else:
            print(R("Error Installing Dmitry"))
        input()
        back()
    # end Dmitry


# Dnsenum
def dnsenum():
    if os.path.isfile("/usr/bin/dnsenum"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Dnsenum ☣" -geometry 100x30 -e "sudo apt install dnsenum"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/dnsenum"):
            print(B("Dnsenum Already Installed"))
        else:
            print(R("Error Installing Dnsenum"))
        input()
        back()
    # end Dnsenum


# Dnsmap
def dnsmap():
    if os.path.isfile("/usr/bin/dnsmap"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Dnsmap ☣" -geometry 100x30 -e "sudo apt install dnsmap"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/dnsmap"):
            print(B("Dnsmap Already Installed"))
        else:
            print(R("Error Installing Dnsmap"))
        input()
        back()
    # end Dnsmap


# DNSRecon
def dnsrecon():
    if os.path.isfile("/usr/bin/dnsrecon"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL DNSRecon ☣" -geometry 100x30 -e "sudo apt install dnsrecon"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/dnsrecon"):
            print(B("DNSRecon Already Installed"))
        else:
            print(R("Error Installing DNSRecon"))
        input()
        back()
    # end DNSRecon


# Dnstracer
def dnstracer():
    if os.path.isfile("/usr/bin/dnstracer"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Dnstracer ☣" -geometry 100x30 -e "sudo apt install dnstracer"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/dnstracer"):
            print(B("Dnstracer Already Installed"))
        else:
            print(R("Error Installing Dnstracer"))
        input()
        back()
    # end Dnstracer


# Dnswalk
def dnswalk():
    if os.path.isfile("/usr/bin/dnswalk"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Dnswalk ☣" -geometry 100x30 -e "sudo apt install dnswalk"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/dnswalk"):
            print(B("Dnswalk Already Installed"))
        else:
            print(R("Error Installing Dnswalk"))
        input()
        back()
    # end Dnswalk


# python-faraday
def faraday():
    if os.path.isfile("/usr/bin/faraday"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Faraday ☣" -geometry 100x30 -e "sudo apt install faraday"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/faraday"):
            print(B("Faraday Already Installed"))
        else:
            print(R("Error Installing Faraday"))
        input()
        back()
    # end Faraday


# Fierce
def fierce():
    if os.path.isfile("/usr/bin/fierce"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Fierce ☣" -geometry 100x30 -e "sudo apt install fierce"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/fierce"):
            print(B("Fierce Already Installed"))
        else:
            print(R("Error Installing Fierce"))
        input()
        back()
    # end Fierce


# Firewalk
def firewalk():
    if os.path.isfile("/usr/bin/firewalk") or os.path.isfile('/usr/sbin/firewalk'):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Firewalk ☣" -geometry 100x30 -e "sudo apt install firewalk"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/firewalk"):
            print(B("Firewalk Already Installed"))
        else:
            print(R("Error Installing Firewalk"))
        input()
        back()
    # end Firewalk


# Fragroute
def fragroute():
    if os.path.isfile("/usr/bin/fragroute"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Fragroute ☣" -geometry 100x30 -e "sudo apt install fragroute"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/fragroute"):
            print(B("Fragroute Already Installed"))
        else:
            print(R("Error Installing Fragroute"))
        input()
        back()
    # end Fragroute


# fragrouter
def fragrouter():
    if os.path.isfile("/usr/bin/fragrouter"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Fragrouter ☣" -geometry 100x30 -e "sudo apt install fragrouter"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/fragrouter"):
            print(B("Fragrouter Already Installed"))
        else:
            print(R("Error Installing Fragrouter"))
        input()
        back()
    # end Fragrouter


# Ghost-Phisher
def ghost_phisher():
    if os.path.isfile("/usr/bin/ghost-phisher"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Ghost-Phisher ☣" -geometry 100x30 -e "sudo apt install ghost-phisher"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/ghost-phisher"):
            print(B("Ghost-Phisher Already Installed"))
        else:
            print(R("Error Installing Ghost-Phisher"))
        input()
        back()
    # end Ghost-Phisher


# GoLismero
def golismero():
    if os.path.isfile("/usr/bin/golismero"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL GoLismero ☣" -geometry 100x30 -e "sudo apt install golismero"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/golismero"):
            print(B("Golismero Already Installed"))
        else:
            print(R("Error Installing Golismero"))
        input()
        back()
    # end GoLismero


# Goofile
def goofile():
    if os.path.isfile("/usr/bin/goofile"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Goofile ☣" -geometry 100x30 -e "sudo apt install goofile"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/goofile"):
            print(B("Goofile Already Installed"))
        input()
        back()
    # end Goofile


# Hping3
def hping3():
    if os.path.isfile("/usr/bin/hping3") or os.path.isfile('/usr/sbin/hping3'):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Hping3 ☣" -geometry 100x30 -e "sudo apt install hping3"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/hping3") or os.path.isfile('/usr/sbin/hping3'):
            print(B("Hping3 Already Installed"))
        else:
            print(R("Error Installing Hping3"))
        input()
        back()
    # end Hping3


# Inspy
def inspy():
    if os.path.isfile("/usr/bin/inspy"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Inspy ☣" -geometry 100x30 -e "sudo apt install inspy"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/inspy"):
            print(B("Inspy Already Installed"))
        else:
            print(R("Error Installing Inspy"))
        input()
        back()
    # end Inspy


# Intrace
def intrace():
    if os.path.isfile("/usr/bin/intrace"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Intrace ☣" -geometry 100x30 -e "sudo apt install intrace"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/intrace"):
            print(B("Intrace Already Installed"))
        else:
            print(R("Error Installing Intrace"))
        input()
        back()
    # end Intrace


# iSMTP
def ismtp():
    if os.path.isfile("/usr/bin/ismtp"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL iSMTP ☣" -geometry 100x30 -e "sudo apt install ismtp"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/ismtp"):
            print(B("iSMTP Already Installed"))
        else:
            print(R("Error Installing iSMTP"))
        input()
        back()
    # end iSMTP


# Teeth
def teeth():
    if os.path.isfile("/usr/bin/teeth"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Teeth ☣" -geometry 100x30 -e "sudo apt install teeth"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/teeth"):
            print(B("Teeth Already Installed"))
        else:
            print(R("Error Installing Teeth"))
        input()
        back()
    # end Teeth


# Masscan
def masscan():
    if os.path.isfile("/usr/bin/masscan"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Masscan ☣" -geometry 100x30 -e "sudo apt install masscan"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/masscan"):
            print(B("Masscan Already Installed"))
        else:
            print(R("Error Installing Masscan"))
        input()
        back()
    # end Masscan


# Metagoofil
def metagoofil():
    if os.path.isfile("/usr/bin/metagoofil"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Metagoofil ☣" -geometry 100x30 -e "sudo apt install metagoofil"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/metagoofil"):
            print(B("Metagoofil Already Installed"))
        else:
            print(R("Error Installing Metagoofil"))
        input()
        back()
    # end Metagoofil


# Miranda
def miranda():
    if os.path.isfile("/usr/bin/miranda"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Miranda ☣" -geometry 100x30 -e "sudo apt install miranda"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/miranda"):
            print(B("Miranda Already Installed"))
        else:
            print(R("Error Installing Miranda"))
        input()
        back()
    # end Miranda


# Nikto
def nikto():
    if os.path.isfile("/usr/bin/nikto"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Nikto ☣" -geometry 100x30 -e "sudo apt install nikto"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/nikto"):
            print(B("Nikto Already Installed"))
        else:
            print(R("Error Installing Nikto"))
        input()
        back()
    # end Nikto


# Ntop
def ntop():
    if os.path.isfile("/usr/bin/ntop"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Ntop ☣" -geometry 100x30 -e "sudo apt install ntop"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/ntop"):
            print(B("Ntop Already Installed"))
        else:
            print(R("Error Installing Ntop"))
        input()
        back()
    # end Ntop


# Recon-ng
def reconng():
    if os.path.isfile("/usr/bin/recon-ng"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Recon-ng ☣" -geometry 100x30 -e "sudo apt install recon-ng"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/recon-ng"):
            print(B("Recon-ng Already Installed"))
        else:
            print(R("Error Installing Recon-ng"))
        input()
        back()
    # end Recon-ng


# Smbmap
def smbmap():
    if os.path.isfile("/usr/bin/smbmap"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Smbmap ☣" -geometry 100x30 -e "sudo apt install smbmap"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/smbmap"):
            print(B("Smbmap Already Installed"))
        else:
            print(R("Error Installing Smbmap"))
        input()
        back()
    # end Smbmap


# Smtp-user-enum
def smtpuserenum():
    if os.path.isfile("/usr/bin/smtp-user-enum"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Smtp-user-enum ☣" -geometry 100x30 -e "sudo apt install smtp-user-enum"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/smtp-user-enum"):
            print(B("Smtp-user-enum Already Installed"))
        else:
            print(R("Error Installing Smtp-user-enum"))
        input()
        back()
    # end Smtp-user-enum


# Snmp-check
def snmpcheck():
    if os.path.isfile("/usr/bin/snmp-check"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Snmp-check ☣" -geometry 100x30 -e "sudo apt install snmp-check"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/snmp-check"):
            print(B("Snmp-check Already Installed"))
        else:
            print(R("Error Installing Snmp-check"))
        input()
        back()
    # end Snmp-check


# Sslcaudit
def sslaudit():
    if os.path.isfile("/usr/bin/sslcaudit"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Sslcaudit ☣" -geometry 100x30 -e "sudo apt install sslcaudit"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/sslcaudit"):
            print(B("Sslcaudit Already Installed"))
        else:
            print(R("Error Installing Sslcaudit"))
        input()
        back()
    # end Sslcaudit


# SSLsplit
def sslsplit():
    if os.path.isfile("/usr/bin/sslsplit"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Sslsplit ☣" -geometry 100x30 -e "sudo apt install sslsplit"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/sslsplit"):
            print(B("Sslsplit Already Installed"))
        else:
            print(R("Error Installing Sslsplit"))
        input()
        back()
    # end Sslsplit


# Maltego
def maltego_teeth():
    if os.path.isfile("/usr/bin/maltego"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Maltego-teeth ☣" -geometry 100x30 -e "sudo apt install maltego-teeth"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/maltego"):
            print(B("Maltego-teeth Already Installed"))
        else:
            print(R("Error Installing Maltego-teeth"))
        input()
        back()
    # end Maltego-teeth


# Recon-ng
def recon_ng():
    if os.path.isfile("/usr/bin/recon-ng"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Recon-ng ☣" -geometry 100x30 -e "sudo apt install recon-ng"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/recon-ng"):
            print(B("Recon-ng Already Installed"))
        else:
            print(R("Error Installing Recon-ng"))
        input()
        back()
    # end Recon-ng


# smtp_user_enum
def smtp_user_enum():
    if os.path.isfile("/usr/bin/smtp-user-enum"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Smtp-user-enum ☣" -geometry 100x30 -e "sudo apt install smtp-user-enum"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/smtp-user-enum"):
            print(B("Smtp-user-enum Already Installed"))
        else:
            print(R("Error Installing Smtp-user-enum"))
        input()
        back()
    # end Smtp-user-enum


# Snmp-check
def snmp_check():
    if os.path.isfile("/usr/bin/snmp-check"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Snmp-check ☣" -geometry 100x30 -e "sudo apt install snmp-check"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/snmp-check"):
            print(B("Snmp-check Already Installed"))
        else:
            print(R("Error Installing Snmp-check"))
        input()
        back()
    # end Snmp-check


# sslcaudit
def sslcaudit_():
    if os.path.isfile("/usr/bin/sslcaudit"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Sslcaudit ☣" -geometry 100x30 -e "sudo apt install sslcaudit"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/sslcaudit"):
            print(B("Sslcaudit Already Installed"))
        else:
            print(R("Error Installing Sslcaudit"))
        input()
        back()
    # end Sslcaudit

# fungsi untuk memanggil lagi InfoGat
# supaya program tidak keluar
def back():
    InfoGat()
# Looping
# while True:
#     InfoGat()
