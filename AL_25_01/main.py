import sys

try:

    data = input().split()
    spaces = input().split()

    result = "NIGDY"
    current_reflection = 0

    for i in range (0, len(spaces)):
        if spaces[i] == data[2]:
            current_reflection += 1
            if current_reflection == int(data[1]):
                result = i
                break

    print (result)

except:
    sys.exit(0)