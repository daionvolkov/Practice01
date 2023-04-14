from func import *
import time

A = read_matrix_from_csv('matrix_a.csv')
B = read_matrix_from_csv('matrix_b.csv')
C = read_matrix_from_csv('matrix_c.csv')

# Matrix multiplication without multithreading
start_time = time.time()
C1 = matmul(A, B)
C1 = [[2.0 * x + 3.0 * y for x, y in zip(row1, row2)]
      for row1, row2 in zip(C1, C)]
end_time = time.time()
res_without_multithreading = 'Time without multithreading: {:.4f} seconds'.format(
    end_time - start_time)
print(res_without_multithreading)
write_result_to_file(res_without_multithreading)

# Matrix multiplication with multithreading
start_time = time.time()
C2 = matmul_threaded(A, B, 4)
C2 = [[2.0 * x + 3.0 * y for x, y in zip(row1, row2)]
      for row1, row2 in zip(C2, C)]
end_time = time.time()
res_with_multithreading = 'Time with multithreading: {:.4f} seconds'.format(
    end_time - start_time)
print(res_with_multithreading)
write_result_to_file(res_with_multithreading)

write_matrix_to_csv(C2, 'C_result.txt')
