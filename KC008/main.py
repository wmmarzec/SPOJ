import sys
try:
    all_summed = 0

    for line in sys.stdin:
        numbers = line.split()
        local_sum = 0
        for x in numbers:
            local_sum += int(x)

        all_summed += local_sum
        print (local_sum)

    print (all_summed)

except:
    sys.exit(0)