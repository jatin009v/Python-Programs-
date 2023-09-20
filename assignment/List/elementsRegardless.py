# Function to check if two lists contain the same elements regardless of order
def are_lists_equal(list1, list2):
    # Convert the lists to sets and check for equality
    return set(list1) == set(list2)

# Test cases
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
list3 = [1, 2, 3, 4, 5, 6]
list4 = [1, 2, 2, 3, 4, 5]

# Check if the lists contain the same elements
result1 = are_lists_equal(list1, list2)
result2 = are_lists_equal(list1, list3)
result3 = are_lists_equal(list1, list4)

# Print the results
print("Result 1 (list1 and list2):", result1)
print("Result 2 (list1 and list3):", result2)
print("Result 3 (list1 and list4):", result3)
