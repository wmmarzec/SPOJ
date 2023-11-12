import sys

try:
    while True:
        my_input = input().split()
        operation = my_input[0]
        a = int(my_input[1])
        b = int(my_input[2])
        result = 0
        if operation == "+":
            result = int(a + b)
        elif operation == "-":
            result = int(a - b)
        elif operation == "*":
            result = int(a * b)
        elif operation == "/":
            result = int(a / b)
        elif operation == "%":
            result = int(a % b)
        else:
            result = "ERROR"

        print (result)
        

except:
    sys.exit(0)