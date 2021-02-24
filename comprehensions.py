# This is comprehensions in python

#List Comprehension
l = [x for x in range(5)]
print(l)

#Dictionary Comprehension
d = {var:var+3 for var in range(5)}
print(d)

#Set Comprehension
s = {x for x in range(5)}
print(s)

# Generator Comprehension
g = (x for x in range(5))
print(g)