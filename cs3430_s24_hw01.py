######################################################
# module: cs3430_s24_hw01.py
# bugs to vladimir kulyukin in canvas
# YOUR NAME: Luke Arnold
# YOUR A-NUMBER: a02368233
######################################################

import numpy as np
import numpy.linalg
import random

# ========== Problem 1 ==============

def cs3430_s24_hw_01_prob_1_1():
    A = np.array([[1, 1], [1, 4]], dtype=float)
    b = np.resize(np.array([3, 10], dtype=float), (2, 1))
    try:
        x = np.linalg.solve(A, b)
    except np.linalg.LinAlgError as e:
        return e
    return A, x, b

def cs3430_s24_hw_01_prob_1_2():
    A = np.array([[0, 1, -3], [2, 3, -1], [4, 5, -2]], dtype=float)
    b = np.array([[-5],
                  [7],
                  [10]], dtype=float)
    try:
        x = np.linalg.solve(A, b)
    except np.linalg.LinAlgError as e:
        return e
    return A, x, b

def cs3430_s24_hw_01_prob_1_3():
    A = np.array([[2, -1, 3], [3, 0, 2], [-2, 1, 4]], dtype=float)
    b = np.array([[4],
                  [5],
                  [6]], dtype=float)
    try:
        x = np.linalg.solve(A, b)
    except np.linalg.LinAlgError as e:
        return e
    return A, x, b

def cs3430_s24_hw_01_prob_1_4():
    A = np.array([[-1, 0, 1, -1], [2, 2, -1, -7], [4, -1, -9, -5], [3, -1, -8, -6]], dtype=float)
    b = np.array([[3],
                  [1],
                  [10],
                  [1]], dtype=float)

    try:
        x = np.linalg.solve(A, b)
    except np.linalg.LinAlgError as e:
        return e
    return A, x, b

### ============== Problem 2 ==================

def leibnitz_det(mat):
    
    if mat.shape[1] == 2:
        minor_determinant = ((mat[0][0] * mat[1][1]) - (mat[1][0] * mat[0][1]))

        return minor_determinant

    final_determinant = 0
    for i in range(mat.shape[1]):
        a = mat[0][i]
        new_matrix = np.delete(np.delete(mat, 0, axis=0), i, axis=1)
        c = ((-1)**(i+2)) * leibnitz_det(new_matrix)
        final_determinant = final_determinant + (a * c)

    return final_determinant

        

### ============== Problem 3 ==================

def cramers_rule(A, b):

    # assuming square matrix A

    a_det = leibnitz_det(A)
    solution_array = []
    for i in range(A.shape[1]):
        B1 = A.copy()
        B1[:, i] = np.squeeze(b)

        b1_det = leibnitz_det(B1)

        solution_array.append((b1_det/a_det))

    solution_vector = np.array([solution_array], dtype=float).transpose()


    return solution_vector
 
    

### ===========================================    
    
              
