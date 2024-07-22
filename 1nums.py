 Write a NumPy program to create an array of 10 zeros, 10 o import numpy as np

# Create arrays of zeros, ones, and fives
zeros_array = np.zeros(10)
ones_array = np.ones(10)
fives_array = np.ones(10) * 5

# Concatenate the arrays to form the final array
result_array = np.concatenate([zeros_array, ones_array, fives_array])

print("Array of 10 zeros:")
print(zeros_array)
print("\nArray of 10 ones:")
print(ones_array)
print("\nArray of 10 fives:")
print(fives_array)

print("\nFinal concatenated array:")
print(result_array)
[4:10 pm, 22/7/2024] Neha: Array of 10 zeros:
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

Array of 10 ones:
[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

Array of 10 fives:
[5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]

Final concatenated array:
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 5. 5. 5. 5. 5.
 5. 5. 5. 5. 5.]
