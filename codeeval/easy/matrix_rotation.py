import sys
import math

with open(sys.argv[1], 'r') as input:
    for row in input:
        a = row.rstrip().split()
        l = int(math.sqrt(len(a)))
        m = []
        for i in range(0, l):
            m.append(a[i*l:(i+1)*l])

        for i in range(0, l/2):
            for j in range(i, l-i - 1):
                t = m[i][j]
                m[i][j] = m[l - 1 - j][i]
                m[l - 1 - j][i] = m[l - i - 1][l - 1 - j]
                m[l - i - 1][l - 1 - j] = m[j][l - i - 1]
                m[j][l - i - 1] = t

        for i in m:
            print " ".join(i),
        print
