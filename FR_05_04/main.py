import sys
try:

    n = input()
    data = []
    for i in range (0, int(n)):
        contestant_data = input().split()
        data.append(contestant_data)
        times = []

    for j in data:
        time = j[2].split(":")
        minutes_to_hour = float(time[1]) / 60
        time_in_hours = float(time[0]) + minutes_to_hour
        times.append(time_in_hours)

    current_best = times[0]
    current_best_index = []

    for k in range (1, len(times)):
        if times[k] < current_best:
            current_best = times[k]
            current_best_index = str(k)
        elif times[k] == current_best:
            current_best_index += str(k)

    for l in current_best_index:
        print(data[int(l)][0], data[int(l)][1])

except:
    sys.exit(0)