#========================================================#
# Worlds Adrift Island Finder
# by wolfinabox
#========================================================#
import winreg #To get the game's install location from the Windows Registry
import glob #To find files matching the island name
import os #To access files
from colorama import init,Fore,Back,Style #For fancy colors
init(autoreset=True)

def is_int(s:str)->bool:
    try: 
        int(s)
        return True
    except ValueError:
        return False

#Colors
good=Style.BRIGHT+Fore.GREEN
warn=Style.BRIGHT+Fore.YELLOW
error=Style.BRIGHT+Fore.RED

wa_install_path=''
#Try to Get Worlds Adrift Install Location from the Windows Registry
try:
    wa_reg_key=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Steam App 322780')
    wa_install_path=winreg.QueryValueEx(wa_reg_key,'InstallLocation')[0]
except FileNotFoundError:
    print(error+'Couldn\'t get Worlds Adrift\'s install location from the registry.'+Fore.RESET+'\nPlease input manually (should end something like "SteamLibrary\steamapps\common\WorldsAdrift)"')
    wa_install_path=input('> ')

if not os.path.isdir(wa_install_path):
    print(error+'"'+wa_install_path+'" is an invalid directory.')
    input('Press return to exit...')

print('Worlds Adrift Install Path: "'+wa_install_path+'"')
islands_path=os.path.join(os.path.join(wa_install_path,'Assets'),'unity')
os.chdir(islands_path)


#Get Island Number
island_num=input('Island number: ').strip()
island_num=island_num.split('?id=')[1] if len(island_num.split('?id='))>1 else island_num.split('?id=')[0]
if not is_int(island_num):
    print(error+'Invalid island number "'+island_num+'"')
    input('Press return to exit...')

island=''
for f in glob.glob(island_num+'@island_unityclient'):
    island=f
print(good+'Island "'+island_num+'" is in game!' if island else warn+'Island "'+island_num+'" is not currently in game.')
input('Press return to exit...')