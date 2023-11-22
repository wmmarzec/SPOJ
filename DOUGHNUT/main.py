import sys

try:

    n = input()

    for i in range (0, int(n)):
        data = input().split()

        cats = int(data[0])
        capacity = int(data[1])
        doughnut_weight = int(data[2])

        if capacity >= cats * doughnut_weight:
            print ("yes")
        else: 
            print ("no")

except:
    sys.exit(0)