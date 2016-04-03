import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        row, n = test.rstrip().split('|')
        row = row.strip().split()
        n = int(n.strip())

        for i in range(0, n):
            j = 1
            while j < len(row):
                if int(row[j]) < int(row[j - 1]):
                    t = row[j]
                    row[j] = row[j - 1]
                    row[j - 1] = t
                    break
                j += 1
            if j == len(row):
                break
        print ' '.join(row)