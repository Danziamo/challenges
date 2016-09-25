test_cases = int(raw_input())


for case in xrange(test_cases):
    n = int(raw_input())
    if n < 12:
        print -1
        continue

    b = 1
    nu = n * (n - 2 * b)
    de = 2 * (n - b)
    while b < nu/de and b < n/2:
        b += 1
        nu = n * (n - 2 * b)
        de = 2 * (n - b)

    while nu % de != 0 and b < n/2:
        b += 1
        nu = n * (n - 2 * b)
        de = 2 * (n - b)

    if nu % de == 0 and nu != 0 and n - nu / de - b > b > nu / de:
        a = nu / de
        print a * b * (n - a - b)
    else:
        print -1
