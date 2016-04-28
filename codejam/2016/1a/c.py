test_cases = int(raw_input())

for case in xrange(1, test_cases+1):
    n = int(raw_input())
    l = [int(i) - 1 for i in raw_input().split()]
    m = 0
    print l
    r = 0
    v = [0]*n
    for i in range(n):
        cur = i
        visited = [0]*n
        visited[cur] = 1
        while visited[l[cur]] == 0 and visited[l[cur]] < 10:
            print cur, l[cur], visited[cur], visited[l[cur]]
            visited[l[cur]] = visited[cur] + 1
            cur = l[cur]

        if visited[cur] > m:
            m = visited[cur]

    print m
    #print "Case #{}: {}".format(case, "INSOMNIA")