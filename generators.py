# This is generator in python
def funname():              #defining the function
    for f in range(10):
        yield f

for i in funname():         #printing the values first method
    print(i)

fn = funname()              #printinng the values second method
print(next(fn))