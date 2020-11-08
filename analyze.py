#!/usr/bin/env python
# -*- coding:utf-8 -*-

from config import *
from singleton import *


class Analyze(Singleton):

    def __init__(self, arg, data):

        assert data, "Data cannot be empty"

        self.players = data
        self.arg = arg

    def analyze(self):
        if self.arg[0] == "7" or self.arg[0] == "8":
            best = getattr(self, OPTIONS[self.arg[0]])()
        else:
            best = self.best_single()

        result = "\nPlayer Name: {}\n".format(best)
        for stat_type, stat in self.filtered[best].items():
            result += "{}: {}\n".format(stat_type, stat)

        return result

    def best_single(self):
        return max(self.filtered, key = lambda  x: self.filtered[x][OPTIONS[self.arg[0]]])

    def best_def(self):
        return max(self.filtered, key = lambda x:
                   self.filtered[x]["blocks"] * 0.3
                   + self.filtered[x]["hits"] * 0.15
                   + self.filtered[x]["time_on_ice_avg"] * 0.2
                   + self.filtered[x]["plus_minus"] * 0.2)

    def best_for(self):
        return max(self.filtered, key = lambda x:
                   self.filtered[x]["goals"] * 0.3
                   + self.filtered[x]["assists"] * 0.2
                   + self.filtered[x]["blocks"] * 0.1
                   + self.filtered[x]["hits"] * 0.1
                   + self.filtered[x]["time_on_ice_avg"] * 0.1
                   + self.filtered[x]["plus_minus"] * 0.1
                   + self.filtered[x]["faceoff_percentage"] * 0.1)

    def time(self):
        for name in self.players.keys():
            mins, secs = list(map(int, self.players[name]["time_on_ice_avg"].split(":")))
            atoi = mins * 60 + secs
            self.players[name]["time_on_ice_avg"] = atoi

    def filter(self):
        f_age_pos = dict()

        for name, stat in self.players.items():
            if stat["age"] >= AGE[self.arg[2]][0] and stat["age"] <= AGE[self.arg[2]][1]:
                if self.arg[0] != "3" or self.arg[0] != "7":
                    if self.arg[1] != "5":
                        if stat["pos"] == POSITION[self.arg[1]]:
                            f_age_pos[name] = stat
                    else:
                        f_age_pos[name] = stat
                else:
                    f_age_pos[name] = stat

        if self.arg[3] == "any":
            if f_age_pos:
                return f_age_pos
            return False

        filtered = dict()
        for name, stat in f_age_pos.items():
            if stat["team"] == self.arg[3]:
                filtered[name] = stat

        f_age_pos = None # Destruct

        if filtered:
            return filtered
        return False


    def handle(self):

        self.time()
        self.filtered = self.filter()

        if self.filtered:
            result = self.analyze()
            return result
        return "No Result"