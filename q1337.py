from dataclasses import dataclass


def kWeakestRows(mat: list[list[int]], k: int) -> list[int]:
    def count_soldiers(row):
        count = 0
        for v in row:
            if v == 1:
                count += 1
            else:
                break
        return count
    
    num_soldiers = []
    for i, row in enumerate(mat):
        num_soldiers.append((count_soldiers(row), i))
    num_soldiers.sort(key = lambda count_index : count_index[0])
    arr = [num_soldiers[i][1] for i in range(k)]
    return arr


def kWeakestRows(mat, k):
    def count(row):
        count = 0
        for v in row:
            if v == 1:
                count += 1
            else:
                break
        return count
    counts = []
    for row in mat:
        counts.append(count(row))
    print(counts)
    arr = [[-1] for i in range(max(counts) + 1)]
    print(arr)
    for i, c in enumerate(counts):
        arr[c].append(i)
    print(arr)
    ret_arr = []
    for row in arr:
        for val in row:
            if val != -1:
                ret_arr.append(val)  
    print(ret_arr)
    return ret_arr[:k]


print(kWeakestRows(

[[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
,3))
