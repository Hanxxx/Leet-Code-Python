"""
Constant space solution
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right_product = [1] * n
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]
        result = right_product
        left = 1
        for i in range(1, n):
            left *= nums[i - 1]
            result[i] = result[i] * left
        return result