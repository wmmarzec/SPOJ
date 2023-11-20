import sys

try:

    for lines in sys.stdin:
        line = lines.split()
        c = (line[0])
        text = line[1]
        result_text = ""

        for i in range (0, len(text)):
            if text[i] != c:
                result_text += text[i]

        print(result_text)

except:
    sys.exit(0)