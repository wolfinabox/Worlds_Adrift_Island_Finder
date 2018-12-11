#========================================================#
# Worlds Adrift Island Finder
# by wolfinabox
#========================================================#
#Imports=================================================#
import winreg #To get the game's install location from the Windows Registry
import glob #To find files matching the island name
import os #To access files
import sys
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QFileDialog
from main_ui import *
#========================================================#
#Functions===============================================#
def is_int(s:str)->bool:
    try: 
        int(s)
        return True
    except ValueError:
        return False

def get_install_from_reg():
    try:
        wa_reg_key=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Steam App 322780')
        wa_install_path=winreg.QueryValueEx(wa_reg_key,'InstallLocation')[0]
        return wa_install_path
    except FileNotFoundError:
        return ''
#========================================================#
#Main Code===============================================#
class Island_Finder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.browse_button.clicked.connect(self.on_browse_clicked)
        self.ui.folder_text_box.textChanged.connect(self.validate_dir)
        self.ui.folder_text_box.setText(get_install_from_reg())
        self.ui.island_id_box.textChanged.connect(self.find_island)

    def validate_dir(self,s:str):
        islands_path=os.path.join(s,os.path.join('Assets','unity'))
        if not s:
            self.ui.dir_label.setText('')
        elif os.path.isdir(islands_path):
            self.ui.dir_label.setStyleSheet('color: green;')
            self.ui.dir_label.setText('Path exists, and islands folder found!')
            self.ui.island_id_box.setEnabled(True)
            self.ui.in_game_label.setEnabled(True)
            self.ui.island_id_label.setEnabled(True)
            os.chdir(islands_path)
            return
        elif os.path.isdir(s):
            self.ui.dir_label.setStyleSheet('color: red;')
            self.ui.dir_label.setText('Path "'+s+'" exists, but islands folder not found.')

        else:
            self.ui.dir_label.setStyleSheet('color: red;')
            self.ui.dir_label.setText('Path "'+s+'" does not exist!')
        self.ui.island_id_box.setEnabled(False)
        self.ui.in_game_label.setEnabled(False)
        self.ui.island_id_label.setEnabled(False)

        
    def on_browse_clicked(self):
        path=QFileDialog.getExistingDirectory(self,'Choose Directory...',(
        self.ui.folder_text_box.text() if self.ui.folder_text_box.text() else 'C:\\'),QFileDialog.ShowDirsOnly)
        self.ui.folder_text_box.setText(path)

    def find_island(self,s:str):
        island_id=s.split('?id=')[1] if len(s.split('?id='))>1 else s.split('?id=')[0]
        if not island_id:
            self.ui.in_game_label.setText('')
            return
        elif not is_int(island_id):
            self.ui.in_game_label.setStyleSheet('color: red;')
            self.ui.in_game_label.setText('Invalid Island ID "'+island_id+'"')
            return
        island=''
        #"Iterate" through files matching the island number (should just be 1 or 0 matches)
        for f in glob.glob(island_id+'@island_unityclient'):
            island=f
        if island:
            self.ui.in_game_label.setStyleSheet('color: green;')
            self.ui.in_game_label.setText('Island "'+island_id+'" is in game!')
        else:
            self.ui.in_game_label.setStyleSheet('color: orange;')
            self.ui.in_game_label.setText('Island "'+island_id+'" is not yet in game!')


    def event(self, e):
        if e.type() == QtCore.QEvent.StatusTip:
            if e.tip() == '':
                e = QtGui.QStatusTipEvent('https://github.com/wolfinabox/Worlds_Adrift_Island_Finder')  # Set this to whatever you like
        return super().event(e)
#========================================================#
if __name__ == '__main__':
    #Run    
    app = QApplication(sys.argv)
    ex = Island_Finder()
    sys.exit(app.exec_())