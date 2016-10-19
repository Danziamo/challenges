#!/bin/python

import sys

Q = int(raw_input().strip())
for a0 in xrange(Q):
    colors = {}
    n = int(raw_input().strip())
    b = raw_input().strip()
    for item in b:
        colors[item] = colors.get(item, 0) + 1

    is_even = True
    for i in colors.keys():
        if i != '_' and colors[i] == 1:
            print 'NO'
            is_even = False
            break
    if not is_even:
        continue

    if colors.get('_', 0) != 0:
        print 'YES'
        continue

    for i in xrange(1, n - 1):
        if b[i] != b[i - 1] and b[i] != b[i + 1]:
            is_even = False
            break

    if is_even:
        print 'YES'
    else:
        print 'NO'
