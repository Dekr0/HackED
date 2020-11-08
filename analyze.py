#!/usr/bin/env python
# -*- coding:utf-8 -*-

from config import *
from singleton import *

class Analyze(Singleton):

    def __init__(self, arg, data):

        assert data, "Data cannot be empty"

        self.players = data
        self.arg = arg
        self.options = {
            "1": self.best_goal,
            "2": self.best_play,
            "3": self.best_od,
            "4": self.best_pm,
            "5": self.most_atoi,
            "6": self.most_pim,
            "7": self.best_def,
            "8": self.best_for
        }

    def analyze(self):
        pass

    def best_goal(self):


        j = max(self.filtered, key = lambda x: self.filtered[x]["goals"])
        print(j)

        pass

    def best_play(self):
        j = max(self.filtered, key = lambda x: self.filtered[x]["assists"])
        print(j)
        pass

    def best_od(self):

        #ONLY FOR POSITION = D
        j = max(self.filtered, key = lambda x: self.filtered[x]["points"])
        print(j)
        pass

    def best_pm(self):
        #plus minus
        j = max(self.filtered, key = lambda x: self.filtered[x]["plus_minus"])
        print(j)
        pass

    def most_atoi(self):
        j = max(self.filtered, key = lambda x: self.filtered[x]["time_on_ice_avg"])
        print(j)
        pass

    def most_pim(self):
        j = max(self.filtered, key = lambda x: self.filtered[x]["pen_min"])
        print(j)
        pass

    def best_def(self):
        j = max((0.3*(self.filtered, key = lambda x: self.filtered[x]["blocks"])+
                (0.15*(self.filtered, key = lambda x: self.filtered[x]["hits"]))+
                (0.15*(self.filtered, key = lambda x: self.filtered[x]["time_on_ice_avg"]))+
                (0.2*(self.filtered, key = lambda x: self.filtered[x]["points"]))+
                (0.2*(self.filtered, key = lambda x: self.filtered[x]["plus_minus"]))))
        print(j)
        pass

    def best_for(self):
        j = max((0.3*(self.filtered, key = lambda x: self.filtered[x]["goals"])+
                (0.2*(self.filtered, key = lambda x: self.filtered[x]["assists"]))+
                (0.1*(self.filtered, key = lambda x: self.filtered[x]["blocks"]))+
                (0.1*(self.filtered, key = lambda x: self.filtered[x]["hits"]))+
                (0.1*(self.filtered, key = lambda x: self.filtered[x]["plus_minus"]))+
                (0.1*(self.filtered, key = lambda x: self.filtered[x]["faceoff_percentage"]))))
        print(j)
        pass

    def filter(self):
        f_age_pos = dict()

        for name, stat in self.players.items():
            if stat["age"] >= AGE[self.arg[2]][0] and stat["age"] <= AGE[self.arg[2]][1]:
                if self.arg[0] == "1" or self.arg[0] == "2":
                    if stat["pos"] == POSITION[self.arg[1]]:
                        f_age_pos[name] = stat
                else:
                    f_age_pos[name] = stat

        if self.arg[3] == "32":
            return f_age_pos

        filtered = dict()
        for name, stat in f_age_pos.items():
            if stat["team"] == self.arg[3]:
                filtered[name] = stat

        f_age_pos = None # Destruct

        return filtered


    def handle(self):
        # assert (self.arg[0] in self.options.keys() and self.arg[1] in POSITION.keys()
        #         and self.arg[2] in AGE.keys()), "Cannot find keys"

        self.filtered = self.filter()
        for key, value in self.filtered.items():
            print(key, value)
        assert self.filtered, ("Cannot be empty")

        self.analyze()