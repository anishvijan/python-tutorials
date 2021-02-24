# This is multiple inheritence of class in python
class A:                            #declaring class A
    var = 10
    def introA(self):
        return 'method of class A'

class B():                          #declaring class B
    def introB(self):
        return 'method of class B'

class C(A,B):                       #Inheriting class A,B in C
    def introC(self):
        return 'method of class C'

c = C()                             #creating object for class C
print(c.var)
print(c.introA())
print(c.introB())
print(c.introC())