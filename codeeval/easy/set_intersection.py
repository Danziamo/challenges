import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        a, b = test.rstrip().split(';')
        a = [int(i) for i in a.split(',')]
        b = [int(i) for i in b.split(',')]
        intersecting_points = set(enumerate(a)).intersection(set(enumerate(b)))
        print ','.join(str(i) for i in sorted(list(set(a).intersection(b))))