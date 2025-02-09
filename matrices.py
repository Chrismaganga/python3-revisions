matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])  # Access element at row 1, column 2 (Output: 6)

# sec
rows, cols = 3, 4
zero_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
print(zero_matrix)
# Output: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# using numpy
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = A + B
print(result)
# Output:
# [[ 6  8]
#  [10 12]]

#lkjkooo
A = np.array([[1, 2, 3], [4, 5, 6]])
transpose = A.T
print(transpose)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]

identity = np.eye(3)
print(identity)
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]


