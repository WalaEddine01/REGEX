#!/bin/env python3
import numpy as np

a = np.array([[2, 3, -1], [4, 1, 5], [-2, 4, 1]])
b = np.array([1, -2, -3])

# using solve method from numpy module
x = np.linalg.solve(a, b)
print(x)
# using the Cramer Rule

# 1- calculate the determinent if a

det_1 = np.linalg.det(a)
if det_1 == 0:
    print("the determinent is equal 0!!")
    exit(1)

x_matrix = a.copy()
y_matrix = a.copy()
z_matrix = a.copy()
for i in range(len(a)):
    for j in range(len(a)):
        if i == 0:
            x_matrix[j][i] = b[j]
        if i == 1:
            y_matrix[j][i] = b[j]
        if i == 2:
            z_matrix[j][i] = b[j]

x_det = np.linalg.det(np.array(x_matrix))
y_det = np.linalg.det(np.array(y_matrix))
z_det = np.linalg.det(np.array(z_matrix))

print(f"""
    x = {x_det/det_1}
    y = {x_det/det_1}
    z = {z_det/det_1}
""")
