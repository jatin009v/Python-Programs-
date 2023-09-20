# Sample dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'd': 4, 'e': 5}

# Find matching key-values in the two dictionaries
matching_key_values = {}

for key, value in dict1.items():
    if key in dict2 and dict2[key] == value:
        matching_key_values[key] = value

print("Matching key-values in the two dictionaries:")
print(matching_key_values)
