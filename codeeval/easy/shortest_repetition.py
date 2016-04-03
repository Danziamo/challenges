import sys

with open(sys.argv[1], 'r') as input:
    for row in input:
        row = row.rstrip()
        i = 1
        rep = row[0]
        while i < len(row) and row[i] != row[0]:
            rep += row[i]
            if len(row) % len(rep) == 0 and (len(row) / len(rep))*rep == row:
                break
            i += 1

        print len(rep)