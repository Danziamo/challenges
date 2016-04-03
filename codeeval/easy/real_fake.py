import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.rstrip().replace(' ', '')
        s = 0
        for i in range(0, len(test)):
            if i % 2 == 0:
                s += 2*int(test[i])
            else:
                s += int(test[i])
        if s%10 == 0:
            print 'Real'
        else:
            print 'Fake'