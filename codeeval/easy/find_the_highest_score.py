import sys

with open(sys.argv[1], 'r') as input:
    for row in input:
        row = row.rstrip().split('|')
        t = row[0].strip().split()
        m = [-1001]*len(t)
        for e in row:
            a = e.strip().split()
            for i in range(0, len(t)):
                if int(a[i]) > m[i]:
                    m[i] = int(a[i])

        print " ".join(str(i) for i in m)