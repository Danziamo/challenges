from math import sqrt

def is_prime(a):
    r = int(sqrt(a)) + 1
    for j in xrange(3, r, 2):
        if a % j == 0:
            return False
    return True

test_cases = int(raw_input())

l = [2, 3, 5]

i = 0
m = 7
while i < 10000:
    if is_prime(m):
        l.append(m)
        i += 1
    m += 2


for case in xrange(test_cases):
    n = int(raw_input())
    print l[n - 1]