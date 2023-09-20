def print_triangle(height):
    for i in range(1, height + 1):
        for j in range(height - i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", end="")
        print()

try:
    height = int(input("Enter the height of the triangle: "))
    print_triangle(height)
except ValueError:
    print("Please enter a valid integer for the height.")
