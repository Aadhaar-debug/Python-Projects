# optional dictionary
dict = {'Bill': '21', 'Elon': '34'}

# Assigning the new values
name = 'jason'
value = 21

print(" ")
print("Current Dict is:", dict)
 
print(" ")
print("Updating the dictionary with another key value pair")


# Function to add value
def add_value(dict , name , value):
    dict.update({name : value})

add_value(dict , name , value)

print("Updated Dict is: ", dict)
print(" ")
