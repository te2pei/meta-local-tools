#!/usr/bin/env pythona
# -*- coding: utf-8 -*-

keycode_buttons = {
    59  : 'SOFT-L', # 'KEY_F1'
    60  : 'SOFT-R', # 'KEY_F2'
    65  : 'ENTER' , # 'KEY_F7'
    66  : '←'     , # 'KEY_F8'
    67  : 'POWER' , # 'KEY_F9'
    68  : '↑'     , # 'KEY_F10'
    87  : '→'     , # 'KEY_F11'
    88  : '↓'     , # 'KEY_F12'
    119 : 'PAUSE' , # 'KEY_PAUSE',
    240 : ''      , # 'KEY_UNKNOWN',
}

import sys
import subprocess
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout 

class ControlPanelWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.move(300, 300)
        self.setWindowTitle('Control Panel')
        self.grid = QGridLayout()

        names = ['POWER' , 'RETURN', ''  , '↑', '' ,
                 'SOFT-L', 'SOFT-R', '←' , '' , '→',
                 'LINE'  , 'ENTER' , ''  , '↓', ''
                ]

        positions = [(y,x) for y in range(3) for x in range(5)]

        for position, name in zip(positions, names):
            if name == '':
                    continue

            self.button = QPushButton(name)
            self.button.setAutoRepeat(True)
            self.button.setAutoRepeatDelay(1000)    # 1sec
            self.button.setAutoRepeatInterval(300)  # 300msec
            self.button.clicked.connect(self.buttonClick)
            self.button.clicked.connect(self.buttonRelease)
            self.grid.addWidget(self.button, *position)

        # レイアウト配置
        self.setLayout(self.grid)

        # 表示
        self.show()

    def buttonClick(self): 

        btn = self.sender()
        print( btn.text() )

        self.p = QProcess(self)
        self.p.finished.connect(self.process_finished)
        res = subprocess.call("/usr/local/bin/hardkey > /dev/input/event1", shell=True)
        print(res)

    def buttonRelease(self): 
        print("released")

    def process_finished(self):
        print("Process finished.")
        self.p = None

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ew = ControlPanelWidget()    
    sys.exit(app.exec_())

