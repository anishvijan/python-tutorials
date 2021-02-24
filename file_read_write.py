# This is file read and write in python

#writing the file
f = open('sample.txt','w')
f.write('This is new file\n')
f.write('Python Programming')
f.close()

# reading the file
f = open('sample.txt','r')
t = f.read()
print(t)
f.close()