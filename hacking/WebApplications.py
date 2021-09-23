import os
from color import*
import Logo

def WebApp():
    os.system('clear')
    # Logo
    Logo.logo_16()
    print(G(""" 
    1.  apache-users
    2.  Arachni(nothing)
    3.  BBQSQL
    4.  BlindElephant
    5.  Burp Suite
    6.  CutyCapt
    7.  DAVtest
    8.  deblaze
    9.  DIRB
    10. DirBuster
    11. fimap
    12. FunkLoad
    13. Gobuster
    14. Grabber
    15. hURL
    16. jboss-autopwn
    17. joomscan
    18. jSQL     Injection
    19. Maltego Teetch
    20. Nikto
    21. PadBuster
    22. Paros
    23. Parsero
    24. plecost
    25. Powerfuzzer
    26. ProxyStrike
    27. Recon-ng
    28. Skipfish
    29. sqlmap
    30. sqlninja
    31. sqlsus
    32. ua-tester
    33. Uniscan
    34. w3af
    35. WebScarab
    36. WebShag
    37. WebSlayer
    38. WebSploit
    39. wfuzz
    40. Whatweb
    41. WPScan
    42. XSSer
    43. zaproxy
    0. back """))
    print(R("    00. exit"))
    menu = input(G("[") + R("DracOS") + G("]select>"))
    if menu == "1":
        # Call function
        apache_users()
    elif menu == "2":
        # Call function
        Arachni()
    elif menu == "3":
        # Call function
        BBQSQL()
    elif menu == "4":
        # Call function
        BlindElephant()
    elif menu == "5":
        # Call function
        BurpSuite()
    elif menu == "6":
        # Call function
        CutyCapt()
    elif menu == "7":
        # Call function
        DAVtest()
    elif menu == "8":
        # Call function
        deblaze()
    elif menu == "9":
        # Call function
        DIRB()
    elif menu == "10":
        # Call function
        DirBuster()
    elif menu == "11":
        # Call function
        fimap()
    elif menu == "12":
        # Call function
        FunkLoad()
    elif menu == "13":
        # Call function
        Gobuster()
    elif menu == "14":
        # Call function
        Grabber()
    elif menu == "15":
        # Call function
        hURL()
    elif menu == "16":
        # Call function
        jboss_autopwn()
    elif menu == "17":
        # Call function
        joomscan()
    elif menu == "18":
        # Call function
        jSQL_Injection()
    elif menu == "19":
        # Call function
        Maltego_Teetch()
    elif menu == "20":
        # Call function
        nikto()
    elif menu == "21":
        # Call function
        PadBuster()
    elif menu == "22":
        # Call function
        Paros()
    elif menu == "23":
        # Call function
        Parsero()
    elif menu == "24":
        # Call function
        plecost()
    elif menu == "25":
        # Call function
        Powerfuzzer()
    elif menu == "26":
        # Call function
        ProxyStrike()
    elif menu == "27":
        # Call function
        Recon_ng()
    elif menu == "28":
        # Call function
        Skipfish()
    elif menu == "29":
        # Call function
        sqlmap()
    elif menu == "30":
        # Call function
        sqlninja()
    elif menu == "31":
        # Call function
        sqlsus()
    elif menu == "32":
        # Call function
        ua_tester()
    elif menu == "33":
        # Call function
        Uniscan()
    elif menu == "34":
        # Call function
        w3af()
    elif menu == "35":
        # Call function
        WebScarab()
    elif menu == "36":
        # Call function
        WebShag()
    elif menu == "37":
        # Call function
        WebSlayer()
    elif menu == "38":
        # Call function
        WebSploit()
    elif menu == "39":
        # Call function
        wfuzz()
    elif menu == "40":
        # Call function
        Whatweb()
    elif menu == "41":
        # Call function
        WPScan()
    elif menu == "42":
        # Call function
        XSSer()
    elif menu == "43":
        # Call function
        zaproxy()
    elif menu == "0":
        os.system("python3 /usr/bin/DracOS_VENOMIZER/venomizer.py")  # /usr/bin/
    elif menu == "00":
        exit()
    else:
        print(R('Wrong Input!'))
        input()
        back()







#Function

#apache-users
def apache_users():
    if os.path.isfile("/usr/bin/apache-users"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Apache Users ☣" -geometry 100x30 -e "sudo apt install apache-users"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/apache-users"):
            print(B("Apache Users Already Installed"))
        else:
            print(R("Apache Users Not Installed"))
        input()
        back()
    # end apache-users

