import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        row = test.rstrip().split()
        word = row[0]
        row.sort(key=len)
        if len(row) > 1 and len(row[-1]) != len(row[-2]):
            word = row[-1]
        s = ""
        for i in range(0, len(word)):
            s += '*'*i + word[i] +' '
        print s.rstrip()