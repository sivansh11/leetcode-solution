from timer import timeit

@timeit
def moveZeroes_1(nums):
    zero_index = -1
    for i in range(len(nums)):
        if nums[i] == 0:
            if zero_index == -1 or nums[zero_index] != 0:
                zero_index = i
        else:
            if zero_index != -1:
                nums[zero_index] = nums[i]
                nums[i] = 0
                index = zero_index
                while index <= len(nums):
                    if nums[index + 1] == 0:
                        zero_index = index + 1
                        break
                    else:
                        index += 1                


@timeit
def moveZeroes_2(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=i+1
        while j<len(nums):
            if nums[i]==0:
                if nums[j]!=0:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
                    j+=1
                else:
                    j+=1
            else:
                i+=1
                j+=1
        return nums

@timeit
def moveZeroes_3(nums: list):
    i = 0
    for num in nums:
        if num != 0:
            nums[i] = num
            i += 1
    for j in range(i, len(nums)):
        nums[j] = 0

@timeit
def moveZeroes_4(nums):
    last=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[last],nums[i]=nums[i],nums[last]
            last+=1


nums = [0,1,0,3,12]
moveZeroes_1(nums)
nums = [0,1,0,3,12]
moveZeroes_2(nums)
nums = [0,1,0,3,12]
moveZeroes_3(nums)
nums = [0,1,0,3,12]
moveZeroes_4(nums)
print(nums)