def findDisappearedNumbers(nums):
    num_set = set(nums)
    return [i for i in range(1, len(nums) + 1) if i not in num_set]

# assert findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5,6]

print(findDisappearedNumbers([1,1]))