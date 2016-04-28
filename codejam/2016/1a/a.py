test_cases = int(raw_input())

for case in xrange(1, test_cases+1):
    s = raw_input()
    r = s[0]
    for i in xrange(1, len(s)):
        if s[i] >= r[0]:
            r = s[i] + r
        else:
            r = r + s[i]
        #print r
    #print r
    print "Case #{}: {}".format(case, r)