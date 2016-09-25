import bisect
test_cases = int(raw_input())
l = set()

def generate_palindromes():
    for i in xrange(100, 1000):
        for j in xrange(100, 1000):
            p = i * j
            if p <= 100000 or p > 999999:
                continue
            s = str(p)
            if s[0] != s[-1] or s[1] != s[-2] or s[2] != s[3]:
                continue
            l.add(p)

generate_palindromes()
l = list(l)
l.sort()
for case in xrange(test_cases):
    n = int(raw_input().rstrip())
    print l[bisect.bisect_left(l, n) - 1]