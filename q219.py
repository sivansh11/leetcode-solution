from time import time
import timer

@timer.timeit
def containsNearbyDuplicate_1(nums, k):
    num_dict = {}
    for i in range(len(nums)):
        if nums[i] in num_dict:
            if i - num_dict[nums[i]] <= k:
                return True
        num_dict[nums[i]] = i
    return False

@timer.timeit
def containsNearbyDuplicate_2(nums, k):
    num_dict = dict()
    num_set = set()
    for i, num in enumerate(nums):
        if num in num_dict:
            num_dict[num].append(i)
        else:
            num_dict[num] = [i]
        num_set.add(num)

    for num in num_set:
        for i in range(len(num_dict[num])):
            for j in range(i + 1, len(num_dict[num])):
                index1 = num_dict[num][i]
                index2 = num_dict[num][j]
                if abs(index1 - index2) <= k:
                    return True
    return False

@timer.timeit
def containsNearbyDuplicate_3(nums, k):
    dict={}
    for i in range(len(nums)):
        if nums[i] in dict:
            dict[nums[i]].append(i)
        elif nums[i] not in dict:
            dict[nums[i]]=[i]
    for j in dict:
        for l in range(1,len(dict[j])):
            if dict[j][l]-dict[j][l-1]<=k:
                return True
    return False

