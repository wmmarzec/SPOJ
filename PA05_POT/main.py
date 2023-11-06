import sys

try:

    n = input()
    for i in range(0, int(n)):
        targetNumbers = sys.stdin.readline().split()

        result = int(targetNumbers[0])
        num = int(targetNumbers[0])
        power = int(targetNumbers[1])

    
        for i in range (2, power+1):
            result *= num

        print("{}".format(int(result % 10)))

except:
    sys.exit(0)