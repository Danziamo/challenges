import sys

with open(sys.argv[1], 'r') as input:
    for row in input:
        row = row.rstrip().lower()
        a = [0]*26
        for i in row:
            if i < 'a' or i > 'z':
                continue
            a[ord(i) - ord('a')] += 1

        a.sort(reverse=True)
        c = 26
        s = 0
        while c > 0 and a[26 - c] > 0:
            s += c*a[26-c]
            c -= 1
        print s