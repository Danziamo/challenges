import sys

with open(sys.argv[1], 'r') as test_cases:
    index = 0
    k = 0
    a = [', yeah!', ', this is crazy, I tell ya.', ', can U believe this?', ', eh?', ', aw yea.', ', yo.', '? No way!',
         '.Awesome!']
    for test in test_cases:
        test = test.strip()
        l = len(test)
        i = 0
        while i < len(test):
            if test[i] in '.!?':
                k += 1
                if k % 2 == 0:
                    test = test[:i] + a[index % 8] + test[i+1:]
                    i += len(a[index % 8])
                    #l += len(a[index % 8]) - 1
                    index += 1
            i += 1
        print test