# Sample list with mixed data types
my_list = [1, 2, 3, (4, 5), 6, 7, 'eight', 9]

# Initialize a counter
count = 0

# Iterate through the list until a tuple is encountered
for item in my_list:
    if isinstance(item, tuple):
        break  # Exit the loop when a tuple is encountered
    count += 1

# Print the count of elements before the tuple
print("Count of elements before the tuple:", count)
