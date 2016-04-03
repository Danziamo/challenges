import sys

calendar = {'Jan': 0,
       'Feb': 1,
       'Mar': 2,
       'Apr': 3,
       'May': 4,
       'Jun': 5,
       'Jul': 6,
       'Aug': 7,
       'Sep': 8,
       'Oct': 9,
       'Nov': 10,
       'Dec': 11
            }

with open(sys.argv[1], 'r') as input:
    for row in input:
        row = row.rstrip().split(';')
        a = [0]*31*12
        for i in row:
            e = i.split('-')
            m1,y1 = e[0].split()
            m2,y2 = e[1].split()
            start = calendar[m1] + 12*(int(y1)-1990)
            stop = calendar[m2] + 12*(int(y2)-1990)
            for j in range(start, stop + 1):
                a[j] = 1

        c = 0
        for j in range(0, 12*31):
            if a[j] > 0:
                c += 1
        print c/12