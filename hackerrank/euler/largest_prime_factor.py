import math

test_cases = int(raw_input())

def is_prime(a):
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    r = int(math.sqrt(a)) + 1
    for i in xrange(3, r, 2):
        if a % i == 0:
            return False
    return True

for case in xrange(1, test_cases+1):
    n = int(raw_input().rstrip())
    c = 1
    while n % c == 0 and n != c:
        if is_prime(n/c):
            print n/c
            break

        n = n/c
        if c == 1 or n%c != 0:
            c += 1

        while n%c != 0:
            c += 1
