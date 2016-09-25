l = []
for row in xrange(20):
    l.append(map(int, raw_input().rstrip().split()))
p = 0

for i in xrange(20):
    for j in xrange(20):
        if j > 16:
            continue
        if l[i][j] * l[i][j + 1] * l[i][j + 2] * l[i][j + 3] > p:
            p = l[i][j] * l[i][j + 1] * l[i][j + 2] * l[i][j + 3]

for i in xrange(20):
    if i > 16:
        continue
    for j in xrange(20):
        if l[i][j] * l[i + 1][j] * l[i + 2][j] * l[i + 3][j] > p:
            p = l[i][j] * l[i + 1][j] * l[i + 2][j] * l[i + 3][j]

for i in xrange(20):
    if i > 16:
        continue
    for j in xrange(20):
        if j > 16:
            continue
        if l[i][j] * l[i + 1][j + 1] * l[i + 2][j + 2] * l[i + 3][j + 3] > p:
            p = l[i][j] * l[i + 1][j + 1] * l[i + 2][j + 2] * l[i + 3][j + 3]

for i in xrange(20):
    if i > 16:
        continue
    for j in xrange(20):
        if j < 3:
            continue
        if l[i][j] * l[i + 1][j - 1] * l[i + 2][j - 2] * l[i + 3][j - 3] > p:
            p = l[i][j] * l[i + 1][j - 1] * l[i + 2][j - 2] * l[i + 3][j - 3]

print p