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

def numIslands(grid: list[list[str]]) -> int:
    islands = 0
    checked = set()            
    def check(i, j, island_id):
        if grid[i][j] == '1' and (i, j) not in checked:
            checked.add((i, j))
            for neighbour in neighbours(i, j, len(grid), len(grid[0])):
                check(neighbour[0], neighbour[1], island_id)
        
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1' and (i, j) not in checked:
                islands += 1
                check(i, j, islands)
    return islands


print(numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

print(numIslands(
    [['0', '1', '1', '1', '1', '1', '0'],
    ['0', '1', '0', '0', '0', '1', '0'],
    ['0', '1', '0', '1', '0', '1', '0'],
    ['0', '1', '0', '1', '0', '1', '0'],
    ['0', '1', '0', '0', '0', '1', '0'],
    ['0', '1', '1', '1', '1', '1', '0']]
))
# print(neighbours(1, 1, 3, 3))