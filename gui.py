#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
WIP, not in used
"""

import sys
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from singleton import *


class Query(Singleton):

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.framework = MainFramework()
        self.window = QueryWindow(self.framework)
        self.show()

    def show(self):
        self.window.show()
        sys.exit(self.app.exec_())


class MainFramework(QWidget):

    def __init__:
        pass


class QueryWindow(QMainWindow):
    pass

