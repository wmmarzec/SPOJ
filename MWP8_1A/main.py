import sys

try:

    def nwd(a, b):
        while b:
            a, b = b, a%b
        return a

    n = input()
    numbers = input().split()

    for i in numbers:
        current_number = int(i)
        result = ""
        for j in numbers:
            num = int(j)
            bla = nwd(current_number, num)
            result += str(bla) + " "
        print (result)

except:
    sys.exit(0)
