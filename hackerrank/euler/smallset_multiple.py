from fractions import gcd

d = {1: 1}
p = 1
for i in xrange(2, 41):
    g = gcd(p, i)
    if g == 1:
        d[i] = p * i
        p *= i
    else:
        d[i] = p * i/g
        p *= i/g

test_cases = int(raw_input())

for case in xrange(test_cases):
    n = int(raw_input())
    print d[n]