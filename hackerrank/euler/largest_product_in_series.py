test_cases = int(raw_input())


def count_max(s, k):
    p = 1
    m = 0
    for i in xrange(len(s)):
        if i >= k:
            p /= int(s[i - k])
        p *= int(s[i])
        if p > m:
            m = p
    return m


for case in xrange(test_cases):
    n, k = map(int, raw_input().rstrip().split())
    m = 0
    s = raw_input().rstrip()
    l = s.split('0')
    for i in l:
        if len(i) >= k:
            p = count_max(i, k)
            if p > m:
                m = p
    print m