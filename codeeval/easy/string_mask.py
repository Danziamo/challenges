import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        a, b = test.rstrip().split()
        for i in range(0, len(a)):
            if b[i] == '1':
                sys.stdout.write(a[i].upper())
            else:
                sys.stdout.write(a[i].lower())
        print