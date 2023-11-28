import sys
try:
    def get_BMI (a, b):
        c = b/100
        BMI = float(a/(c*c))
        
        result = ""
        if BMI < 18.5:
            result = "niedowaga"
        elif BMI >= 25:
            result = "nadwaga"
        else: 
            result = "wartosc prawidlowa"

        return result

            
    n = input()
    underweight = "niedowaga\n"
    overweight = "\nnadwaga\n"
    ok = "\nwartosc prawidlowa\n"
    for i in range (0, int(n)):
        data = input().split()
        result = get_BMI (int(data[1]), int(data[2])) 
        if result == "niedowaga":
            underweight += data[0] + "\n"
        elif result == "nadwaga":
            overweight += data[0] + "\n"
        elif result == "wartosc prawidlowa":
            ok += data[0] + "\n"

    print (underweight, ok, overweight)

except:
    sys.exit(0)
