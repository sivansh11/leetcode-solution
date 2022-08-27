def term(i, j):
    if j == 1:
        return 1
    if j == i:
        return 1
    return term(i - 1, j - 1) + term(i - 1, j)

def generate(numRows):
    cache = {}
    def term(i, j):
        if (i, j) in cache:
            return cache[(i, j)]
        if j == 1 or j == i:
            val = 1
        else:
            val = term(i - 1, j - 1) + term(i - 1, j)
        cache[(i, j)] = val
        return val
    rows = []
    for i in range(1, numRows + 1):
        row = []
        for j in range(1, i + 1):
            row.append(term(i, j))
        rows.append(row)
    return rows

print(generate(5))