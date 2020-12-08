import json
sampleJson = {"id" : 1, "name" : "value2", "age" : 29}


with open('file.xt', 'w') as f_obj:
    json.dump(sampleJson, f_obj, indent=4, sort_keys=True)
