import sys

try:
    def is_uppercase_letter(x):
        if x.isupper():
            return True
        else:
            return False
        
    def is_lowercase_letter(x):
        if len(x) > 2:
            text = x[1:len(x)-1]
            if text.isalpha():
                return True
            else:
                return False
        else:
            return True

    def is_date_correct(x):
        year = x[0:4]
        month = x[5:7]
        day = x[8:10]
        if 1900 <= int(year) <= 2000 and 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
            return True
        else:
            return False
        

    for i in sys.stdin:
        line = i.split()
        name = line[1]
        surname = line[3]
        date = line[6]
        if is_uppercase_letter(name[0]) == False or is_lowercase_letter(name) == False:
            print (0)
        elif is_uppercase_letter(surname[0]) == False or is_lowercase_letter(surname) == False:
            print (1)
        elif is_date_correct(date) == False:
            print (2)
        else:
            print (3)
except:
    sys.exit(0)
       