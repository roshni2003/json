import json
dict1={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
print(json.dumps(dict1, sort_keys=True,indent=4))