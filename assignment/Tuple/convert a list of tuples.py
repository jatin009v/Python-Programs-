# Define a list of tuples
list_of_tuples = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

# Initialize an empty dictionary
my_dict = {}

# Convert the list of tuples into a dictionary
for key, value in list_of_tuples:
    my_dict[key] = value

# Print the dictionary
print("Dictionary from List of Tuples:")
print(my_dict)
