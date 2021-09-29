
import os
from color import *
import Logo


def Sniffing():
    os.system("clear")
    Logo.logo_13()
    print(
        G(
            """
    1. Bettercap
    2. Brup Suite
    3. DNSChef
    4. Fiked
    5. Hamster-sidejack
    6. HexInject
    7. IaxFlood
    8. Inviteflood
    9. iSMTP
    10. isr-evilgrade
    11. Mitmproxy
    12. ohrwurm
    13. protos-sip
    14. rebind
    15. responder
    16. rtpbreak
    17. rtpinsertsound
    18. rtpmixsound
    19. sctpscan
    20. SIPArmyKnife
    21. SIPp
    22. SIPVicious
    23. SniffJoke
    24. SSLsplit
    25. sslstrip
    26. thc-ipv6
    27. VoIPHopper
    28. WebScarab
    29. Wifi Honey
    30. Wireshark
    31. xspy
    32. Yersinia
    33. zaproxy
    0.  Back to Main Menu 
            """
        )
    )
    print(R("    00. exit"))
    menu = input(G("[") + R("DracOS") + G("]select>"))
    if menu == "1":
        # Call function
        Bettercap()
    elif menu == "2":
        # Call function
        Brup_Suite()
    elif menu == "3":
        # Call function
        DNSChef()
    elif menu == "4":
        # Call function
        Fiked()
    elif menu == "5":
        # Call function
        Hamster_sidejack()
    elif menu == "6":
        # Call function
        HexInject()
    elif menu == "7":
        # Call function
        IaxFlood()
    elif menu == "8":
        # Call function
        Inviteflood()
    elif menu == "9":
        # Call function
        iSMTP()
    elif menu == "10":
        # Call function
        isr_evilgrade()
    elif menu == "11":
        # Call function
        Mitmproxy()
    elif menu == "12":
        # Call function
        ohrwurm()
    elif menu == "13":
        # Call function
        protos_sip()
    elif menu == "14":
        # Call function
        rebind()
    elif menu == "15":
        # Call function
        responder()
    elif menu == "16":
        # Call function
        rtpbreak()
    elif menu == "17":
        # Call function
        rtpinsertsound()
    elif menu == "18":
        # Call function
        rtpmixsound()
    elif menu == "19":
        # Call function
        sctpscan()
    elif menu == "20":
        # Call function
        SIPArmyKnife()
    elif menu == "21":
        # Call function
        SIPp()
    elif menu == "22":
        # Call function
        SIPVicious()
    elif menu == "23":
        # Call function
        SniffJoke()
    elif menu == "24":
        # Call function
        SSLsplit()
    elif menu == "25":
        # Call function
        sslstrip()
    elif menu == "26":
        # Call function
        thc_ipv6()
    elif menu == "27":
        # Call function
        VoIPHopper()
    elif menu == "28":
        # Call function
        WebScarab()
    elif menu == "29":
        # Call function
        Wifi_Honey()
    elif menu == "30":
        # Call function
        Wireshark()
    elif menu == "31":
        # Call function
        xspy()
    elif menu == "32":
        # Call function
        Yersinia()
    elif menu == "33":
        # Call function
        zaproxy()
    elif menu == "0":
        os.system("python3 /usr/bin/DracOS_VENOMIZER/venomizer.py")  # //usr/bin/
    elif menu == "00":
        exit()
    else:
        print(R('Wrong Input!'))
        input()
        back()


def back():
    Sniffing()


#function
#Bettercap
def Bettercap():
    if os.path.isfile("/usr/bin/bettercap"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Bettercap ☣" -geometry 100x30 -e "sudo apt install bettercap"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/bettercap"):
            print(B("Bettercap Already Installed"))
        else:
            print(R("Bettercap Not Installed"))
        input()
        back()
    # end Bettercap

#Brup Suite
def Brup_Suite():
    if os.path.isfile("/usr/bin/brup"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Brup Suite ☣" -geometry 100x30 -e "sudo apt install brup"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/brup"):
            print(B("Brup Suite Already Installed"))
        else:
            print(R("Brup Suite Not Installed"))
        input()
        back()
    # end Brup_Suite

#DNSChef
def DNSChef():
    if os.path.isfile("/usr/bin/dnschef"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL DNSChef ☣" -geometry 100x30 -e "sudo apt install dnschef"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/dnschef"):
            print(B("DNSChef Already Installed"))
        else:
            print(R("DNSChef Not Installed"))
        input()
        back()
    # end DNSChef

#Fiked
def Fiked():
    if os.path.isfile("/usr/bin/fiked"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Fiked ☣" -geometry 100x30 -e "sudo apt install fiked"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/fiked"):
            print(B("Fiked Already Installed"))
        else:
            print(R("Fiked Not Installed"))
        input()
        back()
    # end Fiked

