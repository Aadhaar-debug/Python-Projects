print("Welcome tothe rollercoster ")
height = int(input("What is your height ?"))

if height >= 12:
    print("You can ride the rollercoster ")
    age = int(input("What is your age ?"))
    if age < 12 :
        bill = 5 
        print("Child tickets are 5 dolars ")
    elif age <= 18 :
        bill =7 
        print("Youth tickets are 7 dollars")
    else :
        bill = 12
        print("Adult tickets are 12 dolars")

    wnats_photo = input("Do you want a photo taken ?")
    if wnats_photo == "y" :
        bill += 3
    
    print(f"Your final bill for the rollercoster is equal to {bill}")

else :
    print("Sorry you have to grow taller before you can ride")