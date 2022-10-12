num = 1
col = 5
char = "*"
for i in range(col):
    print(char*num)
    num+=1
    
    
    num = 5
col = 5
char = "*"
for i in range(col):
    print(char*num)
    num-=1
    

rows = 5
for i in range(rows+1):  
    for j in range(i):  
        print(i, end=" ") 
    print(" ")  
