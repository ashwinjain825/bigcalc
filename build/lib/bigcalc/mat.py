# Extended mat.py with matrix operations and structured error handling
# Type hints added so IDE shows input and output types
from typing import List, Union, Dict, Tuple

Matrix = List[List[float]]
ErrorType = Dict[str, str]
ResultType = Union[Matrix, float, int, bool, List[float], ErrorType]

ERRORS = {
    "MAT00001": "Matrix must be a non-empty list",
    "MAT00002": "Matrix must be a 2D list",
    "MAT00003": "Matrix rows cannot be empty",
    "MAT00004": "All rows must have same number of columns",
    "MAT00005": "Matrix elements must be numbers",
    "MAT00006": "Addition requires both matrices to have same dimensions",
    "MAT00007": "Subtraction requires both matrices to have same dimensions",
    "MAT00008": "Multiplication not possible: columns of first matrix must equal rows of second matrix",
    "MAT00009": "Trace is only defined for square matrices",
    "MAT00010": "Inverse exists only for square matrices",
    "MAT00011": "Inverse does not exist (determinant is 0)",
    "MAT00012": "Division by zero is not allowed",
    "MAT00013": "Determinant is only defined for square matrices",
    "MAT00014": "Power must be a non-negative integer",
    "MAT00015": "Row index out of range",
    "MAT00016": "Column index out of range",
    "MAT00017": "Scalar value must be a number"
}


def error(code):
    return {
        "error_code": code,
        "message": ERRORS[code]
    }



def is_matrix(mat):
    if not isinstance(mat, list) or len(mat) == 0:
        return False, error("MAT00001")

    if not all(isinstance(row, list) for row in mat):
        return False, error("MAT00002")

    if len(mat[0]) == 0:
        return False, error("MAT00003")

    cols = len(mat[0])

    for row in mat:
        if len(row) != cols:
            return False, error("MAT00004")

        for val in row:
            if not isinstance(val, (int, float)):
                return False, error("MAT00005")

    return True, None


def is_square(mat):
    return len(mat) == len(mat[0])


def copy_matrix(mat):
    return [row[:] for row in mat]


def identity_matrix(n):
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(1.0 if i == j else 0.0)
        result.append(row)
    return result


def transpose(a):
    valid, err = is_matrix(a)
    if not valid:
        return err

    rows = len(a)
    cols = len(a[0])
    result = []

    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(a[i][j])
        result.append(row)

    return result


def scalar_multiply(a, k):
    valid, err = is_matrix(a)
    if not valid:
        return err

    if not isinstance(k, (int, float)):
        return error("MAT00017")

    return [[value * k for value in row] for row in a]


def divide(a, k):
    valid, err = is_matrix(a)
    if not valid:
        return err

    if not isinstance(k, (int, float)):
        return error("MAT00017")

    if k == 0:
        return error("MAT00012")

    return [[value / k for value in row] for row in a]


def determinant(a):
    valid, err = is_matrix(a)
    if not valid:
        return err

    if not is_square(a):
        return error("MAT00013")

    n = len(a)

    if n == 1:
        return a[0][0]

    if n == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]

    det = 0
    for col in range(n):
        minor = []
        for i in range(1, n):
            row = []
            for j in range(n):
                if j != col:
                    row.append(a[i][j])
            minor.append(row)

        sign = 1 if col % 2 == 0 else -1
        det += sign * a[0][col] * determinant(minor)

    return det


def trace(a):
    valid, err = is_matrix(a)
    if not valid:
        return err

    if not is_square(a):
        return error("MAT00009")

    total = 0
    for i in range(len(a)):
        total += a[i][i]

    return total


def add(a, b):
    va, ea = is_matrix(a)
    if not va:
        return ea
    vb, eb = is_matrix(b)
    if not vb:
        return eb

    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return error("MAT00006")

    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def sub(a, b):
    va, ea = is_matrix(a)
    if not va:
        return ea
    vb, eb = is_matrix(b)
    if not vb:
        return eb

    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return error("MAT00007")

    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def multiply(a, b):
    va, ea = is_matrix(a)
    if not va:
        return ea
    vb, eb = is_matrix(b)
    if not vb:
        return eb

    if len(a[0]) != len(b):
        return error("MAT00008")

    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            total = 0
            for k in range(len(a[0])):
                total += a[i][k] * b[k][j]
            row.append(total)
        result.append(row)

    return result


def power(a, n):
    valid, err = is_matrix(a)
    if not valid:
        return err

    if not is_square(a):
        return error("MAT00013")

    if not isinstance(n, int) or n < 0:
        return error("MAT00014")

    result = identity_matrix(len(a))

    for _ in range(n):
        result = multiply(result, a)

    return result


def inverse(a):
    valid, err = is_matrix(a)
    if not valid:
        return err

    if not is_square(a):
        return error("MAT00010")

    if determinant(a) == 0:
        return error("MAT00011")

    n = len(a)
    mat = copy_matrix(a)
    inv = identity_matrix(n)

    for i in range(n):
        pivot = mat[i][i]

        if pivot == 0:
            for j in range(i + 1, n):
                if mat[j][i] != 0:
                    mat[i], mat[j] = mat[j], mat[i]
                    inv[i], inv[j] = inv[j], inv[i]
                    pivot = mat[i][i]
                    break

        for j in range(n):
            mat[i][j] /= pivot
            inv[i][j] /= pivot

        for r in range(n):
            if r != i:
                factor = mat[r][i]
                for c in range(n):
                    mat[r][c] -= factor * mat[i][c]
                    inv[r][c] -= factor * inv[i][c]

    return inv
