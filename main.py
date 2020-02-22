from display import *
from draw import *
from matrix import *

print("Testing add_edge. Adding (1, 2, 3), (4, 5, 6) m2 =")
m2 = new_matrix(4, 0)
add_edge(m2, 1, 2, 3, 4, 5, 6)
print_matrix(m2)
print("\n")
print("Testing ident. m1 =")
m1 = new_matrix(4, 4)
ident(m1)
print_matrix(m1)
print("\n")
print("Testing Matrix mult. m1 * m2 =")
matrix_mult(m1, m2)
print_matrix(m2)
print("\n")
print("Testing Matrix mult. m1 =")
del m1[:]
add_edge(m1, 1, 2, 3, 4, 5, 6)
add_point(m1, 7, 8, 9)
add_point(m1, 10, 11, 12)
print_matrix(m1)
print("\n")
print("Testing Matrix mult. m1 * m2 =")
matrix_mult(m1, m2)
print_matrix(m2)
print("\n")

#draw_lines( matrix, screen, color )
#display(screen)
