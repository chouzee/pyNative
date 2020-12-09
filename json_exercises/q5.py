import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


json_r = json.loads(sampleJson)
print(json_r["company"]["employee"]["payble"]["salary"])
