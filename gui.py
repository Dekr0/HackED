#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
WIP, not in used
"""

import sys
from config import *
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

    def __init__(self):
        super(MainFramework, self).__init__()
        self.init_type_selection()
        self.init_pos_selection()
        self.init_age_selection()
        self.init_team_selection()

        self.button = QPushButton("Search")
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.stat_box)
        self.layout.addWidget(self.age_box)
        self.layout.addWidget(self.pos_box)
        self.layout.addWidget(self.team_box)

    def init_type_selection(self):
        self.stat_box = QGroupBox("Stat Type")
        self.stat_layout = QHBoxLayout()
        self.stat_combobox = QComboBox()

        self.stat_combobox.addItems(STAT_TYPE.key())

        self.stat_layout.addWidget(self.stat_combobox)

        self.stat_box.setLayout(self.stat_layout)

    def init_pos_selection(self):
        self.pos_box = QGroupBox("Position")
        self.pos_layout = QHBoxLayout()
        self.pos_combobox = QComboBox()

        self.pos_combobox.addItems(POSITION.values())

        self.pos_layout.addWidget(self.pos_combobox)

        self.pos_box.setLayout(self.pos_layout)

    def init_age_selection(self):
        self.age_box = QGroupBox("Age Range")
        self.age_layout = QHBoxLayout()
        self.age_combobox = QComboBox()

        self.age_combobox.addItems(POSITION.values())

        self.age_layout.addWidget(self.age_combobox)

        self.age_box.setLayout(self.age_layout)

    def init_team_selection(self):
        self.team_box = QGroupBox("Team")
        self.team_layout = QHBoxLayout()
        self.team_combobox = QComboBox()

        self.team_combobox.addItems(TEAM.values())

        self.team_layout.addWidget(self.team_combobox)

        self.team_box.setLayout(self.team_layout)

class QueryWindow(QMainWindow):
    pass

