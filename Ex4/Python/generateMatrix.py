from func import *

if __name__ == '__main__':
    A = generate_matrix(100, 50, -100, 100)
    B = generate_matrix(50, 200, -100, 100)
    C = generate_matrix(100, 200, -100, 100)

    write_matrix_to_csv(A, 'matrix_a.csv')
    write_matrix_to_csv(B, 'matrix_b.csv')
    write_matrix_to_csv(C, 'matrix_c.csv')
