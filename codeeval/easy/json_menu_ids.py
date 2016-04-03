import sys
import json

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if len(test.rstrip()) == 0:
            continue
        data = json.loads(test.rstrip())
        s = 0
        for i in data['menu']['items']:
            if i is not None and 'label' in i:
                s += i['id']
        print s