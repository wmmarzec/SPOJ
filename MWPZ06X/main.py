import sys
try:
    n = input()
    for i in range (0, int(n)):
        d = int(input())
        d *= d
        print (d)
except:
    sys.exit(0)