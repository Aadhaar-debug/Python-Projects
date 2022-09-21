# Alphabets Frequency in String
# Using isalpha() + len()
  
# initializing string
test_str = 'geeksforgeeks !!$ is best 4 all Geeks ';
  
# printing original string
print("The original string is : "; + str(test_str))
  
# isalpha() to computation of Alphabets
res = len([ele for ele in test_str if ele.isalpha()])
  
# printing result
print("Count of Alphabets : "; + str(res))
