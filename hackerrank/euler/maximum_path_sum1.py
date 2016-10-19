test_cases = int(raw_input())

for test in xrange(test_cases):
    n = int(raw_input())
    arr = []
    arr_sum = []
    for i in xrange(n):
        arr.append(map(int, raw_input().split()))

    for i in xrange(1, n):
        for j in xrange(len(arr[i])):
            if j == 0:
                arr[i][0] += arr[i-1][0]
            elif j == len(arr[i]) - 1:
                arr[i][j] += arr[i - 1][j - 1]
            else:
                arr[i][j] += max(arr[i - 1][j - 1], arr[i - 1][j])

    print max(arr[n - 1])