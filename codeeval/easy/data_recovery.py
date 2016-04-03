import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        l, n = test.rstrip().split(';')
        n = [int(i) for i in n.strip().split()]
        l = l.strip().split()
        s = 0
        a = ['']*len(l)
        for i in range(0, len(n)):
            a[n[i]-1] = l[i]
            s += n[i]
        p = len(l)*(len(l) + 1)/2 - s
        a[p-1] = l[len(l)-1]
        print ' '.join(a)