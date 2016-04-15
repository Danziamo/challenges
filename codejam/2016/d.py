test_cases = int(raw_input())

for case in xrange(1, test_cases + 1):
    t, k, c = [int(i) for i in raw_input().split()]

    l = []
    s = ''
    if t == 1:
        s = '1'
    elif k == 1:
        if c < t:
            s = 'IMPOSSIBLE'
        else:
            s = ' '.join([str(i) for i in xrange(1, t + 1)])
    else:
        if c < t - 1:
            s = 'IMPOSSIBLE'
        else:
            s = ' '.join(str(i) for i in xrange(2, t + 1))

    print "Case #{}: {}".format(case, s)
