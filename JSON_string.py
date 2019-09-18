import json
import time
import calendar
names = ['Unknown','Jackie Chan','Jet Li','zoe','Unknown']
# a Python object (dict)
x = {"timestamp":  calendar.timegm(time.gmtime()) ,"recognized": names}
# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

