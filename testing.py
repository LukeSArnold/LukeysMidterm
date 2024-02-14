import numpy as np

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
    
        print(mat)
        print(x)

    return x
if __name__ == '__main__':
    A = np.array([[1, 1, -3],
                  [2, 3, -1],
                  [4, 5, -2]],
                     dtype=float)
    b = np.array([[-5],
                  [7],
                  [10]], dtype=float)
    x  = solve_lin_sys_with_gje(A, b)
    bb = np.dot(A, x)
    assert np.allclose(bb, b)

