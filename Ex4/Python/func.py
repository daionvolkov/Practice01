import random
import time
import threading
import csv
import datetime


def matmul(A, B):
    m = len(A)
    n = len(B)
    C = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C


def matmul_threaded(A, B, num_threads):
    m = len(A)
    n = len(B)
    C = [[0 for j in range(n)] for i in range(m)]
    threads = []
    for i in range(num_threads):
        start_row = i * m // num_threads
        end_row = (i + 1) * m // num_threads
        thread = threading.Thread(
            target=matmul_worker, args=(A, B, C, start_row, end_row))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return C


def matmul_worker(A, B, C, start_row, end_row):
    for i in range(start_row, end_row):
        for j in range(len(B)):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]


def generate_matrix(m, n, min_val, max_val):
    return [[random.uniform(min_val, max_val) for _ in range(n)] for _ in range(m)]


def write_matrix_to_csv(matrix, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in matrix:
            writer.writerow(row)


def read_matrix_from_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        matrix = []
        for row in reader:
            row = [float(x) for x in row]
            matrix.append(row)
        return matrix


def write_result_to_file(result):
    with open('results.csv', 'a', encoding='utf-8') as f:
        now = datetime.datetime.now()
        f.write('In Python\n')
        f.write(now.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        f.write(result)
