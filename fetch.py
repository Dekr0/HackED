#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Age, Tm, Pos, G, A, PTS, +/-, PIM, ATOI, BLK, HITS, FOW, FO%

import requests
import re
import sys
from bs4 import BeautifulSoup
from bs4 import element
from config import *


class Crawler:

    def __init__(self):
        self.players = dict()
        self.src = ""
        self.soup = None

    def get_name_team(self):
        name_parents = self.soup.find_all("td", {"data-append-csv": re.compile(".*")})
        team_parents = self.soup.find_all("td", {"data-stat": "team_id"})
        for name_parent, team_parent in zip(name_parents, team_parents):
            name = str(name_parent["csk"])
            team_tag = team_parent.contents[0]
            team = str(team_tag) if type(team_tag) is element.NavigableString else str(team_tag.contents[0])
            if name in self.players.keys():
                self.players["-".join((name, team))] = {"team": team}
            else:
                self.players[name] = {"team": team}

    def get_perform(self, tag):
        parents = self.soup.find_all("td", {"data-stat": tag})
        assert len(parents) == len(self.players), "Website's data format change"
        for parent, name_team in zip(parents, self.players.keys()):
            if parent.contents:
                try:
                    value = int(parent.contents[0])
                except ValueError:
                    try:
                        value = float(parent.contents[0])
                    except ValueError:
                        value = str(parent.contents[0])
                self.players[name_team][tag] = value
            else:
                self.players[name_team][tag] = None

    def get_data(self):
        self.get_name_team()
        for tag in DATA_TAG:
            self.get_perform(tag)

    def handle(self):
        self.request()
        assert self.src, "Fetch nothing"

        self.soup = BeautifulSoup(self.src, "lxml")
        self.get_data()

        return self.players

    def request(self):
        try:
            response = requests.get(URL, headers=HEADER)
            self.src = response.text
            response.close()
        except Exception as ex:
            quit(ex)