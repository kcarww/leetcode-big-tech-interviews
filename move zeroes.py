class Solution(object):
    def moveZeroes(self, nums):
        lastZero = 0
        for index, item in enumerate(nums):
            if nums[index] != 0:
                aux = nums[lastZero]
                nums[lastZero] = nums[index]
                nums[index] = aux
                lastZero += 1
        return nums
