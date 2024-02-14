#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s24_midterm01.py
# Luke Arnold
# a02368233
# WRITE THE TIME IT TOOK YOU TO COMPLETE THIS EXAM.
##############################################################

import numpy as np
import numpy.linalg

### put your imports from your previous/current assignments.
from cs3430_s24_hw01 import leibnitz_det, cramers_rule
from cs3430_s24_hw02 import bsubst, fsubst, lud_solve

### ================ Problem 01 ========================

def solve_lin_sys_with_gje(a, b):
    mat = a.copy()
    x = b.copy()


    size = mat.shape[0]

    for col in range(size):
        x[col, :] = (x[col,:] / mat[col][col])
        mat[col, :] = (mat[col, :] / mat[col][col])

        for row in range(size):
            if row != col:
                x[row, :] -= x[col, :] * mat[row][col]
                mat[row, :] -= (mat[col, :] * mat[row][col])
    return x 


### ================ Problem 02 ========================

def solve_lin_sys_with_cramer(A, b):
    
    return cramers_rule(A,b)

### ================ Problem 03 =========================

def solve_lin_sys_with_bsubst(A, n, b, m):
    return bsubst(A, n, b, m)

### ================ Problem 04 =========================

def solve_lin_sys_with_fsubst(A, n, b, m):
    return fsubst(A, n, b, m)
    
### ================ Problem 05 =========================

def solve_lin_sys_with_lud(A, n, b, m):
    return lud_solve(A, n, b, m)


### ================ Problem 06 =========================

"""
1.  A standard maximimzation problem (or SMP) is a function that involves a function p, a function which is dependent on a series of variable, and a 
    series of linear inequalities that correspond to the set of variable. The goal is to maximize the value of the function p 
    while keeping all variables within the bounds of the inequalities.
"""

"""
2. The objective function is the function p, which is a function that takes in a seriers of variables that are restricted by linear inequalities. Usually the goal
   is to mimimize or maximize this function while adhering to the constraints of the linear equalities which dictate its variables.
"""

"""
3. A corner point is where the linear inequalities intersect on a graph if we were to graph them
"""

"""
4. The feasible set is the shaded region on a graph that corrsponds to where all inequalities are satifised for a series of input variables dependent on their values.
""" 

"""
5. One condition is when there is no possible entering value for the simplex algorithm. This occurs when all values in the p-row are non-negative. 

   Another condition is when there is no possible exiting value, this occurs when there exists a possible entering value, but there are no 
   positive entries in the column that correspond to the entering value.
"""

"""
6. If a feasible set is bounded, then the corresponding objective function attains its maximum/minimum value at a corner point of F.
"""

"""
7. If a feasible set is unbounded, then the corresponding ojective function attains its maximum/minimum value at a corner point or takes arbitrarily large positive/negative values on F.
"""



### ================ Problem 07 =========================

"""
Type your answer to Problem 07 here in the form of
the table. Clearly identify the column and row variables.
"""

"""
___________________________________________________
|     |  x  |  y  |  z  |  u  |  v  |  w  |  B.S. |
|-----|-----|-----|-----|-----|-----|-----|-------|
|  u  |  6  |  0  |  1  |  1  |  0  |  0  |  122  |
|-----|-----|-----|-----|-----|-----|-----|-------|
|  v  |  0  |  2  |  5  |  0  |  1  |  0  |  502  |
|-----|-----|-----|-----|-----|-----|-----|-------|
|  w  |  9  | -7  |  6  |  0  |  0  |  1  |  902  |
|_____|_____|_____|_____|_____|_____|_____|_______|

"""

### ================ Problem 08 =========================

"""
Type your answer to Problem 08 here. Clearly identify 
the column and row variables of the pivot and its value
and explain how you found it.
"""

"""
The entering variable is found by taking the most negative value from p, therefore in this example
the entering variable is x_1 with a mininum value of -22. 

Then, the exiting variable is found by dividing the basic solution by each row's variable in the column of the entering value, and taking the
smallest value. 
Therefore,

x_3 => 190/6  = 31.66666
x_4 => 510/7  = 72.857
x_5 => 810/10 = 81

Therefore, x_3 has the smallest value, thus the pivot is occuring at 
row 1, column 2 which has a value of 6
"""

### ================ Problem 09 =========================

"""
Type your answer to Problem 09 here. Be brief. Do not
write an essay.
"""

### ================= Problem 10 ==========================

def farming_land_allocation():
    ### Set up your tableau by replacing Nones
    ### with appropriate values.
    in_vars = {0:3, 1:4, 2:5}
    m = [[2,    2,   3, 1, 0, 0, 160],
         [5,    1,  10, 0, 1, 0, 100],
         [-10, -6,  -2, 0, 0, 1, 0],
         [ 1,  1.2, 2, 0, 0, 0, 0]],
         dtype=float)

    tab = (m, in_vars)
    ### call simplex
    tab, solved = simplex(tab)
    ### get solution
    sol = get_solution_from_tab(tab)
    ### return it
    return sol
