import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        a, n = test.rstrip().split('|')
        a = a.strip().split()
        n = int(n.strip())
        while len(a) != 1:
            a.remove(a[(n - 1)%len(a)])
        print a[0]