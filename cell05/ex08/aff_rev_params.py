#!/usr/bin/python

import sys

params_count = len(sys.argv) - 1

if params_count < 2:
    print("none")
else:
    for i in range(params_count, 0, -1):
        print(sys.argv[i])