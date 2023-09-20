# Define a list of multiple integers
int_list = [1, 2, 3, 4, 5]

# Convert the list of integers to a single integer
# Join the integers as strings and then convert to an integer
single_integer = int(''.join(map(str, int_list)))

# Print the single integer
print("Single Integer:", single_integer)
