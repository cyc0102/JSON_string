import json
# a Python object (dict)
x = {"timestamp": 1568287902, "recognized": ["Jackie Chan", "Jet Li"]}
# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

