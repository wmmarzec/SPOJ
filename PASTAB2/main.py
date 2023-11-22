import sys

try:

    n = int(input())
    numbers = []

    for i in range (0, n):
        line =  input()
        numbers.append(line)

    condition = input().split()
    target_number = condition[1]

    if condition[0] == ">":
        for k in numbers:
            if int(k) > int(target_number):
                    print (k)

    elif condition[0] == "<":
        for k in numbers:
            if int(k) < int(target_number):
                    print (k)

except:
     sys.exit(0)