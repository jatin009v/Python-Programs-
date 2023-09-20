# Function to find repeated items in a tuple
def find_repeated_items(my_tuple):
    item_count = {}  # Dictionary to store item counts
    repeated_items = set()  # Set to store repeated items
    
    for item in my_tuple:
        if item in item_count:
            item_count[item] += 1
            if item_count[item] == 2:
                repeated_items.add(item)
        else:
            item_count[item] = 1
    
    return list(repeated_items)

# Test the function
my_tuple = (1, 2, 2, 3, 4, 4, 4, 5)

# Find repeated items in the tuple
repeated_items = find_repeated_items(my_tuple)

# Print the repeated items
print("Repeated Items:", repeated_items)
