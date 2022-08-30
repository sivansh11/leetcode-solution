import math


def get_other_indices(i, j, max_i, max_j):
    return (j, max_i - i - 1), (max_i - i - 1, max_j - j - 1), (max_j - j - 1, i)


def rotate(matrix: list[list[int]]) -> None:
    max_i = len(matrix)
    max_j = len(matrix[0])

    for i in range(max_i):
        if i >= math.floor(max_i / 2):
            continue
        for j in range(max_j):
            if j >= math.ceil(max_j / 2):
                continue
            top_left = (i, j)
            top_right, bottom_right, bottom_left = get_other_indices(i, j, max_i, max_j)
            matrix[top_left[0]][top_left[1]], matrix[top_right[0]][top_right[1]], matrix[bottom_right[0]][
                bottom_right[1]], \
            matrix[bottom_left[0]][bottom_left[1]] = matrix[bottom_left[0]][bottom_left[1]], matrix[top_left[0]][
                top_left[1]], matrix[top_right[0]][top_right[1]], matrix[bottom_right[0]][bottom_right[1]]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
print(matrix)

a, b, c, d = 1, 2, 3, 4
a, b, c, d = b, c, d, a
