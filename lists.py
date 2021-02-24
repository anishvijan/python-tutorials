# This is list in python 
l1 = [1,2,5,3,7]
l2 = [8,10,9,6]

print(type(l1))

#accessing value in string
print(l1[3])        #accessing single value
print(l1[1:4])      #accessing multiple values
print(l1[-1])       #accessing last value

#updating
l2[2] = 17
print(l2)

#appending and extending
l1.append(20)       #used to append single value and inccreses the length by 1
print(l1)   
l1.extend(l2)       #used to append mutiple value like value in other datatype and increse len to len1+len2

#In Built Function
l1.sort()
print(l1)
print(max(l1))
print(min(l1))
l1.remove(20)
print(l1)
del l1[0]
print(l1)