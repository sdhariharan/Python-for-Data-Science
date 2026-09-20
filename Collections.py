from collections import OrderedDict,namedtuple,Counter

data = OrderedDict()

data["a"] = 1
data["b"] = 2
data["c"] = 3
for i in data.keys():
    print(i,":",data[i])
