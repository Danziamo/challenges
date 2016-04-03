import sys

with open(sys.argv[1], 'r') as input:
    for row in input:
        n = int(row.rstrip())
        r = '3, '
        if n > 7:
            r += str(7) + ', '
        if n > 31:
            r += str(31) + ', '
        if n > 127:
            r += str(127) + ', '
        if n > 2047:
            r += str(2047)
        print r.rstrip(', ')

