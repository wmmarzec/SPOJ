import sys
try:
    while True:
        numbers = input().split()
        wanted = numbers[0]
        occurrence = 0
        for i in range (2, len(numbers)):
            if numbers[i] == wanted:
                occurrence += 1
        print(occurrence)
except:
    sys.exit(0)