class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # for constant space just store the prev, and current of left and right respectively and use that to calculate the next ones
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res

