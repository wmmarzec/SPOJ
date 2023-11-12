import sys

try:

    n = input()
    for i in range (0, int(n)):
        my_string = input()
        lenght = len(my_string)
        if lenght % 2 == 0:
            new_lenght = int(lenght / 2) 
            result = ""
            for j in range (0, new_lenght):
                result += my_string[j]
            print (result)
            
except:
    sys.exit(0)
