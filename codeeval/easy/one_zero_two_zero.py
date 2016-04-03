import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        a, b = test.rstrip().split()
        a = int(a)
        b = int(b)
        s = 0
        for i in range(1, b + 1):
            if bin(i)[2:].count('0') == a:
                s += 1
        print s