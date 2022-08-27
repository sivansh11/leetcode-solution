from cmath import sin
from functools import reduce


def singleNumber(nums):
    bools = {}
    for num in nums:
        if num in bools:
            bools[num] = True
        else:
            bools[num] = False
    for num in bools.keys():
        if not bools[num]:
            return num




a = 5
b = 0

# a ^ 0 = a
# a ^ a = 0
lis = [15, 2, 4, 3, 2, 3, 15]
print(15 ^ 2 ^ 4 ^ 3 ^ 2 ^ 3 ^ 15)
print(reduce(lambda a, b: a ^ b, lis))

