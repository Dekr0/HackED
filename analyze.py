#!/usr/bin/env python
# -*- coding:utf-8 -*-

from config import *

class Analyze:

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
        pass

    def best_play(self):
        pass

    def best_od(self):
        pass

    def best_pm(self):
        pass

    def most_atoi(self):
        pass

    def most_pim(self):
        pass

    def best_def(self):
        pass

    def best_for(self):
        pass

    def filter(self):
        filtered = dict()
        for name, stat in self.players.items():
            if stat["age"] >= AGE[self.arg[2]][0] and stat["age"] <= AGE[self.arg[2]][1] \
                    and stat["team"] == self.arg[3]:
                if self.arg[0] == "1" or self.arg[0] == "2":
                    if stat["pos"] == POSITION[self.arg[1]]:
                        filtered[name] = stat
                else:
                    filtered[name] = stat

        return filtered


    def handle(self):
        assert (self.arg[0] in self.options.keys() and self.arg[1] in POSITION.keys()
                and self.arg[2] in AGE.keys()), "Cannot find keys"

        self.filtered = self.filter()
        print(self.filtered)
        assert self.filtered, ("Cannot be empty")

        self.analyze()