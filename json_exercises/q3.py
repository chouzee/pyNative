import json

sampleJson = {"key1": "value1", "key2": "value2"}

json_r = json.dumps(sampleJson, indent=2, separators=(",", " = "))
print(json_r)
