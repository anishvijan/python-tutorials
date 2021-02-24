# This is multilevel inheritence of class in python
class A:                            #declaring class A
    var = 10
    def introA(self):
        return 'method of class A'

class B(A):                         #inheriting class A in class B
    def introB(self):
        return 'method of class B'

class C(B):                         #inheriting class B in class C
    def introC(self):
        return 'method of class C'

c = C()
print(c.var)
print(c.introA())
print(c.introB())
print(c.introC())