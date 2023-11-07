import sys

n = input()
for i in range(0, int(n)):
    numbers = sys.stdin.readline().split()

    a = int(numbers[0])
    b = int(numbers[1])

    while b:
        a, b = b, a%b
    print (a)

