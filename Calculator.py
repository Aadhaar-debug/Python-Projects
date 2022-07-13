from __future__ import division


def addition() :
    a = int(input("Enter the first number"))
    b = int(input("Enter the second number"))
    result = a + b
    print(result)

def subtraction() :
    a = int(input("Enter the first number"))
    b = int(input("Enter the second number"))
    result = a - b
    print(result)

def Multiplication() :
    a = int(input("Enter the first number"))
    b = int(input("Enter the second number"))
    result = a * b
    print(result)

def division() :
    a = int(input("Enter the first number"))
    b = int(input("Enter the second number"))
    result = a / b
    print(result)


print("Welcome to the calculator app .")
operation = input("Enter what operation you want to perform ")

if operation == "*" :
    Multiplication()
if operation == "+" :
    addition()
if operation == "-" :
    subtraction()
if operation == "/" :
    division()
