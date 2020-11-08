#!/usr/bin/env python
# -*- coding:utf-8 -*-

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

        options = ["1", "2", "2", "ANA"]

        assert len(options) == 4, "Not enough argument"

        crawler = Crawler()
        analyze = Analyze(options, crawler.handle())
        analyze.handle()

if __name__ == "__main__":
    main()