#!/usr/bin/env python
# -*- coding:utf-8 -*-

from fake_useragent import UserAgent

AGENT = UserAgent().random
URL = "https://www.hockey-reference.com/leagues/NHL_2020_skaters.html#stats::goals"
HEADER = {
    "user-agent": AGENT,
    "referrer": URL
}