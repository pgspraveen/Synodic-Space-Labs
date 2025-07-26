import unittest  # Python's built-in testing framework
from matrix_utils import (
    matrix_multiply,
    matrix_transpose,
    read_matrix_from_file,
    ConcurrentMultiplier,
    MatxExm
)

class TestMatrixUtils(unittest.TestCase):

    def test_multiply(self):
        # Test normal matrix multiplication
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        # Expected result:
        # [[1*5 + 2*7, 1*6 + 2*8], [3*5 + 4*7, 3*6 + 4*8]]
        # => [[19, 22], [43, 50]]
        expected = [[19, 22], [43, 50]]
        self.assertEqual(matrix_multiply(A, B), expected)

    def test_transpose(self):
        # Test matrix transposition
        A = [[1, 2, 3], [4, 5, 6]]
        # Transposed result:
        # [[1, 4], [2, 5], [3, 6]]
        expected = [[1, 4], [2, 5], [3, 6]]
        self.assertEqual(matrix_transpose(A), expected)

    def test_incompatible_dimensions(self):
        # Test multiplication with incompatible dimensions
        A = [[1, 2, 3], [4, 5, 6]]
        B = [[1, 2], [3, 4]]  # Not compatible with A
        # Should raise custom exception
        with self.assertRaises(MatxExm):
            matrix_multiply(A, B)

    def test_read_matrix(self):
        # Create a temporary matrix file and read it
        with open("test_matrix.txt", "w") as f:
            f.write("1 2 3\n4 5 6\n")
        # Expected content from file: [[1, 2, 3], [4, 5, 6]]
        result = read_matrix_from_file("test_matrix.txt")
        expected = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(result, expected)

    def test_concurrent_multiply(self):
        # Test threaded multiplication logic
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        # Same expected output as normal multiplication
        expected = [[19, 22], [43, 50]]
        cm = ConcurrentMultiplier(A, B)
        result = cm.multiply()
        self.assertEqual(result, expected)

# Run tests when this file is executed
if __name__ == '__main__':
    unittest.main()
