def summaryRanges(nums):
    if not nums:
        return []
    ret_lis = []
    index = 0
    while True:   
        single = True
        start = nums[index]
        curr = start
        for i in range(index + 1, len(nums)):
            end = nums[i]
            if curr + 1 == end:
                single = False
                curr += 1
                continue
            elif single:
                ret_lis.append(str(start))
            else:
                ret_lis.append(str(start) + '->' + str(curr))
            index = i
            break
        else:
            if single:
                ret_lis.append(str(start))
            else:
                ret_lis.append(str(start) + '->' + str(curr))
            index = len(nums)
        if index >= len(nums):
            return ret_lis


        


print(summaryRanges([0,1,2,4,5,7]))