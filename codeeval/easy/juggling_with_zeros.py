import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        s = ''
        test = test.rstrip().split()
        for i in range(1, len(test), 2):
            if test[i - 1] == '0':
                s += '0'*len(test[i])
            else:
                s += '1'*len(test[i])
        print int(s, 2)