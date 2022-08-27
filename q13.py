symbol_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000    
}

def isBiggerOrEqual(ch1, ch2):
    match ch1:
        case 'I':
            if ch2 == 'I':
                return True
        case 'V':
            if ch2 in set(['I', 'V']):
                return True
        case 'X':
            if ch2 in set(['I', 'V', 'X']):
                return True
        case 'L':
            if ch2 in set(['I', 'V', 'X', 'L']):
                return True
        case 'C':
            if ch2 in set(['I', 'V', 'X', 'L', 'C']):
                return True
        case 'D':
            if ch2 in set(['I', 'V', 'X', 'L', 'C', 'D']):
                return True
        case 'M':
            if ch2 in set(['I', 'V', 'X', 'L', 'C', 'D', 'M']):
                return True
    return False

def romanToInt(s):
    sum = 0
    for i in range(0, len(s) - 1):
        ch = s[i:i+2]
        if isBiggerOrEqual(ch[0], ch[1]):
            sum += symbol_map[ch[0]]
        else:
            sum -= symbol_map[ch[0]]
    sum += symbol_map[s[-1]]
    return sum


print(romanToInt("DCXXI"))

