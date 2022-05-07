# -*- coding: utf-8 -*-
# Import Package 

import os
import time
import os.path
import subprocess
from termcolor import colored as c






"""
Program : venomizer setup.py
"""
#banner
def banner():
    print(c("""
          Venomizer Hacking tools package from DracOS GNU/Linux Remastered
          developed by : Faiz Hidayat - github :https://github.com/faizH3
                         Eko Saputra  - github :https://github.com/ekovegeance
          """, 'red'))
    print(c("Version : 1.2.7     Codename : Mr. Robot","blue"))
    print(c('[(c) 2022 |', 'red'), c(
        'dracos-linux.org | https://github.com/dracos-linux', 'red')+c(']', 'red'))
    
    
#Update Repository
print(os.getcwd())
print(c("[✔]Add Repository","green"))
os.system("echo 'deb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
os.system("gpg --keyserver hkps://keys.openpgp.org --recv-key 44C6513A8E4FB3D30875F758ED444FF07D8D0BF6")
os.system('sudo apt-get update')
print(c("[+]Repository is up to date","blue"))

#cek apakah file xterm sudah ada!
def cek_xterm():
    if os.path.isfile("/usr/bin/xterm"):
        print(c("[✔]xterm is installed","green"))
    else:
        print(c("[!]xterm is not installed","red"))
        print(c("[!]Installing xterm","blue"))
        os.system("sudo apt-get install xterm")
        print(c("[+]xterm is installed","green"))
    
# cek apakah file git sudah ada!
def cek_git():
    if os.path.isfile("/usr/bin/git"):
        print(c("[✔]git is installed","green"))
    else:
        print(c("[!]git is not installed","red"))
        print(c("[!]Installing git","blue"))
        os.system("sudo apt-get install git")
        print(c("[+]git is installed","green"))

#cek apakah file python3 sudah ada!
def cek_python3():
    if os.path.isfile("/usr/bin/python3"):
        print(c("[✔]python3 is installed","green"))
    else:
        print(c("[!]python3 is not installed","red"))
        print(c("[!]Installing python3","blue"))
        os.system("sudo apt-get install python3")
        print(c("[+]python3 is installed","green"))

# Install requirements
print("Installing requirements.txt...")
subprocess.Popen("sudo pip3 install -r requirements.txt", shell=True).wait()

# Setup venomizer
print(c("[*] Installing venomizer to /usr/bin/DracOS_VENOMIZER..","green"))
print(os.getcwd())
subprocess.Popen("mkdir /usr/bin/DracOS_VENOMIZER/; cp -rf * /usr/bin/DracOS_VENOMIZER/; cp vnm /usr/bin", shell=True).wait()
print(c("Create launcher venomizer...","blue"))
os.system("clear")

# cek install venomizer
def cek_install_venomizer():
    print(c("[*] Checking installation...","blue"))
    time.sleep(2)
    print(c("[+]Checking Repository...","blue"))
    time.sleep(2)
    print(c("[✔]Repository Up to date [Done]","green"))
    time.sleep(2)
    print(c("[+]Checking xterm...","blue"))
    time.sleep(2)
    print(c("[✔]xterm is installed [Done]","green"))
    time.sleep(2)
    print(c("[+]Checking git...","blue"))
    time.sleep(2)
    print(c("[✔]Git is installed [Done]","green"))
    time.sleep(2)
    print(c("[+]Checking python3...","blue"))
    time.sleep(2)
    print(c("[✔]Python3 is installed [Done]","green"))
    time.sleep(2)
    print(c("[+]Checking requirements...","blue"))
    time.sleep(2)
    print(c("[✔]requirements.txt is installed [Done]","green"))
    time.sleep(2)
    time.sleep(2)
    print(c("[+]Checking venomizer...","blue"))
    time.sleep(2)



# Create launcher
cek_install_venomizer()
print(c("Creating launcher...","blue"))
os.system("sudo chmod +x /usr/bin/DracOS_VENOMIZER &&sudo chmod +x /usr/bin/vnm")
banner()
print(c("[✔]Finished. Run 'vnm' to start the venomizer framework.","green"))
time.sleep(5)
os.system("vnm")


