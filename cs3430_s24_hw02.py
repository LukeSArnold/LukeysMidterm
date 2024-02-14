
#################################################
# Module: cs3430_s24_hw02.py
# Luke Arnold
# a02368233
# bugs to vladimir kulyukin in canvas
#################################################

import numpy as np
import pickle
import os

### =============== Problem 1 =============================

def lu_decomp(a, n):
    """ 
    lu_decomp(a, n) returns u, l such that np.dot(l, u) === a.
    a is an nxn matrix that is reduced to the upper and lower triangular matrices. 
    throws exception when there is no pivot in a column or rows must be swapped
    to create a pivot.
    lu_decomp(a, n) is destructive in that a is destructively modified into u.
    """
    
    mat = a.copy()
     
    size = mat.shape[0]
    
    l = np.eye(size) 
    # assuming square matrix, iterate through all rows and columns

    for col in range(size):
        for row in range(size - (col+1)):
            row = row + col + 1
            scalar_multiple = ((-(mat[row][col]))/(mat[col][col]))
            mat[row, :] = mat[row,: ] + (scalar_multiple * (mat[col, :]))
            l[row][col] = -scalar_multiple

    return mat, l
            

### =============== Problem 2 =============================

def bsubst(a, n, b, m):
    """
    bsubst uses back substitution to solve ax = b1, b2, ..., bm.
    a is an nxn upper-triangular matrix, n is its dimension.
    b is an nxm matrix of vectors b1, b2, ..., bm. 
    returns x.
    """

    result_array = np.empty((n,0), dtype=float)
    for col in range(m):
        solution = []

        for i in range(1, n+1, 1):
            prev = 0
            for j in range(i - 1):
                prev += (a[n-i][n-j-1] * solution[j]) 
           
            solution.append((b[n-i][col] - prev) / a[n-i][n-i])

        solution = solution[::-1]
        solution_vector = np.array(solution)
        column_vector = solution_vector.reshape(-1,1)
        
        result_array = np.hstack((result_array, column_vector))

    
    
    return result_array

    
        

def fsubst(a, n, b, m):
    """
    fsubst uses forward substitution to solve ax = b1, b2, ..., bm.
    a is an nxn lower-triangular matrix, n is its dimension.
    b is an nxm matrix of vectors b1, b2, ..., bm.
    returns x.
    """

    result_array = np.empty((n, 0), dtype=float)

    for res in range(m):
        solution = []
        for i in range(n):
            prev = 0
            for j in range(i):
                prev += a[i][j] * solution[j]

            result = ((b[i][res] - prev)/a[i][i])
            solution.append((b[i][res] - prev)/a[i][i])

        solution_vector = np.array(solution)
        column_vector = solution_vector.reshape(-1, 1)

        result_array = np.hstack((result_array, column_vector))


    return result_array


### =============== Problem 3 ====================

def lud_solve(a, n, b, m):
    """
    a is an nxn matrix; b is m nx1 vectors.
    Use forward subst to solve Ly = b for y.
    Use back    subst to solve Ux = y for x.
    Then LUx = Ly = b.
    Returns x.
    """

    results = lu_decomp(a,n)
   
    U = results[0]

    L = results[1]

    y = fsubst(L, n, b, m)

    x = bsubst(U, n, y, m)

    
    bb = np.array([np.matmul(a, x[:,0])]).T


    return x
