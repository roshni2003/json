import json
dict = '{"a":  1,"a":  2,"a":  3, "a": 4,   "b": 1, "b": 2}'
print("Original key:")
print(dict)
json1 = json.loads(dict)
print("\nUnique Key :")
print(json1) 