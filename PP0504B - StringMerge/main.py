import sys

def getShorter(list1, list2):
    if len(list1) < len(list2):
        return list1
    else:
        return list2


n = input()
for i in range(0, int(n)):
    myList = input().split()
    list1 = myList[0]
    list2 = myList[1]
    result = []


    for j in range(0, len(getShorter(list1, list2))):
        result += list1[j] + list2[j]

    print (*result, sep='')