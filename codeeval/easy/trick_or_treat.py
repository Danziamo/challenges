import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        kids = test.rstrip().split(',')
        c = 3
        s = 0
        p = 0
        for kid in kids:
            t, n = kid.split(':')
            n = int(n.strip())
            if c < 6:
                s += n * c
                p += n
            else:
                print s*n/p
            c += 1