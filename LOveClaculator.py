from re import U


name1 = input("Enter your name \n")
name2 = input("Enter your lovers name \n")

combined_name  = name1 + name2
lower_case_string = combined_name.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u +e
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)

int_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print("You go like coke and mentos ")
elif (love_score >= 40) and (love_score <= 50) :
    print(f"Your score is {love_score} , you are alright together ")

print(love_score)