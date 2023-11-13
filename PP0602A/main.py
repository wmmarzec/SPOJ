n = input()
for i in range(0, int(n)):
    numbers = input().split()
    lenght = len(numbers)-1
    even = []
    odd = []
    result = []

    for j in range (1, lenght+1):
        if j % 2 == 0:
            even.append(str(numbers[j]))
        else:
            odd.append(str(numbers[j]))

    result += even + odd
    print (*result)