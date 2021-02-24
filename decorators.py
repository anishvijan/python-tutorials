# This is decorator in python
def func(fun_to_be_called):
    def inner():
        print('before')
        fun_to_be_called()
        print('after')
    return inner()

def fun_called():
    print('hello I am called function')

f = func(fun_called)
print(f)