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
from cs3430_s24_hw04 import simplex, get_solution_from_tab

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

"""
8. The simplex algorithm only works for standard maximum problems. This is because it is continually optimizing the results of the 
p function by choosing the most negative value in the corresponding row, and ensuring that the algorithm's chosen exit variable is 
having the smallest impact on the basic solution column. Therefore, the algorithm is only functional for SMPs.
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
Python, as well as many other programming languages, have trouble representing very small or very large
floating point values, thus leading odd and incorrect behaviors. 
For example, as given by lecture 3, in python, due to these properties, the following theorem holds:

"There exist positive real numbers z1, z2, z3 such that z1 < z2 < z3 and
for some real number x such that |x|>0,x+z1 =x+z2 =x+z3." 

Naturally, this cannot be the case, but because very small values in python become instable, this condition 
is true. 
"""

### ================= Problem 10 ==========================

def farming_land_allocation():
    # x := crop A
    # y := crop B
    # z := crop C

    # Total 1000 acres
    # Total 600 acre-feet of water

    # 120(x) + 80(y) + 50(z) ≤ 1000
    # 0.5(x) + 0.33333(y) + 0.3333333(z) ≤ 600

    in_vars = {0:3, 1:4, 2:5}
    m = np.array([[120,   80,        50,          1, 0,   1000],
                  [0.5,   0.333333, 0.3333333,    0, 1,    600],
                  [  0,   0,          0,          0, 0,      0],
                  [ -1,    -1.2,         -2,         0, 0,       0]],dtype=float)

    tab = (in_vars, m)
    ### call simplex
    tab, solved = simplex(tab)
    ### get solution
    sol = get_solution_from_tab(tab)

    print(sol)
    ### return it
    return sol
