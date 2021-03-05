import re

varstr = '''The core of extensible programming is defining functions.
            Python allows mandatory and optional arguments, keyword arguments, and 
            even arbitrary argument lists.'''

# patt = re.compile(r'.thon') #will find character before the defined
# patt = re.compile(r'^The') #will verfiy if the string starts with the defnied
# patt = re.compile(r'lists.$') #will verfiy if the string ends with the defnied
# patt = re.compile(r'li*') #will define the location with zero or more occurrances
# patt = re.compile(r'li+') #will define the location with one or more occurrances
# patt = re.compile(r'li{1}') #will define the location with exact occurrances
# patt = re.compile(r'li{1}') #will define the location with exact occurrances
patt = re.compile(r'li|Py') #will define the either or

output = patt.finditer(varstr)
for match in output:
    print(match)
# span defines the location that is the slice
# print(varstr[71:76])  #used to verify for the span it is defined