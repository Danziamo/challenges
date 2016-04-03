import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        x, y, n = [int(i) for i in test.rstrip().split()]
        for i in xrange(1, n+1):
            if i % x == 0 and i % y == 0:
                print 'FB',
            elif i % x == 0:
                print 'F',
            elif i % y == 0:
                print 'B',
            else:
                print i,
        print