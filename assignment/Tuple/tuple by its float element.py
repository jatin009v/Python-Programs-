# Sample data: a list of tuples
data = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

# Sort the tuple by its float element
sorted_data = sorted(data, key=lambda x: float(x[1]))

# Print the sorted data
print("Sorted Data:")
for item in sorted_data:
    print(item)
