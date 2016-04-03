import sys

with open(sys.argv[1], 'r') as input:
    for row in input:
        a = row.rstrip().split()
        a.pop(0)
        a = sorted([int(i) for i in a])
        min = 999999
        for i in a:
            sum = 0
            for k in a:
                sum += abs(k - i)
            if min > sum:
                min = sum
        print min

