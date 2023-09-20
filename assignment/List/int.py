# Define a sample list with a mix of integer, float, and string elements
my_list = [1, 2.5, 'hello', 3, 'world', 4.0, 5]

# Initialize counters for integers, floats, and strings
int_count = 0
float_count = 0
str_count = 0

# Iterate through the list and count the elements of each type
for item in my_list:
    if isinstance(item, int):
        int_count += 1
    elif isinstance(item, float):
        float_count += 1
    elif isinstance(item, str):
        str_count += 1

# Print the counts
print("Number of integers:", int_count)
print("Number of floats:", float_count)
print("Number of strings:", str_count)
