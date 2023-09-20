# Sample dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

# Create a new dictionary and concatenate the three dictionaries
concatenated_dict = {}
concatenated_dict.update(dict1)
concatenated_dict.update(dict2)
concatenated_dict.update(dict3)

print(concatenated_dict)
