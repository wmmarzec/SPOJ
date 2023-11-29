import sys

try:
    for lines in sys.stdin:
        str = ""
        
        for j in lines:
            str += j.upper()
            

        letter_to_alphabet_morse = {'\n':'','A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'.-..', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'..-.', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', ' ':'/'}

        result = ""

        for i in range (0, len(str)-1):
            if str[i] == " ":
                result += letter_to_alphabet_morse[str[i]]
            else:
                result += letter_to_alphabet_morse[str[i]] + '/'

        print (result)

except:
    sys.exit(0)