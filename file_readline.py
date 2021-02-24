# This is file readline in python
# reading the file
f = open('sample.txt','r')
t = f.readlines()
for i in t:
    print(i)
f.close()