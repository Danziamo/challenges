dictionary = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
              10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
              17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
              60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety", 100: "Hundred", 1000: "Thousand",
              1000000: "Million", 1000000000: "Billion"}

test_cases = int(raw_input())
for test in xrange(test_cases):
    s = raw_input().rstrip()[::-1]
    if s == '0':
        print 'Zero'
        continue
    s = [s[i:i + 3] for i in xrange(0, len(s), 3)]
    words = []
    for i in xrange(len(s)):
        s[i] = s[i][::-1]

    for i in xrange(len(s)):
        word = []
        num = int(s[i])
        if num / 100 != 0:
            word.append(dictionary[num/100])
            word.append(dictionary[100])
            num %= 100
        if num > 20:
            word.append(dictionary[num-num%10])
            if num % 10 != 0:
                word.append(dictionary[num%10])
        elif num != 0:
            word.append(dictionary[num])
        if i == 1 and int(s[i]) != 0:
            word.append('Thousand')
        elif i == 2 and int(s[i]) != 0:
            word.append('Million')
        elif i == 3 and int(s[i]) != 0:
            word.append('Billion')
        elif i == 4 and int(s[i]) != 9:
            word.append('Trillion')
        if len(word) != 0:
            words.append(' '.join(word).strip())
    words = words[::-1]
    print ' '.join(words).strip()