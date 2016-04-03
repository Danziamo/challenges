import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        n, row = test.rstrip().split(';')
        n = int(n.strip())
        row = [int(i) for i in row.strip().split()]
        m = 0
        for i in range(0, n):
            m += row[i]
        s = m

        for i in range(1, len(row) - n + 1):
            s -= row[i - 1]
            s += row[i + n - 1]
            if s > m:
                m = s
        print m if m > 0 else 0
