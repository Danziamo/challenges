import sys

input = open(sys.argv[1], 'r')

for row in input:
    row = row.rstrip().split(',')
    dict = {}
    max = 0
    key = 'None'
    for i in row:
        if i in dict.keys():
            dict[i] += 1
            if dict[i] > max:
                max = dict[i]
        else:
            dict.update({i: 1})

    if max > int(len(row) * 1.0 / 2):
        key = i
    print key

input.close()