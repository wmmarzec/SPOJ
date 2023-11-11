import sys

result = 0

try:

    while True:
        result += int(input())
        print(result)

except:
    sys.exit(0)