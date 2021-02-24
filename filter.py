# This is filter in python

l = [1,2,3,4,5]                         #declaring iterable

f1 = filter(lambda x : x % 2 == 0 , l)  #filter using lambda function
print(list(f1))                         #print using list

def fun(a):                             #declaring function
    if a%2==0:
        return True
    else:
        return False

f2 = filter(fun , l)                    #filter using function
print(list(f2))                         #print using list