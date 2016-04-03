import sys

with open(sys.argv[1], 'r') as input:
    for row in input:
        row = row.rstrip()
        a = row[:row.find('.')]
        b = row[row.find('.'):]
        n = float(b)*3600
        minutes = int(n/60)
        seconds = int(n - 60*minutes)
        print "%s.%02d'%02d\"" % (a, minutes, seconds,)