import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        a, b = int(ord(test[0])-ord('a')) + 1, int(test[1])
        s = ""
        if a - 2 > 0 and b - 1 > 0:
            s += chr(a-2 + ord('a')-1) + str(b-1) + " "
        if a - 2 > 0 and b + 1 < 9:
            s += chr(a-2 + ord('a')-1) + str(b+1) + " "
        if a - 1 > 0 and b - 2 > 0:
            s += chr(a - 1 + ord('a') - 1) + str(b - 2) + " "
        if a - 1 > 0 and b + 2 < 9:
            s += chr(a - 1 + ord('a') - 1) + str(b + 2) + " "
        if a + 1 < 9 and b - 2 > 0:
            s += chr(a + 1 + ord('a') - 1) + str(b - 2) + " "
        if a + 1 < 9 and b + 2 < 9:
            s += chr(a + 1 + ord('a') - 1) + str(b + 2) + " "
        if a + 2 < 9 and b - 1 > 0:
            s += chr(a + 2 + ord('a') - 1) + str(b - 1) + " "
        if a + 2 < 9 and b + 1 < 9:
            s += chr(a + 2 + ord('a') - 1) + str(b + 1) + " "
        print s