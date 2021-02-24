# This is map in python

l = [1,2,3,4,5,6,7,8,9]         #declaring the interable

m1 = map(lambda x : x+3 , l)    #creating map with lambda function
print(list(m1))                 #pritning in list format

def fun(a):                     #creating function
    return a+3

m2 = map(fun , l)               #creating map with function
print(list(m2))                 #printing in list format