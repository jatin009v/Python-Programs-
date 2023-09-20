# Sample dictionary with lists as values
my_dict = {'a': [1, 2, 3], 'b': [4, 5], 'c': [6, 7, 8, 9]}

# Initialize a count variable
count = 0

# Iterate through the values of the dictionary
for value in my_dict.values():
    if isinstance(value, list):  # Check if the value is a list
        count += len(value)

print("Total number of items in lists within the dictionary:", count)
