# This is single inheritence of class in python
class A:                            #declaring class A
    var = 10
    def introA(self):
        return 'method of class A'

class B(A):                         #inheriting class A in class B
    def introB(self):
        return 'method of class B'
b = B()
print(b.var)
print(b.introA())
print(b.introB())