import json
import time
names = ['Jackie Chan','Jet Li','zoe']
# a Python object (dict)
x = {"timestamp":  time.time(),"recognized": names}
# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

