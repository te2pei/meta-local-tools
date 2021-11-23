#!/usr/bin/env pythona
# -*- coding: utf-8 -*-

import sys
import subprocess
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout 


class ControlPanelWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.names = ['POWER' , 'RETURN', ''  , '↑', '' ,
                      'SOFT-L', 'SOFT-R', '←' , '' , '→',
                      'LINE'  , 'ENTER' , ''  , '↓', '',
                     ]

        self.keycodes = [
            'KEY_F9'    , 'KEY_UNKNOWN', '0'     , 'KEY_F10', '0'      ,
            'KEY_F1'    , 'KEY_F2'     , 'KEY_F8', '0'      , 'KEY_F11',
            'KEY_PAUSE' , 'KEY_F7'     , '0'     , 'KEY_F12', '504'    ,
        ]

        self.initUI()
        self.counter = 0
        self.keycode = ''

    def initUI(self):
        self.resize(250, 150)
        self.move(300, 300)
        self.setWindowTitle('Control Panel')
        self.grid = QGridLayout()

        positions = [(y,x) for y in range(3) for x in range(5)]

        for position, name in zip(positions, self.names):
            if name == '':
                    continue

            self.button = QPushButton(name)
            self.button.setAutoRepeat(True)
            self.button.setAutoRepeatDelay(500)    # 1sec
            self.button.setAutoRepeatInterval(300)  # 300msec
            self.button.pressed.connect(self.buttonPress)
            #self.button.released.connect(self.buttonRelease)
            #self.button.clicked.connect(self.buttonClick)
            self.grid.addWidget(self.button, *position)

            # timer
            self.timer=QTimer()
            self.timer.timeout.connect(self.buttonRelease)

        # レイアウト配置
        self.setLayout(self.grid)

        # 表示
        self.show()

    def buttonPress(self): 
        btn = self.sender()
        self.timer.stop()
        self.timer.start(350)

        self.counter += 1
        if self.counter > 2:
           self.counter = 2

        for name, keycode in zip(self.names, self.keycodes):
            if btn.text() == name:
                cmd = './hardkey ' + keycode + ' ' + str(self.counter) + ' > /dev/input/event2'
                res = subprocess.call(cmd, shell=True)
                self.keycode = keycode

    def buttonRelease(self): 

        btn = self.sender()
        self.counter = 0
        self.timer.stop()
        cmd = './hardkey ' + self.keycode + ' ' + str(self.counter) + ' > /dev/input/event2'
        res = subprocess.call(cmd, shell=True)
#        print(cmd)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ew = ControlPanelWidget()    
    sys.exit(app.exec_())

