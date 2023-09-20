# Define two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Find the common elements using a list comprehension
common_elements = [x for x in list1 if x in list2]

# Print the common elements
print("Common elements of list1 and list2 are:", common_elements)
