matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(len(matrix) - 1, -1, -1):
    for j in range(len(matrix[i]) - 1, -1, -1):
        print(matrix[i][j], end=" ")
    print()