#Hamster-sidejack
def Hamster_sidejack():
    if os.path.isfile("/usr/bin/hamster-sidejack"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Hamster-sidejack ☣" -geometry 100x30 -e "sudo apt install hamster-sidejack"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/hamster-sidejack"):
            print(B("Hamster-sidejack Already Installed"))
        else:
            print(R("Hamster-sidejack Not Installed"))
        input()
        back()
    # end Hamster_sidejack

#HexInject
def HexInject():
    if os.path.isfile("/usr/bin/hexinject"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL HexInject ☣" -geometry 100x30 -e "sudo apt install hexinject"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/hexinject"):
            print(B("HexInject Already Installed"))
        else:
            print(R("HexInject Not Installed"))
        input()
        back()
    # end HexInject

#IaxFlood
def IaxFlood():
    if os.path.isfile("/usr/bin/iaxflood"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL IaxFlood ☣" -geometry 100x30 -e "sudo apt install iaxflood"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/iaxflood"):
            print(B("IaxFlood Already Installed"))
        else:
            print(R("IaxFlood Not Installed"))
        input()
        back()
    # end IaxFlood
    
#Inviteflood
def Inviteflood():
    if os.path.isfile("/usr/bin/inviteflood"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Inviteflood ☣" -geometry 100x30 -e "sudo apt install inviteflood"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/inviteflood"):
            print(B("Inviteflood Already Installed"))
        else:
            print(R("Inviteflood Not Installed"))
        input()
        back()
    # end Inviteflood

#iSMTP
def iSMTP():
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
            print(R("iSMTP Not Installed"))
        input()
        back()
    # end iSMTP

#isr-evilgrade
def isr_evilgrade():
    if os.path.isfile("/usr/bin/isr-evilgrade"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL isr-evilgrade ☣" -geometry 100x30 -e "sudo apt install isr-evilgrade"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/isr-evilgrade"):
            print(B("isr-evilgrade Already Installed"))
        else:
            print(R("isr-evilgrade Not Installed"))
        input()
        back()
    # end isr_evilgrade

#Mitmproxy
def Mitmproxy():
    if os.path.isfile("/usr/bin/mitmproxy"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Mitmproxy ☣" -geometry 100x30 -e "sudo apt install mitmproxy"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/mitmproxy"):
            print(B("Mitmproxy Already Installed"))
        else:
            print(R("Mitmproxy Not Installed"))
        input()
        
    # end Mitmproxy

#ohrwurm
def ohrwurm():
    if os.path.isfile("/usr/bin/ohrwurm"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL ohrwurm ☣" -geometry 100x30 -e "sudo apt install ohrwurm"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/ohrwurm"):
            print(B("ohrwurm Already Installed"))
        else:
            print(R("ohrwurm Not Installed"))
        input()
        back()
    # end ohrwurm

#protos-sip
def protos_sip():
    if os.path.isfile("/usr/bin/protos-sip"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL protos-sip ☣" -geometry 100x30 -e "sudo apt install protos-sip"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/protos-sip"):
            print(B("protos-sip Already Installed"))
        else:
            print(R("protos-sip Not Installed"))
        input()
        back()
    # end protos_sip

#rebind
def rebind():
    if os.path.isfile("/usr/bin/rebind"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL rebind ☣" -geometry 100x30 -e "sudo apt install rebind"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/rebind"):
            print(B("rebind Already Installed"))
        else:
            print(R("rebind Not Installed"))
        input()
        back()
    # end rebind

#responder
def responder():
    if os.path.isfile("/usr/bin/responder"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Responder ☣" -geometry 100x30 -e "sudo apt install responder"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/responder"):
            print(B("responder Already Installed"))
        else:
            print(R("responder Not Installed"))
        input()
        back()
    # end responder

#rtpbreak
def rtpbreak():
    if os.path.isfile("/usr/bin/rtpbreak"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL rtpbreak ☣" -geometry 100x30 -e "sudo apt install rtpbreak"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/rtpbreak"):
            print(B("rtpbreak Already Installed"))
        else:
            print(R("rtpbreak Not Installed"))
        input()
        back()
    # end rtpbreak

#rtpinsertsound
def rtpinsertsound():
    if os.path.isfile("/usr/bin/rtpinsertsound"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL rtpinsertsound ☣" -geometry 100x30 -e "sudo apt install rtpinsertsound"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/rtpinsertsound"):
            print(B("rtpinsertsound Already Installed"))
        else:
            print(R("rtpinsertsound Not Installed"))
        input()
        back()
    # end rtpinsertsound

#rtpmixsound
def rtpmixsound():
    if os.path.isfile("/usr/bin/rtpmixsound"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL rtpmixsound ☣" -geometry 100x30 -e "sudo apt install rtpmixsound"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/rtpmixsound"):
            print(B("rtpmixsound Already Installed"))
        else:
            print(R("rtpmixsound Not Installed"))
        input()
        back()
    # end rtpmixsound

