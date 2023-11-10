import sys

def isPalindrome(numbers):
    lenght = len(numbers)-1
    for j in (0, lenght):
        if int(numbers[j]) != int(numbers[(lenght-j)]):
            return False
    return True
    pass

def reverse(numbers):
    lenght = len(numbers)-1
    numbersReversed = ""
    for k in range (0, lenght+1):
        numbersReversed += (numbers[lenght-k])
    return int(numbersReversed)



n = input()
for i in range(0, int(n)):
    numbers = input()
    counter = 0

    if isPalindrome(numbers):
        print (numbers, 0)
    else:
        while isPalindrome(numbers) == False:
            numbers = int(numbers) + reverse(numbers)
            numbers = str(numbers)
            counter += 1
        print (numbers, counter)






