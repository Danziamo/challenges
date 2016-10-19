months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum_days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

test_cases = int(raw_input())

for test in xrange(test_cases):
    start_year, start_month, start_day = map(int, raw_input().split())
    end_year, end_month, end_day = map(int, raw_input().split())

    count = 0
    for year in xrange(start_year, end_year + 1):
        for month in xrange(1, 13):
            if month < start_month and year == start_year:
                continue
            if month > end_month and year == end_year:
                break
            if start_day != 1 and month == start_month and year == start_year:
                continue
            h = 0
            m = month
            d = 1
            y = year
            if month < 3:
                m += 12
                y -= 1
            k = y%100
            j = y/100
            h += d + (13 * m + 13) / 5 + k + k / 4 + j / 4 + 5* j
            h %= 7
            if h == 1:
                count += 1
    print count
