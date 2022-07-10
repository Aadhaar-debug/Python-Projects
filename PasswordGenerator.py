import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['~','!','@','#','$','%','^','&','*','(',')','_','+',]

print("Welcome to the password generator")

no_letters = int(input("Enter the number of letters you want in the passsword\n"))
no_symbols = int(input("Enter the number of symbols you want in the passsword\n"))
nu_numbers = int(input("Enter the number of numbers you want in the passsword\n"))

password = ""

for char in range(1,no_letters + 1) :
    password += random.choice(letters)

for char in range(1,no_letters + 1) :
    password += random.choice(symbols)

for char in range(1,no_letters + 1) :
    password += random.choice(numbers)

print("\nYour password is")
print(password)