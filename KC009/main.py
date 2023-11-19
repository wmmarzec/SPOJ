import sys
try:

    while True:
        text = input()
        text_backwards = ""
        lenght = len(text)-1
        for i in range (0, lenght+1):
            text_backwards += (text[lenght-i])
        print(text_backwards)

except:
    sys.exit(0)
