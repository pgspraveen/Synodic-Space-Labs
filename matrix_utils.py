import threading  # For multithreading support

# Custom exception class to handle matrix-specific errors
class MatxExm(Exception):
    pass

# 1. Matrix Multiplication
def matrix_multiply(A, B):
    # Check if number of columns in A == number of rows in B
    if len(A[0]) != len(B):
        raise MatxExm("Cannot multiply: Incompatible dimensions.")
    
    result = []  # To store the final matrix
    for i in range(len(A)):  # For each row in A
        row = []
        for j in range(len(B[0])):  # For each column in B
            sum_value = 0
            for k in range(len(A[0])):  # Perform dot product
                sum_value += A[i][k] * B[k][j]
            row.append(sum_value)
        result.append(row)
    return result

# Example:
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]
# Output: [[19, 22], [43, 50]]

# 2. Matrix Transpose
def matrix_transpose(A):
    # zip(*A) transposes the matrix
    return [list(row) for row in zip(*A)]

# Example:
# Input: A = [[1, 2, 3], [4, 5, 6]]
# Output: [[1, 4], [2, 5], [3, 6]]

# 3. Read Matrix from File
def read_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            row = list(map(int, line.strip().split()))
            if len(row) == 0:
                continue
            # Ensure all rows have the same number of columns
            if matrix and len(row) != len(matrix[0]):
                raise MatxExm("Rows have inconsistent length")
            matrix.append(row)
    return matrix

# File: test_matrix.txt
# Content:
# 1 2 3
# 4 5 6
# Output: [[1, 2, 3], [4, 5, 6]]

# 4. Concurrent Matrix Multiplication
class ConcurrentMultiplier:
    def __init__(self, A, B):
        if len(A[0]) != len(B):
            raise MatxExm("Cannot multiply: Incompatible dimensions.")
        self.A = A
        self.B = B
        self.result = [[0] * len(B[0]) for _ in range(len(A))]
        self.lock = threading.Lock()  # To avoid race conditions

    def worker(self, i, j):
        sum_val = 0
        for k in range(len(self.A[0])):
            sum_val += self.A[i][k] * self.B[k][j]
        with self.lock:
            self.result[i][j] = sum_val  # Safely write to shared matrix

    def multiply(self):
        threads = []
        for i in range(len(self.A)):
            for j in range(len(self.B[0])):
                t = threading.Thread(target=self.worker, args=(i, j))
                threads.append(t)
                t.start()
        for t in threads:
            t.join()
        return self.result

# Example:
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]
# Output: [[19, 22], [43, 50]] (Same as normal multiply but done with threads)
