n = input()
for i in range (0, int(n)):
    all = input().split()
    lenght = len(all)
    result = 0
    for j in range (0, lenght):
        result += int(all[j])
    if result > 0:
        result += -1
    print (result)