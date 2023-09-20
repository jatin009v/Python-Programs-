# Sample dictionary
my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# Calculate the average of dictionary values
values = list(my_dict.values())
average = sum(values) / len(values)

# Replace dictionary values with their average
for key in my_dict:
    my_dict[key] = average

print("Dictionary with values replaced by their average:")
print(my_dict)
