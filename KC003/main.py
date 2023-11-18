import sys
try:   
    while True:
        side_lenghts = input().split()
        sum = float(side_lenghts[0])
        longest_side = float(side_lenghts[0])

        for i in range (1, 3):
            sum += float(side_lenghts[i])
            if float(side_lenghts[i]) > longest_side:
                longest_side = float(side_lenghts[i])

        if longest_side < (sum - longest_side):
            print ("1")
        else:
            print("0")
except:
    sys.exit(0)
    