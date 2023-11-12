import sys

try: 
    n = input()
    for i in range (0, int(n)):
        input_numbers = input().split()
        my_numbers = input_numbers[1:len(input_numbers)]

        lenght = len(my_numbers)-1
        numbersReversed = ""
        for k in range (0, lenght+1):
            numbersReversed += (my_numbers[lenght-k]) + " "
        print (numbersReversed)

except:
    sys.exit(0)