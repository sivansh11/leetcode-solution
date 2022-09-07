def neighbours(i, j, max_i, max_j):
    ret_lis = []

    if max_i != 1:
        if i == 0:
            ret_lis.append((i + 1, j))
        elif i == max_i - 1:
            ret_lis.append((i - 1, j))
        else:
            ret_lis.append((i + 1, j))
            ret_lis.append((i - 1, j))
    if max_j != 1:
        if j == 0:
            ret_lis.append((i, j + 1))
        elif j == max_j - 1:
            ret_lis.append((i, j - 1))
        else:
            ret_lis.append((i, j + 1))
            ret_lis.append((i, j - 1))

    return ret_lis


def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:
    can_flow_to_map = {}
    to_check = set()

    def get_oceans_to_flow_to(i, j, max_i, max_j):
        if (i, j) in can_flow_to_map:
            return can_flow_to_map[(i, j)]
        can_flow_to = set()
        if i - 1 == -1 or j - 1 == -1:
            can_flow_to.add(1)
        if i + 1 == max_i or j + 1 == max_j:
            can_flow_to.add(2)

        to_check.add((i, j))
        for n_i, n_j in neighbours(i, j, max_i, max_j):
            if (n_i, n_j) in to_check:
                continue
            neighbour_can_flow_to = get_oceans_to_flow_to(n_i, n_j, max_i, max_j)
            can_flow_to.union(neighbour_can_flow_to)
        can_flow_to_map[(i, j)] = can_flow_to
        to_check.remove((i, j))
        return can_flow_to

    ret_lis = []
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            if len(get_oceans_to_flow_to(i, j, len(heights), len(heights[0]))) == 2:
                ret_lis.append((i, j))

    print(ret_lis)
    return ret_lis



assert pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]) == [
    [0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
