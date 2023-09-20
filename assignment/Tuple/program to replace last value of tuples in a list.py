# Sample list of tuples
list_of_tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# Function to replace the last value in a tuple with a new value
def replace_last_value(tuple_list, new_value):
    modified_list = [list(t) for t in tuple_list]  # Convert tuples to lists
    for sublist in modified_list:
        sublist[-1] = new_value  # Replace the last value
    return [tuple(sublist) for sublist in modified_list]  # Convert lists back to tuples

# New value to replace the last values in tuples
new_value = 100

# Replace the last values in tuples
modified_tuples = replace_last_value(list_of_tuples, new_value)

# Print the modified list of tuples
print("Modified List of Tuples:")
print(modified_tuples)
