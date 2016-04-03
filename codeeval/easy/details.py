import sys

with open(sys.argv[1], 'r') as input:
    for row in input:
        m = row.rstrip().split(',')
        min = 999
        for s in m:
            d = s.find('Y') - s.rfind('X') - 1
            if d < min:
                min = d

        print min