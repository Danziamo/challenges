import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.rstrip().rstrip(';').split(';')
        l = [0]
        for i in test:
            l.append(int(i.strip().split(',')[1]))
        l.sort()
        for i in range(1, len(l) - 1):
            sys.stdout.write(str(l[i] - l[i-1]) + ',')
        print str(l[len(l)-1] - l[len(l) - 2])