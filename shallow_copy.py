# This is shallow copy in python

# Case 1
l1 = [1,2,3,4]
l2 = l1
l2[0] = 4       #changing value without shallow copy
print(l1)       
print(l2)       #changes in both l1 and l2 will be observed

# Case 2
import copy
l1 = [1,2,3,4]
l2 = l1.copy()
l2[0] = 4       #changing value with shallow copy
print(l1)       
print(l2)       #changes in only l2 and not in l1 will be observed

# Case 3
l1 = [1,[2,3,4],3,4]
l2 = l1.copy()
l2[1][0] = 4       #changing value with shallow copy
print(l1)       
print(l2)       #changes in both l1 and l2 will be observed for this we need to use deep copy

