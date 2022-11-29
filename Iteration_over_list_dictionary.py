'''
QUESTION : 
Write a program to  illustrate iteration over the list and dictionary
'''
# list = ["AADHAAR" , "ELON" , "JEFF" , "BILL" , "WARREN"]
list = [1,2,3,4,5,6,7,8,9,0]
thisdict = { "brand": "Ford","model": "Mustang","year": 1964}

for i in list:
    print(list[i])

print("------End of the list contents------")


for j in thisdict:
    print(thisdict[j])

print("------End of the Dictionary values------")
