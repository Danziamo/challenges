dic = [0]*5000001
arr = [0]*25000001
arr[1] = 1
dic[1] = 1

max_value = 0
max_index = 0

for i in xrange(2, 5001):
    x = i
    k = 0
    while x != 1 and x >= i and arr[x] == 0:
        k += 1
        if x % 2 == 0:
            x /= 2
        else:
            x = 3*x + 1
    arr[i] = k + arr[x]
    if arr[i] >= max_value:
        max_index = i
        max_value = arr[i]
        dic[i] = max_index

test_cases = int(raw_input())
for test in xrange(test_cases):
    n = int(raw_input())
    print dic[n]
