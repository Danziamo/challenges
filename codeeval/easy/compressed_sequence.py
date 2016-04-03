import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.rstrip().split()
        c = 1
        for i in range(1, len(test)):
            if test[i] == test[i - 1]:
                c += 1
            else:
                print c, test[i - 1],
                c = 1
        print c, test[-1]