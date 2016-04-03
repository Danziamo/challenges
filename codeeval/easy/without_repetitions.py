import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.rstrip()
        sys.stdout.write(test[0])
        for i in range(1, len(test)):
            if test[i] != test[i - 1]:
                sys.stdout.write(test[i])
        print