# Define a list
my_list = [12, 45, 2, 41, 31, 10, 8, 6]

# Initialize variables to store the smallest and second smallest numbers
smallest = float('inf')  # Initialize to positive infinity
second_smallest = float('inf')  # Initialize to positive infinity

# Iterate through the list to find the smallest and second smallest numbers
for num in my_list:
    if num < smallest:
        second_smallest = smallest  # Update second_smallest
        smallest = num  # Update smallest
    elif num < second_smallest and num != smallest:
        second_smallest = num  # Update second_smallest

# Check if a second smallest number was found
if second_smallest == float('inf'):
    print("There is no second smallest number in the list.")
else:
    print(f"The second smallest number in the list is: {second_smallest}")
