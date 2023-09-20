# Function to remove an item from a tuple
def remove_item_from_tuple(input_tuple, item_to_remove):
    # Convert the tuple to a list to make it mutable
    mutable_list = list(input_tuple)
    
    # Check if the item exists in the list before attempting removal
    if item_to_remove in mutable_list:
        mutable_list.remove(item_to_remove)
    
    # Convert the list back to a tuple
    new_tuple = tuple(mutable_list)
    
    return new_tuple

# Test the function
my_tuple = (1, 2, 3, 4, 5)
item_to_remove = 3

# Remove the item from the tuple
new_tuple = remove_item_from_tuple(my_tuple, item_to_remove)

# Print the new tuple
print("Original Tuple:", my_tuple)
print("New Tuple after removing", item_to_remove, ":", new_tuple)
