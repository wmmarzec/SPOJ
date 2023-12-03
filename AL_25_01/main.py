

def get_space (current_space, number_of_spaces):
    if current_space > number_of_spaces:
        current_space -= number_of_spaces
    return current_space

data = input().split()
spaces = input().split()

result = "NIGDY"
space = int(data[1])

for i in range (0, len(spaces)):
    space += int(spaces[i])
    current_reflection = get_space(space, int(data[0]))
    space = current_reflection
    print(space)
    if space == data[2]:
        result == space
        break

print (result)
