test_cases = int(raw_input())

for case in xrange(1, test_cases+1):
    n = int(raw_input())
    d = {}
    for i in xrange(1, 2*n):
        l = [int(x) for x in raw_input().split()]
        for k in l:
            if k not in d.keys():
                d.update({k: 1})
            else:
                d.update({k: d.get(k) + 1})

    l = []
    for i in d.keys():
        if d.get(i) % 2 != 0:
            l.append(i)

    print "Case #{}: {}".format(case, ' '.join([str(i) for i in sorted(l)]))