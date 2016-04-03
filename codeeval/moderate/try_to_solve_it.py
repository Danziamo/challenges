import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
        b = ['u', 'v', 'w', 'x', 'y', 'z', 'n', 'o', 'p', 'q', 'r', 's', 't']

        for i in test.rstrip():
            if i in a:
                sys.stdout.write(b[a.index(i)])
            else:
                sys.stdout.write(a[b.index(i)])
        print