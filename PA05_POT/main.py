import sys

n = input()
for i in range(0, int(n)):
    targetNumbers = sys.stdin.readline().split()

    lenght = len(targetNumbers)-1
    
    for j in range (0, lenght):
        sys.stdout.write(targetNumbers[lenght-j])

    print("{}".format(int(result % 10)))
