"""
This problem is a special case of partition in 3-way quick sort.
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero = -1
        two = n
        i = 0
        while i < two:
            if nums[i] == 0:
                nums[zero + 1], nums[i] = nums[i], nums[zero + 1]
                zero += 1
                i += 1
            elif nums[i] == 2:
                nums[two - 1], nums[i] = nums[i], nums[two - 1]
                two -= 1
            else:
                i += 1