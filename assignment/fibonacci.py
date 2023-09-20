# Function to generate Fibonacci series up to a given limit
def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        print(a, end=" ")
        a, b = b, a + b

# Call the function to print Fibonacci series up to 50
fibonacci(50)
