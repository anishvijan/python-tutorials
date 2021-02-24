# This is exception handling in python

try:                                                        #try
    a = 1/0
    print(a)

except ZeroDivisionError:                                   #except
    print('value to be printed is not correct')
else:                                                       #else
    print('this will be executed if not exception occurs')
finally:                                                    #finally
    print('this will always be executed')
