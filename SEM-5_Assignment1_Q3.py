#given Dictionary
original_list =[11,45,8,11,23,45,23,45,89,11,89]
 

# Function to count the occurences of number in the given dictionary 
def CountOccurences(original_list):
 
    # Creating an empty dictionary
    freq = {}
    for item in original_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    for key, value in freq.items():
        freq.update({key : value})
    print(freq)
 
# Driver function

CountOccurences(original_list)
