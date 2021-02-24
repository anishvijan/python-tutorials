# This is **kwargs in python
def fun(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

fun(a=1,b=2)