#!/usr/bin/python

import sys

def downcase_it(list):
    for i in range(len(list)):
        print(list[i].lower())

if len(sys.argv) <= 1:
    print("none")
else:
    downcase_it(sys.argv[1:])