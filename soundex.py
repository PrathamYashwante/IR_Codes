def gen_soundex(token):
    token = token.upper()
    soundex = token[0]

    soundex_dict = {
        "BFPV": "1", "CGJKQSXZ": "2",
        "DT": "3", "L": "4", "MN": "5",
        "R": "6", "AEIOUHWY": "."
    }

    for char in token[1:]:
        code = ''

        for key, value in soundex_dict.items():
            if char in key:
                code = value
                break

        if code != '.' and code != soundex[-1]:
            soundex += code

    soundex = soundex.ljust(4, "0")

    return soundex



print(gen_soundex('Pratham'))  
print(gen_soundex('Pratam')) 
