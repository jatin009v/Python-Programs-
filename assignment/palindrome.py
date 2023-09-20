for num in range(100, 501):
    # Convert the number to a string for easy comparison
    num_str = str(num)
    
    # Check if the reversed string is equal to the original string
    if num_str == num_str[::-1]:
        print(num)
