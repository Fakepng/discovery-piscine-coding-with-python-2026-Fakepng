#!/usr/bin/python

import sys

if len(sys.argv) != 3:
    print("none")
    sys.exit()

start = int(sys.argv[1])
end = int(sys.argv[2])

final_array = []
for num in range(start, end + 1):
    final_array.append(num)

print(final_array)