n = input()
numbers = []
for i in range (0, int(n)):
    city = input()
    numbers.append(city)
current_biggest = 0
current_biggest_backwards = 0
indexes = []
indexes_backwards = []
for j in range(0, len(numbers)):
        if int(numbers[j]) + current_biggest > 0:
            current_biggest += int(numbers[j])
            indexes += str(j)
        else:
             indexes = []
             current_biggest = 0
for k in reversed(range(0, len(numbers))):
        if int(numbers[k]) + current_biggest_backwards > 0:
            current_biggest_backwards += int(numbers[k])
            indexes_backwards += str(k)
        else:
             indexes_backwards = []
             current_biggest_backwards = 0
profit_indexes = []
for l in indexes:
     for m in indexes_backwards:
          if l == m:
             profit_indexes.extend(l)  
               
result = 0
for m in profit_indexes:
     m = int(m)
     result += int(numbers[m])
print(result)
