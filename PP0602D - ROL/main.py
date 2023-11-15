import sys
try:
    first_input = input().split()
    n = first_input[0]
    k = first_input[1]
    list = input().split()
    list_extended = list + list

    for i in range(0, int(n)):
        list[i] = list_extended[i+int(k)]
    print(*list)

except:
    sys.exit(0)