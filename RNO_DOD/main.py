import sys

n = input()
for i in range(0, int(n)):
    m = input()
    numbers = sys.stdin.readline().split()
    result = 0

    for k in range (0, len(numbers)):
        result += int(numbers[k])
    print(result)