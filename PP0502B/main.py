import sys

try:

    n = input()
    for i in range(0, int(n)):
        myList = sys.stdin.readline().split()
        lenght = len(myList)-1
        for j in range(0, lenght):
            sys.stdout.write(myList[lenght-j] + " ")
        print()


except:
    sys.exit(0)
