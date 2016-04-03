import sys

with open(sys.argv[1], 'r') as input:
    for row in input:
        a = row.rstrip('\n').split(',')
        print a[0].rfind(a[1])