#Arachni(nothing)
def Arachni():
    if os.path.isfile("/usr/bin/arachni"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Arachni ☣" -geometry 100x30 -e "sudo apt install arachni"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/arachni"):
            print(B("Arachni Already Installed"))
        else:
            print(R("Arachni Not Installed"))
        input()
        back()
    # end arachni

#BBQSQL
def BBQSQL():
    if os.path.isfile("/usr/bin/bbqsql"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL BBQSQL ☣" -geometry 100x30 -e "sudo apt install bbqsql"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/bbqsql"):
            print(B("BBQSQL Already Installed"))
        else:
            print(R("BBQSQL Not Installed"))
        input()
        back()
    # end bbqsql

#BlindElephant
def BlindElephant():
    if os.path.isfile("/usr/bin/blindelephant"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL BlindElephant ☣" -geometry 100x30 -e "sudo apt install blindelephant"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/blindelephant"):
            print(B("BlindElephant Already Installed"))
        else:
            print(R("BlindElephant Not Installed"))
        input()
        back()
    # end blindelephant

#Burp Suite
def BurpSuite():
    if os.path.isfile("/usr/bin/burpsuite"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Burp Suite ☣" -geometry 100x30 -e "sudo apt install burpsuite"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/burpsuite"):
            print(B("Burp Suite Already Installed"))
        else:
            print(R("Burp Suite Not Installed"))
        input()
        back()
    # end burpsuite

#CutyCapt
def CutyCapt():
    if os.path.isfile("/usr/bin/cutycapt"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL CutyCapt ☣" -geometry 100x30 -e "sudo apt install cutycapt"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/cutycapt"):
            print(B("CutyCapt Already Installed"))
        else:
            print(R("CutyCapt Not Installed"))
        input()
        back()
    # end cutycapt

#DAVtest
def DAVtest():
    if os.path.isfile("/usr/bin/davtest"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL DAVtest ☣" -geometry 100x30 -e "sudo apt install davtest"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/davtest"):
            print(B("DAVtest Already Installed"))
        else:
            print(R("DAVtest Not Installed"))
        input()
        back()
    # end davtest

#deblaze
def deblaze():
    if os.path.isfile("/usr/bin/deblaze"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL deblaze ☣" -geometry 100x30 -e "sudo apt install deblaze"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/deblaze"):
            print(B("deblaze Already Installed"))
        else:
            print(R("deblaze Not Installed"))
        input()
        back()
    # end deblaze

#DIRB
def DIRB():
    if os.path.isfile("/usr/bin/dirb"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL DIRB ☣" -geometry 100x30 -e "sudo apt install dirb"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/dirb"):
            print(B("DIRB Already Installed"))
        else:
            print(R("DIRB Not Installed"))
        input()
        back()
    # end dirb

#DirBuster
def DirBuster():
    if os.path.isfile("/usr/bin/dirbuster"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL DirBuster ☣" -geometry 100x30 -e "sudo apt install dirbuster"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/dirbuster"):
            print(B("DirBuster Already Installed"))
        else:
            print(R("DirBuster Not Installed"))
        input()
        back()
    # end dirbuster

#fimap
def fimap():
    if os.path.isfile("/usr/bin/fimap"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL DirBuster ☣" -geometry 100x30 -e "sudo apt install fimap"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/fimap"):
            print(B("Fimap Already Installed"))
        else:
            print(R("Fimap Not Installed"))
            input()
            back()
    # end fimap

#FunkLoad
def FunkLoad():
    if os.path.isfile("/usr/bin/funkload"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL FunkLoad ☣" -geometry 100x30 -e "sudo apt install funkload"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/funkload"):
            print(B("FunkLoad Already Installed"))
        else:
            print(R("FunkLoad Not Installed"))
        input()
        back()
    # end funkload

#Gobuster
def Gobuster():
    if os.path.isfile("/usr/bin/gobuster"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Gobuster ☣" -geometry 100x30 -e "sudo apt install gobuster"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/gobuster"):
            print(B("Gobuster Already Installed"))
        else:
            print(R("Gobuster Not Installed"))
        input()
        back()
    # end gobuster

#Grabber
def Grabber():
    if os.path.isfile("/usr/bin/grabber"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Grabber ☣" -geometry 100x30 -e "sudo apt install grabber"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/grabber"):
            print(B("Grabber Already Installed"))
        else:
            print(R("Grabber Not Installed"))
        input()
        back()
    # end grabber

