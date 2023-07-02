
def matrix_divided(matrix, div):
    # matrix must be a matrix (list of lists) of integers/floats
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [n for row in matrix for n in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Each row of the matrix must be of the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # div must be a number
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    # division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # output
    new_matrix = [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
    # Returns a new matrix
    return new_matrix

