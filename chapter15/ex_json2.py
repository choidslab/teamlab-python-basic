import json

dict_data = {'Name': 'Dooseop', 'Age': 33, 'Class': 'First Calass'}
with open('data.json', 'w') as f:
    json.dump(dict_data, f)
