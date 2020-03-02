"""
json 파일은 읽은 후, dict type으로 처리하면 됨!
"""

import json

with open('json_example.json', 'r', encoding='utf-8') as f:
    contents = f.read()
    json_data = json.loads(contents)
    print(json_data)
    print(json_data['employees'])
    print(json_data['employees'][0])
    print(json_data['employees'][1])
    print(json_data['employees'][2])
    print(json_data['employees'][0]['firstName'])
    emp1 = json_data['employees'][0]
    print(emp1['firstName'])

