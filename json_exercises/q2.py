import json
sampleJson = """{"key1": "value1", "key2": "value2"}"""

to_dict = json.loads(sampleJson)
print(to_dict['key2'])
