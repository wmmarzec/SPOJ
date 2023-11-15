import sys
try:
    n = input()
    for i in range(0, int(n)):
        pesel = input()
        first = int(pesel[0])
        second = int(pesel[1]) * 3
        third = int(pesel[2]) * 7
        fourth = int(pesel[3]) * 9
        fifth = int(pesel[4])
        sixth = int(pesel[5]) * 3
        seventh = int(pesel[6]) * 7
        eighth = int(pesel[7]) * 9
        ninth = int(pesel[8])
        tenth = int(pesel[9]) * 3
        eleventh = int(pesel[10])
        sum = first + second + third + fourth + fifth + sixth + seventh + eighth + ninth + tenth + eleventh
        sum = list(str(sum))
        last_index = len(sum)-1
        if int(sum[last_index]) == 0:
            print ("D")
        else: 
            print ("N")
except:
    sys.exit(0)