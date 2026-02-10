#!/usr/bin/python

keyword = input("What you gotta say? : ").strip()

while True:
    keyword = input("I got that! Anything else? : ").strip()
    if keyword == "STOP":
        break