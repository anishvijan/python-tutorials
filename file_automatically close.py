# This is file autommatically close in python
# reading the file
with open('sample.txt','r') as f:   #file open
    t = f.read()
    print(t)
    print(f.closed)

print(f.closed)