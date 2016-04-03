import sys

with open(sys.argv[1], 'r') as input:
    for row in input:
        countries = row.rstrip().split('|')
        fans = {}
        counter = 0
        for country in countries:
            counter += 1
            clubs = country.split()
            for c in clubs:
                club = int(c)
                if not fans.has_key(club):
                    fans.update({club: [str(counter)]})
                else:
                    list = fans.get(club)
                    list.append(str(counter))
                    fans.update({club: list})

        result = ""
        for k in sorted(fans):
            result += str(k) + ":" + ','.join(fans.get(k)) + "; "
        print result.rstrip()
