n = input()
for i in range (0, int(n)):
    data = input()
    
    cachedOperation = "dupa"
    cachedNumber = 0
    result = int(data[0])


    for j in range (1, len(data)-1, 2):


        if data[j].isnumeric() == True:
            cachedNumber = int(data[j])
            cachedOperation = data[j+1]
        else:
            cachedNumber = int(data[j+1])
            cachedOperation = data[j]


        if cachedOperation == "+":
            result += cachedNumber
        else:
            result -= cachedNumber


    print (result)

        
        
