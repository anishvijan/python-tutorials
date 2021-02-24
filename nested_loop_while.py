# this is nested while-loop in python
i = 0                           #initialize outer loop
while i<5:                      #condition outer loop
    j = 0                       #initialize inner loop
    while j<5:                  #condition inner loop
        print('*',end = '')     #printing star accordingly where 'end' is used ti print in one line
        j+=1                    #increment inner loop
    print()                     #make statement after inner loop to print tin next line
    i+=1                        #increment outer loop