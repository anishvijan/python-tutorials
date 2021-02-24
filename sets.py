# This is set in python
s1 = {1,2,3,1,2,3,1,2,3}    #declaring set
print(s1)

s2 = {3,4,5,2,6}            #declaring set
print(s2)

# Accessing Values in sets
for f in s1:
    print(f)

# Updating the set
s1.add(10)
print(s1)
s1.update([10,11,12,13])
print(s1)

# In Built function
print(s1.intersection(s2))
print(s1.union(s2))
print(s1.difference(s2))
s1.remove(15)
print(s1)
