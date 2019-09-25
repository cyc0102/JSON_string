import json
import time
import calendar
names = ["Unknown","Jackie Chan","Jet Li","zoe","Unknown"]
locations = [(1,2),(3,4),(5,6),(7,8)]
recognized_dic = {"Jacke Chan":(3,4),"Jet Li":(5,6),"Unknown": [(1,2),(7,8)]}
# a Python object (dict)
x = {"timestamp":  calendar.timegm(time.gmtime()) ,"recognized": recognized_dic}
# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

