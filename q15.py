from timer import timeit

@timeit
def threeSum_1(nums):
    # all three indices must not be equal
    # nums[i] + nums[j] + nums[k] = 0    
    ans = set()
    nums_dict = {}
    for i, num in enumerate(nums):
        nums_dict[num] = i

    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            nums_k = -(nums[i] + nums[j])
            if nums_k in nums_dict:
                if nums_dict[nums_k] not in (i, j): 
                    lis = [nums[i], nums[j], nums_k]
                    lis.sort()
                    ans.add(tuple(lis))
    return ans


@timeit
def threeSum_2(nums):
    nums.sort()
    ans = set()
    i, j, k = 0, 1, 2
    while True:
        if nums[i] >= 0:
            break
    
        if nums[i] + nums[j] + nums[k] == 0:
            ans.add((nums[i], nums[j], nums[k]))
        k += 1
        if (k == len(nums)):
            j += 1
            k = j + 1
            if (j == len(nums) - 1):
                i += 1
                j = i + 1
                k = j + 1
    return ans

sum = 0
for i in range(500):
    sum += i

print(threeSum_1([-1,0,1,2,-1,-4]))
print(threeSum_2([-1,0,1,2,-1,-4]))