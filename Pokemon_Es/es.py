import sys;

input = input().split()

shouldBeUpper = False

if(input[0][0].isupper()):
    shouldBeUpper = False
elif(input[0][0].islower()):
    shouldBeUpper = True

for word in input:

    newWord = ""

    startingIndex = 0
    if(word == input[0]): 
        startingIndex = 1
        newWord += word[0]
    else:
        startingIndex = 0
        

    for i in range(startingIndex, len(word)):
        if shouldBeUpper == True:

            newWord += word[i].upper()

            shouldBeUpper = False
        elif shouldBeUpper == False:

            newWord += word[i].lower()

            shouldBeUpper = True

    sys.stdout.write(newWord + " ")
