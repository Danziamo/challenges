matrix = [[0] * 501 for i in range(501)]
matrix[0][0] = 1
for i in xrange(501):
    matrix[0][i] = 1
    matrix[i][0] = 1

for i in xrange(1, 501):
    for j in xrange(1, 501):
        matrix[i][j] += matrix[i - 1][j] + matrix[i][j - 1]

test_cases = int(raw_input())
for test in xrange(test_cases):
    n, m = map(int, raw_input().split())
    print matrix[n][m] % 1000000007
