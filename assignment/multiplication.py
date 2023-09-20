# Define the first matrix (4x5)
matrix1 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

# Define the second matrix (5xN)
matrix2 = [
    [21, 22, 23],
    [24, 25, 26],
    [27, 28, 29],
    [30, 31, 32],
    [33, 34, 35]
]

# Initialize a result matrix with zeros (4xN)
result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

# Perform matrix multiplication
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

# Display the result matrix
for row in result:
    print(row)
