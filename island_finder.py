#========================================================#
# Worlds Adrift Island Finder
# by wolfinabox
#========================================================#
#Imports=================================================#
import winreg #To get the game's install location from the Windows Registry
import glob #To find files matching the island name
import os #To access files
from colorama import init,Fore,Back,Style #For fancy colors
init(autoreset=True)
#========================================================#

#Globals=================================================#
#Colors
HEADER_COLOR=Style.BRIGHT+Fore.CYAN
GOOD_COLOR=Style.BRIGHT+Fore.GREEN
WARN_COLOR=Style.BRIGHT+Fore.YELLOW
ERROR_COLOR=Style.BRIGHT+Fore.RED
#========================================================#

#Functions===============================================#
def is_int(s:str)->bool:
    try: 
        int(s)
        return True
    except ValueError:
        return False
#========================================================#

#Main Code===============================================#
print(HEADER_COLOR+'"Is my island in the game?" Let\'s find out!')
wa_install_path=''
#Try to Get Worlds Adrift Install Location from the Windows Registry
try:
    wa_reg_key=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Steam App 322780')
    wa_install_path=winreg.QueryValueEx(wa_reg_key,'InstallLocation')[0]
except FileNotFoundError:
    #Get it from the user instead
    print(ERROR_COLOR+'Couldn\'t get Worlds Adrift\'s install location from the registry.'+Fore.RESET+'\nPlease input manually (should end something like "SteamLibrary\steamapps\common\WorldsAdrift)"')
    wa_install_path=input('> ')

#Path doesn't exist
if not os.path.isdir(wa_install_path):
    print(ERROR_COLOR+'"'+wa_install_path+'" is an invalid directory.')
    input('Press return to exit...')
    exit()

print('Worlds Adrift Install Path: "'+wa_install_path+'"')
islands_path=os.path.join(os.path.join(wa_install_path,'Assets'),'unity')

#Islands directory path doesn't exist
if not os.path.isdir(islands_path):
    print(ERROR_COLOR+'Could not find Assets/unity folder. Please make sure that the game path above is correct.')
    input('Press return to exit...')
    exit()
os.chdir(islands_path)

#Get Island Number
island_num=input('Island number: ').strip()
island_num=island_num.split('?id=')[1] if len(island_num.split('?id='))>1 else island_num.split('?id=')[0]

#User didn't enter something valid for the island number
if not is_int(island_num):
    print(ERROR_COLOR+'Invalid island number "'+island_num+'"')
    input('Press return to exit...')
    exit()

island=''
#"Iterate" through files matching the island number (should just be 1 or 0 matches)
for f in glob.glob(island_num+'@island_unityclient'):
    island=f
print(GOOD_COLOR+'Island "'+island_num+'" is in game!' if island else WARN_COLOR+'Island "'+island_num+'" is not currently in game.')
input('Press return to exit...')
#========================================================#
