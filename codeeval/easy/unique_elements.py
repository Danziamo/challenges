import sys

with open(sys.argv[1], 'r') as input:
    for row in input:
        list = set(row.rstrip().split(','))
        list = sorted(list)
        list = sorted(list, key=len)
        print ','.join(list)