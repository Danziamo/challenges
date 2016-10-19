l = [0] * 5000001
l[1] = 1
for i in xrange(2, 5000001):
    if i % 2 == 0:
        l[i] = l[i/2] + 1
    else:
        print l

test_cases = int(raw_input())

for case in xrange(test_cases):
    n = int(raw_input())