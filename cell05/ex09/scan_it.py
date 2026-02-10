#!/usr/bin/python

import sys
import re

params_count = len(sys.argv) - 1
if params_count != 2:
    print("none")
else:
    pattern = sys.argv[1]
    string = sys.argv[2]

    match = re.findall(pattern, string)
    if match:
        print(len(match))
    else:
        print("none")