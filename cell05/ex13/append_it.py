#!/usr/bin/python

import sys

params_count = len(sys.argv) - 1
if params_count > 0:
    for i in range(1, params_count + 1):
        if not sys.argv[i].endswith("ism"):
            print(f"{sys.argv[i]}ism")