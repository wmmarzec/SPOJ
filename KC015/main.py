import sys

try:

    for lines in sys.stdin:
        line = lines.split()
        first_number = int(line[0])
        second_number = int(line[2])
        if line[1] == "==":
            if first_number == second_number:
                print(1)
            else:
                print(0)
        elif line[1] == "!=":
            if first_number != second_number:
                print(1)
            else:
                print(0)
        elif line[1] == ">=":
            if first_number >= second_number:
                print(1)
            else:
                print(0)
        elif line[1] == "<=":
            if first_number <= second_number:
                print(1)
            else:
                print(0)
except:
    sys.exit(0)