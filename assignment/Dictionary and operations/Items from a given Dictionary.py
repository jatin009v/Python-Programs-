# Sample dictionary with empty items
my_dict = {'a': 1, 'b': '', 'c': None, 'd': 0, 'e': 'Hello', 'f': []}

# Drop empty items from the dictionary
filtered_dict = {key: value for key, value in my_dict.items() if value}

print("Dictionary with empty items dropped:")
print(filtered_dict)
