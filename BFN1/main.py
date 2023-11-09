import sys

def isPalidrome(numbers, lenght):
    for j in (0, lenght):
        if int(numbers[j]) == int(numbers[(lenght-j)]):
            return (numbers, 0)
        else:
            print ("chuj")

n = input()
for i in range(0, int(n)):
    numbers = input()
    lenght = len(numbers)-1
    isPalidrome(numbers, lenght)
    




