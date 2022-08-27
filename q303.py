class NumArray:
    def __init__(self, nums) -> None:
        self.nums = nums
    
    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left, right + 1):
            sum += self.nums[i]
        return sum