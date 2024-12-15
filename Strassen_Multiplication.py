def multiply(A, B, C):
    for i in range(N):

        for j in range(N):

            C[i][j] = 0
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]

print(i+j+k)
