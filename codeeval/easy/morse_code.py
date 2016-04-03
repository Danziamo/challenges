import sys

def getLetter(code):
    if code == '.-':
        return 'A'
    if code == '-...':
        return 'B'
    if code == '-.-.':
        return 'C'
    if code == '-..':
        return 'D'
    if code == '.':
        return 'E'
    if code == '..-.':
        return 'F'
    if code == '--.':
        return 'G'
    if code == '....':
        return 'H'
    if code == '..':
        return 'I'
    if code == '.---':
        return 'J'
    if code == '-.-':
        return 'K'
    if code == '.-..':
        return 'L'
    if code == '--':
        return 'M'
    if code == '-.':
        return 'N'
    if code == '---':
        return 'O'
    if code == '.--.':
        return 'P'
    if code == '--.-':
        return 'Q'
    if code == '.-.':
        return 'R'
    if code == '...':
        return 'S'
    if code == '-':
        return 'T'
    if code == '..-':
        return 'U'
    if code == '...-':
        return 'V'
    if code == '.--':
        return 'W'
    if code == '-..-':
        return 'X'
    if code == '-.--':
        return 'Y'
    if code == '--..':
        return 'Z'
    if code == '-----':
        return '0'
    if code == '.----':
        return '1'
    if code == '..---':
        return '2'
    if code == '...--':
        return '3'
    if code == '....-':
        return '4'
    if code == '.....':
        return '5'
    if code == '-....':
        return '6'
    if code == '--...':
        return '7'
    if code == '---..':
        return '8'
    if code == '----.':
        return '9'

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        row = test.rstrip().split('  ')
        for i in row:
            a = i.split()
            for j in a:
                sys.stdout.write(getLetter(j))
            sys.stdout.write(' ')
        print
