import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.rstrip().lower()
        b = False
        for i in test:
            if 'a' <= i <= 'z':
                b = True
                sys.stdout.write(i)
            elif b:
                sys.stdout.write(' ')
                b = False
        print