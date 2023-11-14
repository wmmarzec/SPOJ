import sys

try:
    n = input()
    for i in range (0, int(n)):
        input_data = input().split()
        gifted_children = (int(input_data[0])) - 1
        candies = int(input_data[1])
        if gifted_children == 0 or candies % gifted_children != 0:
            print("TAK")
        else:
            print("NIE")

except:
    sys.exit(0)