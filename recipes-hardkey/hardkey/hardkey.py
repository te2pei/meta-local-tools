#!/usr/bin/env pythona
# coding: utf-8
#

import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ExampleWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.move(300, 300)
        self.setWindowTitle('Hardware Keys')

        # buttonの設定
        self.button = QPushButton('Poweroff')
        self.label = QLabel('connected')

        # buttonのclickでF9送信
        self.button.clicked.connect(self.pushButtionClicked)

        # レイアウト配置
        self.grid = QGridLayout()
        self.grid.addWidget(self.button, 0, 0, 1, 1)
        self.grid.addWidget(self.label, 1, 0, 1, 2)
        self.setLayout(self.grid)

        # 表示
        self.show()

    def pushButtionClicked(self):
        '''Push Button が押されると呼ばれる。F9 キーを押す
        '''
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
    ew = ExampleWidget()    
    sys.exit(app.exec_())

