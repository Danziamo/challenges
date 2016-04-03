import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        wines, word = test.rstrip().split('|')
        wines = wines.strip().split()
        l = []
        for wine in wines:
            r = [0]*26
            for i in wine.lower():
                r[ord(i) - ord('a')] += 1
            l.append(r)
        s = ""
        word = word.strip()
        index = 0
        for i in l:
            b = True
            for j in word:
                if i[ord(j) - ord('a')] > 0:
                    i[ord(j) - ord('a')] -= 1
                else:
                    b = False
                    break
            if b:
                s += wines[index] + ' '
            index += 1
        print s.rstrip() if len(s) > 0 else 'False'