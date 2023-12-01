import sys

try: 
    n = input()

    for i in range (0, int(n)):
        numbers = input().split()
        result = ""

        for j in range (2, len(numbers)):
            result += numbers[j] + " "

        result += numbers[1]
        print (result)

except:
    sys.exit(0)