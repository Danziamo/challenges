from math import sqrt
from bisect import bisect_right, bisect_left


def is_prime(a):
    r = int(sqrt(a)) + 1
    for j in xrange(3, r, 2):
        if a % j == 0:
            return False
    return True


l = {2: 2, 1: 0}
s = 2
for i in xrange(3, 1000000, 2):
    if is_prime(i):
        s += i
        l[i] = s

#print l.keys()
a = sorted(l.keys())

test_cases = int(raw_input())

for case in xrange(test_cases):
    n = int(raw_input())
    print l[a[bisect_right(a, n) - 1]]