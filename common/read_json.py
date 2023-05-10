import json
def read_json(path_filename):
    with open(path_filename,'r',encoding='utf-8') as f:
        data = json.load(f)
        arrs = []
        for i in data:
            arrs.append(tuple(i.values()))
        return arrs
