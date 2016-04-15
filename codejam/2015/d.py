import math

test_cases = int(raw_input())

for case in xrange(1, test_cases+1):
    x, r, c = [int(i) for i in raw_input().split()]
    s = min(r, c)
    m = max(r, c)
    res = "GABRIEL"
    if s*m % x != 0:
        res = 'RICHARD'
    if x == 3 and s == 1:
        res = 'RICHARD'
    if x == 4 and s <= 2:
        res = 'RICHARD'
    if x == 5 and s <= 2 or (s == 3 and m == 5):
        res = 'RICHARD'
    if x == 6 and s <= 3:
        res = 'RICHARD'
    if x > 6:
        res = 'RICHARD'
    print "Case #{}: {}".format(case, res)