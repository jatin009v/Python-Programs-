# Function to add two matrices
def add_matrices(mat1, mat2):
    result = [[0 for _ in range(4)] for _ in range(4)]  # Initialize a 4x4 matrix with zeros

    # Iterate through each element of the matrices and add them
    for i in range(4):
        for j in range(4):
            result[i][j] = mat1[i][j] + mat2[i][j]

    return result

# Input matrices
matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

matrix2 = [
    [17, 18, 19, 20],
    [21, 22, 23, 24],
    [25, 26, 27, 28],
    [29, 30, 31, 32]
]

# Call the function to add the matrices
result_matrix = add_matrices(matrix1, matrix2)

# Display the result
print("Matrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nSum of the matrices:")
for row in result_matrix:
    print(row)
