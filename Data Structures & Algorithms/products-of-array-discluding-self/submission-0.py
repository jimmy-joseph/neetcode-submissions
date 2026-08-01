class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = 1
        res = []
        for num in nums:
            ans *= num
        
        for index, num in enumerate(nums):
            if num == 0:
                ans2 = 1
                for index2, num2 in enumerate(nums):
                    if index != index2:
                        ans2 *= num2
                res.append(ans2)
            else:
                res.append(ans // num)
        
        return res