my_dict = {'key1': 'value1', 'key2': 'value2'}
# print(my_dict['key1']) # value1

prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
# print(prices_lookup['apple']) # 2.99

d = {'k1': 123, 'k2': [0,1,2], 'k3': {'insideKey': 100}}
# print(d['k2']) # [0, 1, 2]
# print(d['k2'][2]) # 2
# print(d['k3']['insideKey']) # 100

d = {'key1': ['a','b','c']}
my_list = d['key1'] # ['a','b','c']
letter = my_list[2] # 'c'
letter.upper() # 'C'
d['key1'][2].upper() # 'C'

d = {'k1': 100, 'k2': 200}
d['k3'] = 300 # Add a new key value pair
# print(d) # {'k1': 100, 'k2': 200, 'k3': 300}
d['k1'] = 'New Value' # Assign new value to an existing key
# print(d) # {'k1': 'New Value', 'k2': 200, 'k3': 300}

d = {'k1': 100, 'k2': 200, 'k3': 300}
# print(d.keys()) # dict_keys(['k1', 'k2', 'k3'])
# print(d.values()) # dict_values([100, 200, 300])
# print(d.items()) # dict_items([('k1', 100), ('k2', 200), ('k3', 300)])