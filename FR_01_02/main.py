import sys

try: 
    def get_NWD(a,b):
        while b:
            a, b = b, a%b
        return a

    def get_NWW(a,b):
        NWW = a*b/get_NWD(a,b)
        return NWW

    for lines in sys.stdin:
        line = lines.split()
        first_number = line[0].split('/')
        first_numerator = int(first_number[0])
        first_denominator = int(first_number[1])
        second_number = line[1].split('/')
        second_numerator = int(second_number[0])
        second_denominator = int(second_number[1])

        common_denominator = int(get_NWW(first_denominator, second_denominator))
        
        first_numerator = first_numerator * (common_denominator/first_denominator)
        second_numerator = second_numerator * (common_denominator/second_denominator)
        summed_numerator = int(first_numerator + second_numerator)

        NWD = int(get_NWD(summed_numerator,common_denominator))
        if NWD > 1:
            summed_numerator = int(summed_numerator/NWD)
            common_denominator = int(common_denominator/NWD)

        result = ""
        result += str(summed_numerator) + "/" + str(common_denominator)
        
        print(line[0], "+", line[1], "=", result)

except:
    sys.exit(0)