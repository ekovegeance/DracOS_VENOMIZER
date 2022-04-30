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
    lists = ('apache-users','arachni','bbqsql','blindelephant','burpsuite','cutycapt','davtest','deblaze',
    'dirb','dirbuster','fimap','funkload','gobuster','grabber','hurl','jboss-autopwn','joomscan','jsql',
    'maltego-teeth','nikto','padbuster','paros','parsero','plecost','powerfuzzer','proxystrike','recon-ng',
    'skipfish','sqlmap','sqlninja','sqlsus','ua-tester','uniscan','w3af','webscarab','webshag','webslayer',
    'websploit','wfuzz','whatweb','wpscan','xsser')
    menu = int(input(G("[") + R("DracOS") + G("]select>")))
    if menu:
        menu = int(menu)-1
        # Call function
        webApp_tool(lists[name])
    elif menu == 0:
        os.system(f"python3 /usr/bin/DracOS_VENOMIZER/venomizer.py")  # /usr/bin/
    elif menu == 00:
        exit()
    else:
        print(R('Wrong Input!'))
        input()
    back()

#Function
def webApp_tool(a):
    if os.path.isfile(f'/usr/bin/{a}'):
        os.system('clear')
        print(B('tools Available'))
        # input()
        # back()
    else:
        os.system(
            f'xterm - T "install {a}" -geometry 100x30 -e "sudo apt install {a}"'
        )
        os.system('clear')
        if os.path.isfile(f'/usr/bin/{a}'):
            print(B(f'{a} already installed'))
        else:
            print(B(f'{a} users not installed'))
    input()
    back()



def back():
    WebApp()