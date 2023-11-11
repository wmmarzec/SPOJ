import sys
myList = input().split()

def isSorted(myList):
    for i in range (0, len(myList)-1):
        if myList[i] > myList[i+1]:
            return False
    return True
            
while (isSorted(myList) == False):
    for i in range (0, len(myList)-1):
        a = myList[i]
        b = myList[i+1]
        if myList[i] > myList[i+1]:
            myList[i] = b
            myList[i+1] = a

print (myList)
