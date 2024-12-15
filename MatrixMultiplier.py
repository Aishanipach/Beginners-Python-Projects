# Define the matrices A and B
A = [
    [12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]
]

# Initialize the result matrix with zeros
result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

# Perform matrix multiplication
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

# Display the result
for r in result:
    print(r)
