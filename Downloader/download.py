import os
print('Installing Lutris')
os.system("sudo add-apt-repository ppa:lutris-team/lutris")
os.system("sudo apt-get update")
os.system("sudo apt-get install lutris")
print('Installing kdenlive')
os.system("sudo apt-get install kdenlive")
print('Installing Steam')
os.system("sudo apt install steam-installer")
print('Installing Discord')
os.system("sudo apt-get install snapd")
os.system("sudo snap install discord")
print("Installing OBS")
os.system("sudo add-apt-repository ppa:obsproject/obs-studio")
os.system("sudo apt update")
os.system("sudo apt install obs-studio")
print("Installing Filezilla")
os.system("sudo apt-get install filezilla")


print("Installing wine, this may take a while")
os.system("sudo dpkg --add-architecture i386")
os.system("wget -O - https://dl.winehq.org/wine-builds/winehq.key | sudo apt-key add -")
print("16 = ubuntu 16.04, 18 = ubuntu 18.04, 19 = ubuntu 19.10, 20 = ubuntu 20.04")
C = input("Which one do you have: ")
if C == "16":
    os.system("sudo add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ xenial main' ")
if C == "18":
    print('Dont need a Repo!')
if C == "19":
    os.system("sudo add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main' ")
if C == "20":
    os.system("sudo add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ focal main' ")

os.system("sudo apt update")

D = input("Do you want stable = stable, stag = staging or d = developement")
if D == "stable":
    os.system("sudo apt install --install-recommends winehq-stable")
if D == "stag":
    os.system("sudo apt install --install-recommends winehq-staging")
if D == "d":
    os.system("sudo apt install --install-recommends winehq-devel")

os.system("sudo apt-get update")
print("installed everything!")
