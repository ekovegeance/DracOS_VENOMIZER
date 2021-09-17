import os
from color import*
import Logo

def WebApps():
    os.system('clear')
    # Logo
    print(""" 
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
    0. back """)
    print(R('00. exit'))
    
    menu = input(G('[')+R('DracOS')+G(']select> '))

    if menu == '1':
        print()
    # elif menu == '2':
    # elif menu == '3':
    # elif menu == '4':
    # elif menu == '5':
    # elif menu == '6':
    # elif menu == '7':
    # elif menu == '8':
    # elif menu == '9':
    # elif menu == '10':
    # elif menu == '11':
    # elif menu == '12':
    # elif menu == '13':
    # elif menu == '14':
    # elif menu == '15':
    # elif menu == '16':
    # elif menu == '17':
    # elif menu == '18':
    # elif menu == '19':
    # elif menu == '20':
    # elif menu == '21':
    # elif menu == '22':
    # elif menu == '23':
    # elif menu == '24':
    # elif menu == '25':
    # elif menu == '26':
    # elif menu == '27':
    # elif menu == '28':
    # elif menu == '29':
    # elif menu == '30':
    # elif menu == '31':
    # elif menu == '32':
    # elif menu == '33':
    # elif menu == '34':
    # elif menu == '35':
    # elif menu == '36':
    # elif menu == '37':
    # elif menu == '38':
    # elif menu == '39':
    # elif menu == '40':
    # elif menu == '41':
    # elif menu == '42':
    # elif menu == '43':

    elif menu == '0':
        os.system('python3 $HOME/git/DracOS_VENOMIZER/venomizer.py')
    elif menu == '00':
        exit()



def back():
    WebApps()

