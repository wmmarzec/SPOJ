import sys
try:
    def get_cipher_letter (a):
        letter_ascii = int(ord(a))
        if 87 < letter_ascii < 91 or 119 < letter_ascii < 123:
            letter_ascii -= 26
            cipher_letter_ascii = letter_ascii + 3
            cipher_letter = chr(cipher_letter_ascii)
        else:
            cipher_letter_ascii = letter_ascii + 3
            cipher_letter = chr(cipher_letter_ascii)

        return cipher_letter
        

    for lines in sys.stdin:
        line = ""
        for j in lines:
            line += j

        cipher_line = ""

        for j in line:
            if j != " ":
                cipher_line += get_cipher_letter (j)
            else:
                cipher_line += j

        print (cipher_line)
       
except:
    sys.exit(0)
