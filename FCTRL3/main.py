import sys

try:

    n = input()
    for i in range(0, int(n)):
        targetNumber = int(input())

        factorial = 1
        
        if targetNumber >= 2 and targetNumber < 10:
            for j in range(2, targetNumber+1):
                factorial *= j

        if(targetNumber > 9):
            print(0, 0)
        else:
            print("{} {}".format((int((factorial%100)/10)), int(factorial % 10)))

except:
    sys.exit(0)
