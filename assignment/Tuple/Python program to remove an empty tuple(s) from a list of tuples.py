# Sample data: a list of tuples
data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

# Remove empty tuples using a list comprehension
filtered_data = [tup for tup in data if tup]

# Print the filtered data
print("Filtered Data:")
print(filtered_data)
