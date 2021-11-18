#!/usr/bin/env pythona
# coding: utf-8
#

import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ControlPanelWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.move(300, 300)
        self.setWindowTitle('Control Panel')
        self.grid = QGridLayout()

        names = ['Power' , 'Return', ''  , '↑', '' ,
                 'SOFT-L', 'SOFT-R', '←' , '' , '→',
                 'LINE'  , 'ENTER' , ''  , '↓', ''
                ]

        positions = [(y,x) for y in range(3) for x in range(5)]

        for position, name in zip(positions, names):
            if name == '':
                    continue

            button = QPushButton(name)
            self.grid.addWidget(button, *position)

        # buttonの設定
        self.button = QPushButton('Poweroff')
        self.button.clicked.connect(self.pushButtonClicked)

        # レイアウト配置
        self.grid.addWidget(self.button, 0, 0, 1, 1)
        self.setLayout(self.grid)

        # 表示
        self.show()

    def pushButtonClicked(self): 

        self.p = QProcess(self)
        self.p.finished.connect(self.process_finished)
        #self.p.start(
        #    "/usr/local/bin/hardkey", [">", "/dev/input/event1"]
        #    )
        res = subprocess.call("/usr/local/bin/hardkey > /dev/input/event1", shell=True)
        print(res)

    def process_finished(self):
        print("Process finished.")
        self.p = None


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ew = ControlPanelWidget()    
    sys.exit(app.exec_())

