# This is dictionary in python
d = {'p':'python', 'l':'language'}  #declaring dictionary
print(d)

print(d['l'])                       #accessing values

d['p']='programing'
print(d)

#in Built Function
print(d.keys())
print(d.values())
print(d.get('a', 'No Value'))
del d['p']
print(d)