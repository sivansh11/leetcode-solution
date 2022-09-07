def countKDifference(nums: list[int], k: int) -> int:
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j >= i:
                break
            if abs(nums[i] - nums[j]) == k:
                count += 1
    return count

assert countKDifference(
[7,7,8,3,1,2,7,2,9,5], 6) == 6