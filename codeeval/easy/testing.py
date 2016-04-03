import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        a, b = test.rstrip().split(' | ')
        s = 0
        for i in range(0, len(b)):
            if a[i] != b[i]:
                s += 1
            if s > 6:
                break

        if s > 6:
            print 'Critical'
        elif s > 4:
            print 'High'
        elif s > 2:
            print 'Medium'
        elif s > 0:
            print 'Low'
        else:
            print 'Done'