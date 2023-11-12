import sys

try: 
    numbers = input().split()

    lenght = len(numbers)-1
    numbersReversed = ""
    for k in range (0, lenght+1):
        numbersReversed += (numbers[lenght-k]) + " "
    print (numbersReversed)

except:
    sys.exit(0)