s = 0
l = []
for i in xrange(1, 10001):
    s += i * i
    t = ((i + 1)*i)/2
    l.append(t*t - s)

test_cases = int(raw_input())

for case in xrange(test_cases):
    n = int(raw_input().rstrip())
    print l[n - 1]