import sys
try:
    n = input()
    for i in range (0, int(n)):
        speeds = input().split()
        speed1 = int(speeds[0])
        speed2 = int(speeds[1])
        

        average_speed = (2 * speed1 * speed2) / (speed1 + speed2)
        print (int(average_speed))

except:
    sys.exit(0)

