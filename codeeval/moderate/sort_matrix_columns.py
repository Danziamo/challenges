import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        m = []
        c = 1
        for i in test.rstrip().split('|'):
            m.append((i.strip().split(), c))
            c += 1

        for i in m:
            print m