import sys

l = []


def permutation(p, s):
    n = len(s)
    if n == 0:
        l.append(p)
    else:
        for i in xrange(0, n):
            permutation(p + s[i], s[0:i] + s[i + 1:n])


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        l = []
        permutation("", sorted(test.rstrip()))
        print ','.join(l)
