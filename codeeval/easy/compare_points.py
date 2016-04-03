import sys

with open(sys.argv[1], 'r') as input:
    for row in input:
        l = [int(i) for i in row.rstrip().split()]

        if l[2] == l[0]:
            if l[1] > l[3]:
                print 'S'
            elif l[1] < l[3]:
                print 'N'
            else:
                print 'here'
            continue

        if l[1] == l[3]:
            if l[0] > l[2]:
                print 'W'
            elif l[0] < l[2]:
                print 'E'
            else:
                print 'here'
            continue

        result = ''

        if l[1] > l[3]:
            result += 'S'
        else:
            result += 'N'
        if l[2] > l[0]:
            result += 'E'
        else:
            result += 'W'

        print result