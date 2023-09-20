# Define a list of lists
list_of_lists = [[3, 2, 1], [5, 4], [9, 6, 7, 8], [10], [12, 11]]

# Sort the list of lists by length and then by value
sorted_list = sorted(list_of_lists, key=lambda x: (len(x), x))

# Print the sorted list
print("Sorted List of Lists:")
for sublist in sorted_list:
    print(sublist)
