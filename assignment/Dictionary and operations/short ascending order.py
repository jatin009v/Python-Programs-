# Sample dictionary
my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}

# Sorting by values in ascending order
ascending_sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Sorting by values in descending order
descending_sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Ascending Order:", ascending_sorted_dict)
print("Descending Order:", descending_sorted_dict)
