###############################
# module: cs3430_s24_hw04.py
# description: CS3430: S24: Assignment 04
# YOUR NAME: Luke Arnold
# YOUR A-NUmBER: a02368233
###############################
import numpy as np
def simplex(tab):
    """
    Apply the simplex algorithm to the tableaue tab.
    """
    while True:

        # find minimum variable from last row to determine entering variable
        last_row = tab[1][-1]
        min_val = min(last_row)
        
        # if the smallest value is greater or equal to 0, all elements are non negative
        if min_val >= 0:
            return tab, True

        entering_variable = np.where(last_row==min_val)[0][0]
        
        # find minimum value in basic solution to determine exiting value
        working_column = tab[1][:,entering_variable]

        if max(working_column) <= 0:
            # no positive value in corresponding column
            return tab, False

        basic_solution_col = tab[1][:, -1]

        new_array = []
        for i in range(len(working_column) - 1):
            if working_column[i] >  0:
                new_array.append(basic_solution_col[i] / working_column[i])
            else:
                new_array.append(10000000000000000000000) 

        exiting_variable = new_array.index(min(new_array))
        row = tab[0]


        pivot_var = tab[1][exiting_variable][entering_variable]

        for i in range(tab[1].shape[0]):
            if i == exiting_variable:
                continue
            else:
                multiple = tab[1][i][entering_variable] / pivot_var
                tab[1][i] = tab[1][i] - (tab[1][exiting_variable] * multiple)   
        tab[1][exiting_variable] = tab[1][exiting_variable]/pivot_var


        tab[0][exiting_variable] = entering_variable

def get_solution_from_tab(tab):
    in_vars, mat = tab[0], tab[1]
    nr, nc = mat.shape
    sol = {}
    for k, v in in_vars.items():
        sol[v] = mat[k,nc-1]
    sol['p'] = mat[nr-1,nc-1]
    return sol

def display_solution_from_tab(tab):
    sol = get_solution_from_tab(tab)
    for var, val in sol.items():
        if var == 'p':
            print('p\t=\t{}'.format(val))
        else:
            print('x{}\t=\t{}'.format(var, val))



