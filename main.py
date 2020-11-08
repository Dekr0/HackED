#!/usr/bin/env python
# -*- coding:utf-8 -*-

from fetch import *
from analyze import *

if __name__ == "__main__":

    arg = ["1", "2", "2", "OTT"]
    assert len(arg) == 4, "Not enough argument"

    crawler = Crawler()
    analyze = Analyze(arg, crawler.handle())
    analyze.handle()