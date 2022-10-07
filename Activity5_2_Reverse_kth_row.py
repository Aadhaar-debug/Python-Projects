test_list = [[5,3,2],[8,6,3],[3,5,2],[3,6],[3,7,4],[2,9]]

print("Original list :" , str(test_list))

k = 3

res = [ele[::-1]if(idx+1)%k==0 else ele in enumerate(test_list)]

print("After reversing kth row : " + str(res))
