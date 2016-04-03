import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        row = test.rstrip().split()
        s = ""
        for i in row:
            m = list(i)
            t = m[0]
            m[0] = m[-1]
            m[-1] = t
            s += ''.join(m) + ' '
        print s