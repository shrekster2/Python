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
print('WINE is good to install too!')
