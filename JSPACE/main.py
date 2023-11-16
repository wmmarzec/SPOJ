import sys
try:

    while True:
        text = input().split()
        new_text = ""
        for i in range (0, len(text)):
            if i > 0:
                new_text += text[i].capitalize()
            else:
                new_text += text[i]
        print(new_text)

except:
    sys.exit(0)