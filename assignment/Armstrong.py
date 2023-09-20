for num in range(100, 501):
    # Convert the number to a string to count the number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Initialize a variable to store the sum of digits raised to the power of the number of digits
    armstrong_sum = 0
    
    # Calculate the sum of digits raised to the power of the number of digits
    for digit in num_str:
        armstrong_sum += int(digit) ** num_digits
    
    # Check if the number is an Armstrong number
    if armstrong_sum == num:
        print(num)
