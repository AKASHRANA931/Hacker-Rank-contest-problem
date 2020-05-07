
for i in range(int(input(""))):
    num = int(input(""))
    fact= 1 
    sum1 = 0
    for i in range(1,num + 1):
        fact = fact*i
   
    while(fact!=0):
        n = fact % 10
        sum1 = sum1 + n
        fact = fact // 10
    print(sum1)
            
            