import sys
try:
    num = input()
    for i in range (0, int(num)):
        numbers = input().split()
        n = int(numbers[0])
        x = int(numbers[1])
        y = int(numbers[2])
        result = []
        for j in range (1, int(n)):
            if j % x == 0 and j % y != 0:
                result.append(j)
        print (*result)
except:
    sys.exit(0)