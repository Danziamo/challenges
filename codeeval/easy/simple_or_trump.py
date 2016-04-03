import sys

with open(sys.argv[1], 'r') as input:
    for row in input:
        list = row.rstrip().split('|')
        c = list[1]
        a, b = list[0].split()
        a1 = a.replace('10', ':').replace('J', 'B').replace('Q', 'C').replace('K', 'D').replace('A', 'E')
        b1 = b.replace('10', ':').replace('J', 'B').replace('Q', 'C').replace('K', 'D').replace('A', 'E')
        if b1[-1] == c[-1] and a1[-1] == c[-1]:
            if b1[0] > a1[0]:
                print b
            elif b1[0] < a1[0]:
                print a
            else:
                print a, b
        elif b1[-1] == c[-1]:
            print b
        elif a1[-1] == c[-1]:
            print a
        else:
            if b1[0] > a1[0]:
                print b
            elif b1[0] < a1[0]:
                print a
            else:
                print a, b