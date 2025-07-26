# Matrix Operations Utility

## 📌 Project Overview

This project provides utility functions for performing essential matrix operations such as multiplication, transpose, file reading, and multithreaded multiplication using Python. It is designed to be modular, testable, and easy to extend.

## 🚀 Features Implemented

* **Matrix Multiplication**: Standard row-column based multiplication.
* **Matrix Transpose**: Efficient transposition using Python’s built-in functions.
* **Read Matrix from File**: Read and validate matrix data from text files.
* **Concurrent Matrix Multiplication**: Multiply matrices using multithreading.
* **Custom Exception Handling**: Catches dimension mismatches and input errors.

## 🧠 Thought Process Behind the Code

### 1. **Design Philosophy**

The goal was to build **clean, modular, and testable** code:

* Each function does **one clear task**.
* Used Python features like `zip`, list comprehensions, and custom exceptions.
* Designed with **edge cases** and **real-world usage** in mind.

### 2. **Why Multithreading?**

Matrix operations can be time-consuming for large inputs. We added `ConcurrentMultiplier` to:

* Perform element-wise computation in **parallel**.
* Use `threading.Lock()` to handle **shared memory safely**.

### 3. **Error Handling**

* Used a custom exception class `MatxExm` to handle all errors in a clean, traceable way.
* Checks for **dimension mismatch**, **inconsistent row lengths**, and **empty input**.

### 4. **Testing Philosophy**

* Wrote **unit tests** using `unittest` to test each function independently.
* Included both **happy paths** and **edge cases** (like incompatible dimensions).
* Created a sample file `test_matrix.txt` for testing file input logic.

## 📂 File Structure

```
matrix_project/
├── matrix_utils.py          # Matrix functions and ConcurrentMultiplier class
├── test_matrix_utils.py     # Unit tests for all matrix operations
├── test_matrix.txt          # Sample matrix input for testing
├── matrix_utility_report.pdf# Detailed report of fixes, improvements, and features
└── README.md                # This file
```

## 📋 Requirements

* Python 3.x

## ✅ How to Run

1. Clone the repo or download the files.
2. To test:

```bash
python test_matrix_utils.py
```

## 📈 Future Improvements

* Add support for float inputs and sparse matrices.
* Use ThreadPoolExecutor to manage threads more efficiently.
* Add matrix operations like addition, subtraction, inverse, and determinant.
* Integrate with NumPy for performance boosts (if external libraries are allowed).

## 👨‍💻 Author Notes

This project was developed with the mindset of making matrix operations **educational**, **scalable**, and **thread-safe**. All functions were debugged, tested, and commented for clarity.

Feel free to extend or contribute to make it even better! 🎯


