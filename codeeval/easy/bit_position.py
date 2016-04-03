import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        n, p1, p2 = [int(i) for i in test.rstrip().split(',')]
        n = bin(n)[2:]
        if n[len(n) - p1] == n[len(n) - p2]:
            print 'true'
        else:
            print 'false'