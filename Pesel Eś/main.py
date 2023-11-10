import sys
print ("Podaj swój PESEL:")
pesel = input()
if len(pesel) == 11:
    year =  pesel[0] + pesel[1]
    month = pesel[2] + pesel[3]
    day = pesel[4] + pesel[5]
    if int(day) < 32:
        if int(month) > 0 and int(month) < 13:
            year = "19" + pesel[0] + pesel[1]
            print (day + "/" + month + "/" + year)
        elif int(month) > 20 and int(month) < 33:
            year = "20" + pesel[0] + pesel[1]
            month = str((int(month) - 20))
            if len(month) == 1:
                month = "0" + month
            print (day + "/" + month + "/" + year)
        elif int(month) > 80 and int(month) < 93:
            year = "18" + pesel[0] + pesel[1]
            month = str((int(month) - 80))
            if len(month) == 1:
                month = "0" + month
            print (day + "/" + month + "/" + year)
        else:
            print ("Nieprawidłowy format numeru PESEL.")
    else:
            print ("Nieprawidłowy format numeru PESEL.")
        
else:
    print ("Nieprawidłowy format numeru PESEL.")