my_input = input()
text_string = ""
text_string += my_input
text_list = []
for x in text_string:
    text_list.extend(x)
result = ""
result += text_list[0]
lenght = len(text_list)
for i in range (0, lenght-1):
    if text_list[i] != " ":
        if text_list[i+1] != " ":
            if text_list[i] == text_list[i].upper():
                text_list[i+1] = text_list[i+1].lower()
                result += text_list[i+1]
            else:
                text_list[i+1] = text_list[i+1].upper()
                result += text_list[i+1]
        else:
            if text_list[i] == text_list[i].upper():
                text_list[i+2] = text_list[i+2].lower()
                result += text_list[i+1]
                result += text_list[i+2]
            else:
                text_list[i+2] = text_list[i+2].upper()
                result += text_list[i+1]
                result += text_list[i+2]
print (result)