#sctpscan
def sctpscan():
    if os.path.isfile("/usr/bin/sctpscan"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL sctpscan ☣" -geometry 100x30 -e "sudo apt install sctpscan"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/sctpscan"):
            print(B("sctpscan Already Installed"))
        else:
            print(R("sctpscan Not Installed"))
        input()
        back()
    # end sctpscan

#SIPArmyKnife
def SIPArmyKnife():
    if os.path.isfile("/usr/bin/SIPArmyKnife"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL SIPArmyKnife ☣" -geometry 100x30 -e "sudo apt install siparmyknife"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/SIPArmyKnife"):
            print(B("SIPArmyKnife Already Installed"))
        else:
            print(R("SIPArmyKnife Not Installed"))
        input()
        back()
    # end SIPArmyKnife

#SIPp
def SIPp():
    if os.path.isfile("/usr/bin/SIPp"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL SIPp ☣" -geometry 100x30 -e "sudo apt install sipp"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/SIPp"):
            print(B("SIPp Already Installed"))
        else:
            print(R("SIPp Not Installed"))
        input()
        back()
    # end SIPp

#SIPVicious
def SIPVicious():
    if os.path.isfile("/usr/bin/SIPVicious"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL SIPVicious ☣" -geometry 100x30 -e "sudo apt install sipvicious"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/SIPVicious"):
            print(B("SIPVicious Already Installed"))
        else:
            print(R("SIPVicious Not Installed"))
        input()
        back()
    # end SIPVicious

#SniffJoke
def SniffJoke():
    if os.path.isfile("/usr/bin/SniffJoke"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL SniffJoke ☣" -geometry 100x30 -e "sudo apt install sniffjoke"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/SniffJoke"):
            print(B("SniffJoke Already Installed"))
        else:
            print(R("SniffJoke Not Installed"))
        input()
        back()
    # end SniffJoke

#SSLsplit
def SSLsplit():
    if os.path.isfile("/usr/bin/sslsplit"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL SSLsplit ☣" -geometry 100x30 -e "sudo apt install sslsplit"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/sslsplit"):
            print(B("sslsplit Already Installed"))
        else:
            print(R("sslsplit Not Installed"))
        input()
        back()
    # end sslsplit

#sslstrip
def sslstrip():
    if os.path.isfile("/usr/bin/sslstrip"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL sslstrip ☣" -geometry 100x30 -e "sudo apt install sslstrip"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/sslstrip"):
            print(B("sslstrip Already Installed"))
        else:
            print(R("sslstrip Not Installed"))
        input()
        back()
    # end sslstrip

#thc-ipv6
def thc_ipv6():
    if os.path.isfile("/usr/bin/thc-ipv6"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL thc-ipv6 ☣" -geometry 100x30 -e "sudo apt install thc-ipv6"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/thc-ipv6"):
            print(B("thc-ipv6 Already Installed"))
        else:
            print(R("thc-ipv6 Not Installed"))
        input()
        back()
    # end thc-ipv6

#VoIPHopper
def VoIPHopper():
    if os.path.isfile("/usr/bin/VoIPHopper"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL VoIPHopper ☣" -geometry 100x30 -e "sudo apt install voiphopper"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/VoIPHopper"):
            print(B("VoIPHopper Already Installed"))
        else:
            print(R("VoIPHopper Not Installed"))
        input()
        back()
    # end VoIPHopper

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

#Wifi Honey
def Wifi_Honey():
    if os.path.isfile("/usr/bin/wifi-honey"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Wifi Honey ☣" -geometry 100x30 -e "sudo apt install wifi-honey"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/wifi-honey"):
            print(B("Wifi Honey Already Installed"))
        else:
            print(R("Wifi Honey Not Installed"))
        input()
        back()
    # end Wifi Honey

#Wireshark
def Wireshark():
    if os.path.isfile("/usr/bin/wireshark"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Wireshark ☣" -geometry 100x30 -e "sudo apt install wireshark"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/wireshark"):
            print(B("Wireshark Already Installed"))
        else:
            print(R("Wireshark Not Installed"))
        input()
        back()
    # end Wireshark

#xspy
def xspy():
    if os.path.isfile("/usr/bin/xspy"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL xspy ☣" -geometry 100x30 -e "sudo apt install xspy"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/xspy"):
            print(B("xspy Already Installed"))
        else:
            print(R("xspy Not Installed"))
        input()
        back()
    # end xspy

#Yersinia
def Yersinia():
    if os.path.isfile("/usr/bin/yersinia"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Yersinia ☣" -geometry 100x30 -e "sudo apt install yersinia"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/yersinia"):
            print(B("Yersinia Already Installed"))
        else:
            print(R("Yersinia Not Installed"))
        input()
        back()
    # end Yersinia

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



#loop
# while True:
#     Sniffing()