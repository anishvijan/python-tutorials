# This is init of class in python
class A:                #declaring class A
    var = 10            #defining variable
    def __init__(self):
        print('this method will always be executed')
    def intro(self):    #defining method
        return 'this is method/function inside the class'

a = A()                 #creating object for class
print(a.var)
print(a.intro())