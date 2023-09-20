# Original tuple of string values
original_tuple = (('333', '33'), ('1416', '55'))

# Convert the original tuple to a tuple of integers
integer_tuple = tuple(tuple(int(value) for value in subtuple) for subtuple in original_tuple)

# Print the tuple of integers
print("Tuple of Integer Values:")
print(integer_tuple)
