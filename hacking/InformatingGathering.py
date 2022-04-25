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
    32. Miranda(Not Found)
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

    lists = ('nmap','amap','whatweb','sublist3r','arp-scan','automater','braa','casefile','cisco-torch',
    'dmitry','dnsenum','dnsmap','dnsrecon','dnstracer','dnswalk','python-faraday','fierce','firewalk',
    'fragroute','fragrouter','ghost-phisher','goofile','hping3','inspy','intrace','ismtp','maltego-teeth',
    'masscan','metagoofil','miranda','nikto','ntop','recon-ng','smbmap','smtp-user-enum','snmp-check','sslcaudit','sslsplit')

    menu = int(input(G("[") + R("DracOS") + G("]select>")))
    if menu:
        menu -= 1
        # Call function
        info_gathering(lists[menu])
    elif menu == 0:
        os.system(f"python3 {os.getcwd()}/venomizer.py")  # /usr/bin/
    elif menu == 00:
        exit()
 
    else:
        print(R('Wrong Input!'))
        input()
        back()


# tambah fungsi tools lalu panggil ke dalam fungsi InfoGat
# info_gathering
def info_gathering(a):
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
            print(R(f"Error Installing {a}"))
        input()
        back()
        # end info_gathering

# fungsi untuk memanggil lagi InfoGat
# supaya program tidak keluar
def back():
    os.system('clear')
    InfoGat()
# Looping
# while True:
#     InfoGat()
