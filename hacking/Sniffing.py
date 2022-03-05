
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
    lists = ('bettercap','brup','dnschef','fiked','hamster-sidejack','hexinject','iaxflood','inviteflood','ismtp',
    'isr-evilgrade','mitmproxy','ohrwurm','protos-sip','rebind','responder','rtpbreak','rtpinsertsound','sctpscan',
    'siparmyknife','sipp','sipvicious','sniffjoke','sslsplit','thc-ipv6','voiphopper','webscarab','wifi-honey','wireshark',
    'xspy','yersinia','zaproxy')
    menu = int(input(G("[") + R("DracOS") + G("]select>")))
    if menu == "1":
        # Call function
        sniffing_tool(lists[menu])
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
#sniffing tool
def sniffing_tool(a):
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
    # end sniffing tool
