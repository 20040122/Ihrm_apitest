import json
def read_ejson(path_filename):
    with open('../data/ihrm_emp.json','r',encoding='utf-8') as f:
        data = json.load(f)
        arr = []
        for i in data:
            arr.append(tuple(i.values()))
        return arr