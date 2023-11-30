import sys

try:

    n = input()

    for i in range (0, int(n)):
        data = input().split()
        time = []

        for j in range (0, int(data[0])):
            time_in_minutes = int(input())/60
            time.append(time_in_minutes)
        
        cookies = 0

        for k in time:
            cookies_within_day = int(1440/k)
            cookies += cookies_within_day
        
        boxes = 0
        
        if cookies % int(data[1]) == 0:
            boxes = int(cookies / int(data[1]))
        else:
            boxes = int(cookies / int(data[1])) + 1

        print (boxes)

except:
    sys.exit(0)