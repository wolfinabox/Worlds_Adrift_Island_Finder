# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 305)
        MainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.install_folder_label = QtWidgets.QLabel(self.centralwidget)
        self.install_folder_label.setAlignment(QtCore.Qt.AlignCenter)
        self.install_folder_label.setObjectName("install_folder_label")
        self.gridLayout.addWidget(self.install_folder_label, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 2)
        self.island_id_box = QtWidgets.QLineEdit(self.centralwidget)
        self.island_id_box.setEnabled(False)
        self.island_id_box.setObjectName("island_id_box")
        self.gridLayout.addWidget(self.island_id_box, 5, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 2)
        self.dir_label = QtWidgets.QLabel(self.centralwidget)
        self.dir_label.setText("")
        self.dir_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dir_label.setObjectName("dir_label")
        self.gridLayout.addWidget(self.dir_label, 2, 0, 1, 2)
        self.browse_button = QtWidgets.QPushButton(self.centralwidget)
        self.browse_button.setToolTip("")
        self.browse_button.setObjectName("browse_button")
        self.gridLayout.addWidget(self.browse_button, 1, 1, 1, 1)
        self.folder_text_box = QtWidgets.QLineEdit(self.centralwidget)
        self.folder_text_box.setObjectName("folder_text_box")
        self.gridLayout.addWidget(self.folder_text_box, 1, 0, 1, 1)
        self.in_game_label = QtWidgets.QLabel(self.centralwidget)
        self.in_game_label.setEnabled(True)
        self.in_game_label.setText("")
        self.in_game_label.setAlignment(QtCore.Qt.AlignCenter)
        self.in_game_label.setObjectName("in_game_label")
        self.gridLayout.addWidget(self.in_game_label, 6, 0, 1, 2)
        self.island_id_label = QtWidgets.QLabel(self.centralwidget)
        self.island_id_label.setEnabled(False)
        self.island_id_label.setAlignment(QtCore.Qt.AlignCenter)
        self.island_id_label.setObjectName("island_id_label")
        self.gridLayout.addWidget(self.island_id_label, 4, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Worlds Adrift Island Finder, by wolfinabox"))
        self.install_folder_label.setText(_translate("MainWindow", "Worlds Adrift Install Folder"))
        self.island_id_box.setStatusTip(_translate("MainWindow", "Island ID/Steam Workshop Link"))
        self.dir_label.setStatusTip(_translate("MainWindow", "Game directory status"))
        self.browse_button.setStatusTip(_translate("MainWindow", "Choose the Worlds Adrift install directory..."))
        self.browse_button.setText(_translate("MainWindow", "Browse..."))
        self.folder_text_box.setStatusTip(_translate("MainWindow", "Worlds Adrift install directory"))
        self.in_game_label.setStatusTip(_translate("MainWindow", "In-game Status"))
        self.island_id_label.setText(_translate("MainWindow", "Island ID/Steam Workshop Link"))