#hURL
def hURL():
    if os.path.isfile("/usr/bin/hurl"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL hURL ☣" -geometry 100x30 -e "sudo apt install hurl"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/hurl"):
            print(B("hURL Already Installed"))
        else:
            print(R("hURL Not Installed"))
        input()
        back()
    # end hurl

#jboss-autopwn
def jboss_autopwn():
    if os.path.isfile("/usr/bin/jboss-autopwn"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL jboss-autopwn ☣" -geometry 100x30 -e "sudo apt install jboss-autopwn"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/jboss-autopwn"):
            print(B("jboss-autopwn Already Installed"))
        else:
            print(R("jboss-autopwn Not Installed"))
        input()
        back()
    # end jboss-autopwn

#joomscan
def joomscan():
    if os.path.isfile("/usr/bin/joomscan"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL joomscan ☣" -geometry 100x30 -e "sudo apt install joomscan"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/joomscan"):
            print(B("joomscan Already Installed"))
        else:
            print(R("joomscan Not Installed"))
        input()
        back()
    # end joomscan
#jSQL-Injection
def jSQL_Injection():
    if os.path.isfile("/usr/bin/jSQL"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL jSQL ☣" -geometry 100x30 -e "sudo apt install jsql"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/jSQL"):
            print(B("jSQL Already Installed"))
        else:
            print(R("jSQL Not Installed"))
        input()
        back()
    # end jSQL-Injection

#Maltego Teetch
def Maltego_Teetch():
    if os.path.isfile("/usr/bin/maltego-teeth"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Maltego Teetch ☣" -geometry 100x30 -e "sudo apt install maltego-teeth"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/maltego-teeth"):
            print(B("Maltego Teetch Already Installed"))
        else:
            print(R("Maltego Teetch Not Installed"))
        input()
        back()
    # end maltego-teetch

#Nikto
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
            print(R("Nikto Not Installed"))
        input()
        back()
    # end nikto

#PadBuster
def PadBuster():
    if os.path.isfile("/usr/bin/padbuster"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL PadBuster ☣" -geometry 100x30 -e "sudo apt install padbuster"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/padbuster"):
            print(B("PadBuster Already Installed"))
        else:
            print(R("PadBuster Not Installed"))
        input()
        back()
    # end padbuster

#Paros
def Paros():
    if os.path.isfile("/usr/bin/paros"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Paros ☣" -geometry 100x30 -e "sudo apt install paros"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/paros"):
            print(B("Paros Already Installed"))
        else:
            print(R("Paros Not Installed"))
        input()
        back()
    # end paros

#Parsero
def Parsero():
    if os.path.isfile("/usr/bin/parsero"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Parsero ☣" -geometry 100x30 -e "sudo apt install parsero"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/parsero"):
            print(B("Parsero Already Installed"))
        else:
            print(R("Parsero Not Installed"))
        input()
        back()
    # end parsero

#plecost
def plecost():
    if os.path.isfile("/usr/bin/plecost"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL plecost ☣" -geometry 100x30 -e "sudo apt install plecost"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/plecost"):
            print(B("plecost Already Installed"))
        else:
            print(R("plecost Not Installed"))
        input()
        back()
    # end plecost

#Powerfuzzer
def Powerfuzzer():
    if os.path.isfile("/usr/bin/powerfuzzer"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Powerfuzzer ☣" -geometry 100x30 -e "sudo apt install powerfuzzer"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/powerfuzzer"):
            print(B("Powerfuzzer Already Installed"))
        else:
            print(R("Powerfuzzer Not Installed"))
        input()
        back()
    # end powerfuzzer

#ProxyStrike
def ProxyStrike():
    if os.path.isfile("/usr/bin/proxystrike"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL ProxyStrike ☣" -geometry 100x30 -e "sudo apt install proxystrike"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/proxystrike"):
            print(B("ProxyStrike Already Installed"))
        else:
            print(R("ProxyStrike Not Installed"))
        input()
        back()
    # end proxystrike

#Recon-ng
def Recon_ng():
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
            print(R("Recon-ng Not Installed"))
        input()
        back()
    # end recon-ng

#Skipfish
def Skipfish():
    if os.path.isfile("/usr/bin/skipfish"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Skipfish ☣" -geometry 100x30 -e "sudo apt install skipfish"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/skipfish"):
            print(B("Skipfish Already Installed"))
        else:
            print(R("Skipfish Not Installed"))
        input()
        back()
    # end skipfish

