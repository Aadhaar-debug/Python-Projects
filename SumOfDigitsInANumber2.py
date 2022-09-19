n=int(input("enter : "))
sum=0
r=0
while (n!=0):
    r=n%10
    sum+=r
    n//=10
print(sum)
