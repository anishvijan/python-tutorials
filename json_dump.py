import json
var = {'name':'python', 'age' : 20, 'version':['3.8.4','3.9.1','3.9.2']}

varJSON = json.dumps(var, indent=4)
print(varJSON)

with open('varJSON.json','w') as file:
    json.dump(var,file,indent=4)