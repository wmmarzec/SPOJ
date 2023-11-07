import sys

def nwd(a, b):
    while b:
        a, b = b, a%b
    return a

n = input()
for i in range(0, int(n)):
    numbers = sys.stdin.readline().split()

    a = int(numbers[0])
    b = int(numbers[1])
    myNWD = int(nwd(a, b))
    print (a*b//myNWD)

