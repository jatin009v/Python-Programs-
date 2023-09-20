# Method 1: Using the extend() method
# Define two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Append the elements of list1 to list2 using the extend() method
list2.extend(list1)

# Print the updated list2
print("Method 1 - Using extend():")
print("List2 after appending list1:", list2)

# Method 2: Using the + operator
# Define two lists again to avoid modification from the previous method
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Append the elements of list1 to list2 using the + operator
list2 += list1

# Print the updated list2
print("\nMethod 2 - Using + operator:")
print("List2 after appending list1:", list2)
