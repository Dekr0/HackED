#!/usr/bin/env python
# -*- coding:utf-8 -*-

from fake_useragent import UserAgent

AGENT = UserAgent().random

AGE = {
    "1": [18, 23],
    "2": [24, 29],
    "3": [30, 35],
    "4": [36, 40],
    "5": [40, 999],
    "6": [0, 999]
}

DATA_TAG = ["age",
            "pos",
            "goals",
            "assists",
            "points",
            "plus_minus",
            "pen_min",
            "time_on_ice_avg",
            "blocks",
            "hits",
            "faceoff_wins",
            "faceoff_percentage"
            ]

POSITION = {
    "1": "C",
    "2": "LW",
    "3": "RW",
    "4": "D"
}

URL = "https://www.hockey-reference.com/leagues/NHL_2020_skaters.html#stats::goals"
HEADER = {
    "user-agent": AGENT,
    "referrer": URL
}