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

OPTIONS = {
    "1": "goals",
    "2": "assists",
    "3": "points",
    "4": "plus_minus",
    "5": "time_on_ice_avg",
    "6": "plus_minus",
    "7": "best_def",
    "8": "best_for"
}

POSITION = {
    "1": "C",
    "2": "LW",
    "3": "RW",
    "4": "D",
    "5": "ANY",
}

# Fixed in furture
STAT_TYPE = {
    "Best Goal Scorer": "goals",
    "Best Playmaker": "assists",
    "Best Offensive Decencemen": "points",
    "Best +/-": "plus_minus",
    "Most Time on Ice": "time_on_ice_avg",
    "Most Penalty Minutes": "plus_minus",
    "Best Overall Defenceman": "best_def",
    "Best Overall Forward": "best_for"
}

TEAM = {
    "1": 'ANA',
    "2": 'ARI',
    "3": 'BOS',
    "4": 'BUF',
    "5": 'CAR',
    "6": 'CBJ',
    "7": 'CGY',
    "8": 'CHI',
    "9": 'COL',
    "10": 'DAL',
    "11": 'DET',
    "12": 'EDM',
    "13": 'FLA',
    "14": 'LAK',
    "15": 'MIN',
    "16": 'MTL',
    "17": 'NJD',
    "18": 'NSH',
    "19": 'NYI',
    "20": 'NYR',
    "21": 'OTT',
    "22": 'PHI',
    "23": 'PIT',
    "24": 'SJS',
    "25": 'STL',
    "26": 'TBL',
    "27": 'TOR',
    "28": 'VAN',
    "29": 'VEG',
    "30": 'WPG',
    "31": 'WSH',
    "32": 'TOT',
    "33": 'any'
}

URL = "https://www.hockey-reference.com/leagues/NHL_2020_skaters.html#stats::goals"
HEADER = {
    "user-agent": AGENT,
    "referrer": URL
}
