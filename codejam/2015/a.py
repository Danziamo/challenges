import sys

test_cases = int(raw_input())

for case in xrange(1, test_cases+1):
    m, s = raw_input().split()
    m = int(m)
    n = 0
    c = 0
    for i in xrange(0, m + 1):
        if i > n:
            c += i - n
            n = i
        n += int(s[i])
    print "Case #{}: {}".format(case, c)