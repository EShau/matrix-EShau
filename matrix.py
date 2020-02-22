"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for row in range(len(matrix[0])):
        for point in matrix:
            print("%-3d" % point[row]),
        print("\n"),

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for col in range(len(matrix)):
        for row in range(len(matrix[0])):
            if col == row:
                matrix[col][row] = 1
            else:
                matrix[col][row] = 0


#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    new_row = len(m1[0])
    new_col = len(m2)
    temp_matrix = new_matrix(new_row, new_col)
    for row in range(new_row):
        for col in range(new_col):
            temp_matrix[col][row] = sum([(m1[k][row] * m2[col][k]) for k in range(len(m2[0]))])
    del m2[:]
    for col in temp_matrix:
        m2.append(col)


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
