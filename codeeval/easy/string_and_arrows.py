import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        s = 0
        i = -1
        j = -1
        test = test.rstrip()
        for i in range(5, len(test) + 1):
            if test[i - 5:i] in ['<--<<','>>-->']:
                s += 1
        print s