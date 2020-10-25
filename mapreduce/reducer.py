#!/usr/bin/env python

import sys

last_key = None
running_total = 0

for line in sys.stdin:
    # split line into key and value
    line = line.strip().split()
    this_key, value = line
    value = int(value)

    # This only works because the reducer
    # receives its data sorted by key:
    if this_key == last_key:
        running_total = running_total + 1
    else:
        if last_key:
            print( '%s\t%s' % (last_key, running_total) )
        last_key = this_key
        running_total = value

print( '%s\t%s' % (last_key, running_total) )