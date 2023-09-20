# Sample dictionary with duplicate keys
my_dict = {'a': 1, 'b': 2, 'a': 3, 'c': 4, 'b': 5}

# Create a new dictionary without duplicates
unique_dict = {}
for key, value in my_dict.items():
    unique_dict[key] = value

print(unique_dict)
