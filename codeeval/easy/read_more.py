import sys

with open(sys.argv[1], 'r') as input:
    for row in input:
        row = row.rstrip()
        if len(row) > 55:
            print row[:40].rsplit(' ', 1)[0] + '... <Read More>'
        else:
            print row