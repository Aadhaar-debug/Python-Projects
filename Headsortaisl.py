import random

choice = int(input("What do you choose ? 1 for H or 0 for T"))
a = random.randint(0,1)
if choice == a :
    print("Yay ! You win")
else :
    print("AWW , You loose")