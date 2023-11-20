import sys

try:
    result = 0
    for i in sys.stdin:
        result += 1
    print (result)
except:
    sys.exit(0)