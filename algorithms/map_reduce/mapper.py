#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip().split(",", 1)

    if line[0] == "BibNumber":
        pass
    else:
        key = line[0]
        value = 1

        print( '%s\t%s' % (key, value) )
        value = 1

        print( '%s\t%s' % (key, value) )
