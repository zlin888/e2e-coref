import json

p = []
i = 0

with open('xlnet_features.hdf5', 'r') as f:
    for line in f.readlines():
        dic = json.loads(line)
        print(dic.keys())
        i =+ 1
        if i >= 100:
            break