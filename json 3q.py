# Q.1 Json data ko python object main convert karne ka program likho?
import json
a='{"name": "David", "class": "I", "age": 6}'
b=json.loads(a)
print(b)