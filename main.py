#!/usr/bin/env python
# -*- coding:utf-8 -*-

from config import TEAM
from fetch import *
from analyze import *


def main():
    while True:
        with open("description", "r") as f:
            options = []
            while len(options) != 4:
                while True:
                    line = f.readline().strip()
                    if line[0] == "%":
                        options.append(input(line[1:]).strip())
                        break
                    print(line)

        # options = ["3", "5", "6", "21"]

        assert len(options) == 4, "Not enough options"
        assert (options[0] in OPTIONS.keys() and options[1] in POSITION.keys()
                and options[2] in AGE.keys() and options[3] in TEAM.keys()), "Invalid options"

        options[3] = TEAM[options[3]]

        crawler = Crawler()
        analyze = Analyze(options, crawler.handle())
        result = analyze.handle()
        print(result)


if __name__ == "__main__":
    main()