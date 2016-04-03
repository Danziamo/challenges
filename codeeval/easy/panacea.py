import sys

with open(sys.argv[1], 'r') as input:
    for row in input:
        a, b = row.rstrip().split('|')
        a = a.strip().split()
        b = b.strip().split()
        s1 = 0
        s2 = 0
        for i in a:
            s1 += int(i, 16)
        for i in b:
            s2 += int(i, 2)
        if s2 >= s1:
            print 'True'
        else:
            print 'False'