#!/usr/bin/python

import sys

params_count = len(sys.argv) - 1
if params_count > 0:
    print(sys.argv[1])
else:
    print("none")