#!/bin/env python3
import numpy as np

# Solving (A) system
a = np.array([[0, 1, -1], [3, 2, 1], [5, 4, 0]])
b = np.array([2, 4, 1])

# using solve method from numpy module
x = np.linalg.solve(a, b)
print(f"""this is the solution for the first system
        'using the solve method': '{x}""")
# using the Cramer Rule

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
this is the solution for the first system 'using the Cramer's rule:
    x = {x_det/det_1}
    y = {x_det/det_1}
    z = {z_det/det_1}
""")

# solving the (B) system

a = np.array([[-1, 0, -1], [3, 2, 1], [5, 4, 0]])
b = np.array([-3, 2, 1])

# using solve method from numpy module
x = np.linalg.solve(a, b)
print(f"""this is the solution for the first system
        'using the solve method':{x}""")
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
this is the solution for the Second system 'using the Cramer's Rule:
    x = {x_det/det_1}
    y = {x_det/det_1}
    z = {z_det/det_1}
""")

