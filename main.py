#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from os import path
from config import TEAM
from fetch import *
from analyze import *


def main():

    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        bundle_dir = getattr(sys, "_MEIPASS", path.abspath(path.dirname(__file__)))
        prompt = path.abspath(path.join(bundle_dir, "description.txt"))
    else:
        prompt = "description.txt"

    while True:
        with open(prompt, "r") as f:
            options = []
            while len(options) != 4:
                while True:
                    line = f.readline().strip()
                    if line[0] == "%":
                        option = input(line[1:]).strip()
                        if option == "exit" or option == "quit":
                            quit()
                        options.append(option)
                        break
                    print(line)

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