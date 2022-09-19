# initializing the string
test_str = 'geeksforgeeks!!$is the best 4 all geeks 10-0'

# printing the original string
print("The original string is = " + str(test_str))

# isalpha() to computation of alphabets
res = len([ele for ele in test_str if ele.isalpha()])

# printing the result
print("Count of alphabets = " + str(res))
