test_list = [[5,3,2],[8,6,3],[3,5,2],[3,6],[3,7,4],[2,9]]

print("Original list :" , str(test_list))

k = 3

res = []

for idx , ele in element (test_list):
  if(idx+1)%k == 0:
    res.append(list(reversed(ele)))
  else:
    res.append(ele)
  
print("After reversing kth row : " + str(res))
