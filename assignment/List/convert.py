# Define a list of values
values = [1, 2, 3, 4, 5]

# Convert the list to a list of dictionaries
list_of_dicts = [{'value': value} for value in values]

# Print the list of dictionaries
print("List of Dictionaries:")
for item in list_of_dicts:
    print(item)
