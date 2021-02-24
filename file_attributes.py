# This is file attributes in python
# reading the file
f = open('sample.txt','r')
print(f.writable())
print(f.readable())
print(f.mode)
print(f.closed)
f.close()
print(f.closed)