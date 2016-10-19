test_cases = int(raw_input())
for test in xrange(test_cases):
    n = int(raw_input())
    n = str(pow(2, n))
    sum_counter = 0
    for digit in n:
        sum_counter += int(digit)
    print sum_counter