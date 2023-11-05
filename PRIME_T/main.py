def IsPrime(x):
    
    if(x <= 1):
        print ("NIE")
        return
    

    for i in range(2, int(x/2)+1):
        if(x % i == 0):
            print("NIE")
            return
        
    print ("TAK")
    
    return


n = input()
for i in range(0, int(n)):
    targetNumber = int(input())
    IsPrime(targetNumber)
