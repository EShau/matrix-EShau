from display import *
from draw import *
from matrix import *

BROWN_1 = [74, 55, 19]
BROWN_2 = [105, 82, 32]
BROWN_3 = [139, 106, 39]
BROWN_4 = [37, 30, 12]
BLUE_1 = [56, 200, 173]
BLUE_2 = [28, 178, 153]
BLUE_3 = [119, 207, 185]
BLUE_4 = [27,62,55]

screen = new_screen(15,15)
matrix = new_matrix(4, 0)
add_edge(matrix, 1, 2, 0, 9, 10, 0)
add_edge(matrix, 11, 12, 0, 11, 12, 0)
draw_lines( matrix, screen, BROWN_1 )
matrix = new_matrix(4, 0)
add_edge(matrix, 1, 1, 0, 1, 1, 0)
add_edge(matrix, 3, 3, 0, 3, 3, 0)
add_edge(matrix, 5, 5, 0, 5, 5, 0)
add_edge(matrix, 7, 7, 0, 7, 7, 0)
add_edge(matrix, 9, 9, 0, 9, 9, 0)
add_edge(matrix, 12, 12, 0, 12, 12, 0)
draw_lines( matrix, screen, BROWN_2 )
matrix = new_matrix(4, 0)
add_edge(matrix, 2, 2, 0, 2, 2, 0)
add_edge(matrix, 4, 4, 0, 4, 4, 0)
add_edge(matrix, 6, 6, 0, 6, 6, 0)
add_edge(matrix, 8, 8, 0, 8, 8, 0)
add_edge(matrix, 9, 9, 0, 9, 9, 0)
add_edge(matrix, 11, 11, 0, 11, 11, 0)
draw_lines( matrix, screen, BROWN_3 )
matrix = new_matrix(4, 0)
add_edge(matrix, 2, 1, 0, 10, 9, 0)
add_edge(matrix, 12, 11, 0, 12, 11, 0)
draw_lines( matrix, screen, BROWN_4 )
matrix = new_matrix(4, 0)
add_edge(matrix, 6, 12, 0, 6, 12, 0)
add_edge(matrix, 9, 12, 0, 9, 12, 0)
add_edge(matrix, 10, 10, 0, 10, 10, 0)
add_edge(matrix, 12, 6, 0, 12, 6, 0)
add_edge(matrix, 12, 9, 0, 12, 9, 0)
draw_lines( matrix, screen, BLUE_1 )
matrix = new_matrix(4, 0)
add_edge(matrix, 7, 12, 0, 8, 12, 0)
add_edge(matrix, 9, 11, 0, 10, 11, 0)
add_edge(matrix, 11, 9, 0, 11, 10, 0)
add_edge(matrix, 12, 7, 0, 12, 8, 0)
draw_lines( matrix, screen, BLUE_2 )
matrix = new_matrix(4, 0)
add_edge(matrix, 5, 12, 0, 5, 12, 0)
add_edge(matrix, 12, 5, 0, 12, 5, 0)
draw_lines( matrix, screen, BLUE_3 )
matrix = new_matrix(4, 0)
add_edge(matrix, 4, 12, 0, 4, 12, 0)
add_edge(matrix, 5, 11, 0, 8, 11, 0)
add_edge(matrix, 5, 13, 0, 9, 13, 0)
add_edge(matrix, 10, 12, 0, 10, 12, 0)
add_edge(matrix, 11, 5, 0, 11, 8, 0)
add_edge(matrix, 12, 4, 0, 12, 4, 0)
add_edge(matrix, 12, 10, 0, 12, 10, 0)
add_edge(matrix, 13, 5, 0, 13, 9, 0)
draw_lines( matrix, screen, BLUE_4 )

display(screen)

print("Pictures at pic.ppm")
print("Resize the picture into a .png using:")
print("convert -resize 500 -interpolate Nearest -filter point pic.ppm pic.png")
