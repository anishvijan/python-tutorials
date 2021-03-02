import json
var = {'name':'python', 'age' : 20, 'version':['3.8.4','3.9.1','3.9.2']}

varJSON = json.dumps(var, indent=4)

rev = json.loads(varJSON)
print(rev)

with open('varJSON.json','r') as file:
    text = json.load(file)
    print(text)
