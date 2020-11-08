#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Age, Tm, Pos, G, A, PTS, +/-, PIM, ATOI, BLK, HITS, FOW, FO%

import requests
import re
import sys
from bs4 import BeautifulSoup
from config import *


class Crawler:

    def __init__(self):
        self.players = dict()
        self.src = ""
        self.soup = None

    def get_data(self):
        self.get_name()

    def get_name(self):
        name_parents = self.soup.find_all("td", {"data-append-csv": re.compile(".*")})
        team_parents = self.soup.find_all("td", {"class": "left", "data-stat": "team_id"})


    def handle(self):
        self.request()
        assert self.src, "Fetch nothing"

        self.soup = BeautifulSoup(self.src, "lxml")
        self.get_data()

    def request(self):
        try:
            response = requests.get(URL, headers=HEADER)
            self.src = response.text
            response.close()
        except Exception as ex:
            quit(ex)