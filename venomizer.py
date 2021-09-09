#! usr/share/bin/python3
from termcolor import colored as c
import sys
import Logo
import hack, eksploit #, InformatingGathering #, VulnerabilityAssesment, webAttack, dll
import os.path
import os
from install import install


if os.path.isfile('/usr/bin/git'):
    print()
else:
    os.system('sudo apt install git')


# logo 
def LOGO():
    os.system("clear")
    print(c("        -os:",'red'))
    print("            "+c("-os/`", 'red'))
    print("            "+c("  :s", 'red')+c("y+-`",'red'))
    print("            "+c("   `/y", 'red')+c("yyy+.",'red'))
    print("            "+c("     `+y", 'red')+c("yyyo-",'red'))
    print("            "+c("       `/y", 'red')+c("yyys:",'red'))
    print(c("`:osssoo",'red')+c("oo++-",'red'),c("        +y", 'red')+c("yyyyy/`",'red'))
    print(c("   ./yyyy",'red')+c("yyo ",'red'),c("        yo`", 'red')+c(":syyyy+.",'red'))
    print(c("      -oyy",'red')+c("y+ ",'red')+c("        +-   :y", 'red')+c("yyyyo-",'red'))
    print(c("        `:s",'red')+c("y:",'red')+c("        `.    `/y", 'red')+c("yyyys:",'red'))
    print(c("           .",'red')+c("/o')+/.`",'red')+c("           .oyy", 'red')+c("so+oo:`",'red'))
    print(c("              :+oo+//::::///:-.`",'red')+c("     `.`",'red'))
    print(c('=================================================================', 'green'))
    print("__      _______ __   __  _____  ___  ___ _____ ___________ _____   ")
    print("\ \    / / ____|  \  | |/ ___ \|   \/   |_   _|___  |  ___| __   \ ")
    print(" \ \  / /| |__ |   \ | | |   | | |\  /| | | |    / /| |__ | |__) / ")
    print("  \ \/ / |  __|| |\ \| | |   | | | \/ | | | |   / / |  __||  _  /  ")
    print("   \  /  | |___| | \   | |___| | |    | |_| |_ / /__| |___| | \ \  ") 
    print("    \/   |_____|_|  \__|\_____/|_|    |_|_____/_____|_____|_|  \_\ ")
    print(c('[(c) 2018 |', 'red'), c('dracos-linux.org | https://github.com/DracOS-Remaster', 'red')+c(']', 'red'))


# def LOGO_hacking():
#     os.system('clear')
#     print(c('[','green')+c('GROUP', 'red')+c(']','green'))
#     print(c('____   ____     _____      _______  ___  _______ __    ___________   ','red'))
#     print(c('|   |  |   |   /  _   \   /  ___  /|  | / |_   _|  \  |  |   _____ \ ','red'))
#     print(c('|   |__|   |  /  /__\  \ |  |   |  |  |/  / | | |   \ |  |  /   ___  ','red'))
#     print(c('|    __    | /   ____   \|  |   |  |     x  | | |    \|  |  |  |_  \ ','red'))
#     print(c('|   |  |   |/   /    \   \   \__---|  |\  \_| |_|  |\    |   \__|  | ','red'))
#     print(c('|___|  |___|___/      \___\_______/|__| \__\____|__| \__ |\______  / ','red'))

global DracOS
DracOS = c('[','green')+c('DracOS','red')+c(']> ','green')

def menu():
    # call logo
    os.system('clear')
    LOGO()
    print(c('0. sudo apt update', 'green'))
    print(c('1. sudo apt upgrade', 'green'))
    print(c('2. Install', 'green'))
    print(c('3. Check Update Tools', 'green'))
    print(c('4. Hacking', 'green'))
    print(c('5. Informating gathering', 'green'))
    print(c('6. Vulnerability Assessment', 'green'))
    print(c('7. Web Attack', 'green'))
    print(c('8. Exploitation Testing', 'green'))
    print(c('9. Privilege Escalation', 'green'))
    print(c('10. Password Attack', 'green'))
    print(c('11. Social Engineering', 'green'))
    print(c('12. Man In The Middle attack', 'green'))
    print(c('13. Stress Testing', 'green'))
    print(c('14. Wireless Attack', 'green'))
    print(c('15. Maintining Access', 'green'))
    print(c('16. Forensic Tools', 'green'))
    print(c('17. Reverse Engineering', 'green'))
    print(c('18. Malware Analysis', 'green'))
    print(c('19. Covering Track', 'green'))
    print(c('00. exit'))
    menu = input(DracOS)
    if menu == '0':
        var = input('sudo apt update(y/n)? ')
        if var == 'y': 
                os.system('sudo apt update')
                # os.system('clear')
        else:
            # os.system('clear')
            back()
    elif menu == '1':
        var = input('sudo apt upgrade(y/n)? ')
        if var == 'y':
            os.system('sudo apt upgrade')
            # os.system('clear')
        else:
            # os.system('clear')
            back()
    elif menu == '2':
        install()
    # elif menu == '3':
    #     check_update_tools()
    elif menu == '4':
        hack.hacking()
    elif menu == '5':
        os.system('python3 $HOME/git/DracOS_VENOMIZER/InformatingGathering.py')
    #     InformatingGathering.InfoGat()
    # elif menu == '6':
    #     VulnerabilityAssessment()
    # elif menu == '7':
    #     WebAttack()
    # elif menu == '8':
    #     ExploitationTesting()
    # # elif menu == '9':
    #     PrivilegeEscalation()
    # elif menu == '10':
    #     PasswordAttack()
    # elif menu == '11':
    #     SocialEngineering()
    # elif menu == '12':
    #     ManInTheMiddleAttack()
    # elif menu == '13':
    #     StressTesting()
    # elif menu == '14':
    #     WirelessAttack()
    # elif menu == '15':
    #     MaintiningAcces()
    # elif menu == '16':
    #     ForensicTools()
    # elif menu == '17':
    #     ReverseEngineering()
    # elif menu == '18':
    #     MalwareAnalysis()
    # elif menu == '19':
    #     CoveringTrack()
    elif menu == '00':
        os.system('exit')
        sys.exit()
        exit()
    elif menu == 'clear':
        os.system('clear')
        back()


def back():
    menu()


while menu():
    menu()
# if __name__ == "__main__":
# 	os.system("clear")
# 	menu()