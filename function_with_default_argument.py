#This is funtion with default argument in python
def fun(a=0, b=0, c=10):     #declaring the function
    return a+b+c

print(fun(1,2,3))            #printiing with define argument
print(fun())                 #printing with default argument
print(fun(1,2))              #printing with c default argument