#sqlmap
def sqlmap():
    if os.path.isfile("/usr/bin/sqlmap"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL sqlmap ☣" -geometry 100x30 -e "sudo apt install sqlmap"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/sqlmap"):
            print(B("sqlmap Already Installed"))
        else:
            print(R("sqlmap Not Installed"))
        input()
        back()
    # end sqlmap

#sqlninja
def sqlninja():
    if os.path.isfile("/usr/bin/sqlninja"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL sqlninja ☣" -geometry 100x30 -e "sudo apt install sqlninja"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/sqlninja"):
            print(B("sqlninja Already Installed"))
        else:
            print(R("sqlninja Not Installed"))
        input()
        back()
    # end sqlninja

#sqlsus
def sqlsus():
    if os.path.isfile("/usr/bin/sqlsus"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL sqlsus ☣" -geometry 100x30 -e "sudo apt install sqlsus"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/sqlsus"):
            print(B("sqlsus Already Installed"))
        else:
            print(R("sqlsus Not Installed"))
        input()
        back()
    # end sqlsus

#ua-tester
def ua_tester():
    if os.path.isfile("/usr/bin/ua-tester"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL ua-tester ☣" -geometry 100x30 -e "sudo apt install ua-tester"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/ua-tester"):
            print(B("ua-tester Already Installed"))
        else:
            print(R("ua-tester Not Installed"))
        input()
        back()
    # end ua-tester

#Uniscan
def Uniscan():
    if os.path.isfile("/usr/bin/uniscan"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Uniscan ☣" -geometry 100x30 -e "sudo apt install uniscan"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/uniscan"):
            print(B("Uniscan Already Installed"))
        else:
            print(R("Uniscan Not Installed"))
        input()
        back()
    # end uniscan

#w3af
def w3af():
    if os.path.isfile("/usr/bin/w3af"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL w3af ☣" -geometry 100x30 -e "sudo apt install w3af"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/w3af"):
            print(B("w3af Already Installed"))
        else:
            print(R("w3af Not Installed"))
        input()
        back()
    # end w3af

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

#WebShag
def WebShag():
    if os.path.isfile("/usr/bin/webshag"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL WebShag ☣" -geometry 100x30 -e "sudo apt install webshag"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/webshag"):
            print(B("WebShag Already Installed"))
        else:
            print(R("WebShag Not Installed"))
        input()
        back()
    # end WebShag

#WebSlayer
def WebSlayer():
    if os.path.isfile("/usr/bin/webslayer"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL WebSlayer ☣" -geometry 100x30 -e "sudo apt install webslayer"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/webslayer"):
            print(B("WebSlayer Already Installed"))
        else:
            print(R("WebSlayer Not Installed"))
        input()
        back()
    # end WebSlayer

#WebSploit
def WebSploit():
    if os.path.isfile("/usr/bin/websploit"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL WebSploit ☣" -geometry 100x30 -e "sudo apt install websploit"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/websploit"):
            print(B("WebSploit Already Installed"))
        else:
            print(R("WebSploit Not Installed"))
        input()
        back()
    # end WebSploit

#wfuzz
def wfuzz():
    if os.path.isfile("/usr/bin/wfuzz"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL wfuzz ☣" -geometry 100x30 -e "sudo apt install wfuzz"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/wfuzz"):
            print(B("wfuzz Already Installed"))
        else:
            print(R("wfuzz Not Installed"))
        input()
        back()
    # end wfuzz

#Whatweb
def Whatweb():
    if os.path.isfile("/usr/bin/whatweb"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL Whatweb ☣" -geometry 100x30 -e "sudo apt install whatweb"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/whatweb"):
            print(B("Whatweb Already Installed"))
        else:
            print(R("Whatweb Not Installed"))
        input()
        back()
    # end Whatweb

#WPScan
def WPScan():
    if os.path.isfile("/usr/bin/wpscan"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL WPScan ☣" -geometry 100x30 -e "sudo apt install wpscan"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/wpscan"):
            print(B("WPScan Already Installed"))
        else:
            print(R("WPScan Not Installed"))
        input()
        back()
    # end WPScan

#XSSer
def XSSer():
    if os.path.isfile("/usr/bin/xsser"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            'xterm -T "☣ INSTALL XSSer ☣" -geometry 100x30 -e "sudo apt install xsser"'
        )
        os.system("clear")
        if os.path.isfile("/usr/bin/xsser"):
            print(B("XSSer Already Installed"))
        else:
            print(R("XSSer Not Installed"))
        input()
        back()
    # end XSSer

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

def back():
    WebApp()