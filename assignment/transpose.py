# Define the original matrix (4x5)
original_matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

# Find the dimensions of the original matrix
rows = len(original_matrix)
columns = len(original_matrix[0])

# Initialize a new matrix for the transpose (5x4)
transpose_matrix = [[0 for _ in range(rows)] for _ in range(columns)]

# Calculate the transpose
for i in range(rows):
    for j in range(columns):
        transpose_matrix[j][i] = original_matrix[i][j]

# Display the transpose matrix
for row in transpose_matrix:
    print(row)
