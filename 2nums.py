 Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
 import numpy as np

# Create an array of values ranging from 2 to 10 (inclusive)
values = np.arange(2, 11)

# Reshape the array into a 3x3 matrix
matrix = values.reshape(3, 3)

print("3x3 Matrix with values ranging from 2 to 10:")
print(matrix)
[4:11 pm, 22/7/2024] Neha: 3x3 Matrix with values ranging from 2 to 10:
[[ 2  3  4]
 [ 5  6  7]
 [ 8  9 10]]
