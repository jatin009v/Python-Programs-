# Sample dictionary
my_dict = {'a': 10, 'b': 5, 'c': 15, 'd': 20, 'e': 25}

# Sort the dictionary by values in descending order
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

# Get the top 3 key-value pairs with the highest values
top_3_values = dict(list(sorted_dict.items())[:3])

print("Top 3 key-value pairs with the highest values:")
for key, value in top_3_values.items():
    print(f"{key}: {value}")
