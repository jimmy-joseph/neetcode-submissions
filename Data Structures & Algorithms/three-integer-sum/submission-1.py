class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            target = -nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[l] + nums[r]

                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    res.append([-target, nums[l], nums[r]])
                    
                    l += 1
                    r -= 1

                    while (nums[l] == nums[l-1]) and l < r:
                        l += 1
                    while (nums[r] == nums[r+1]) and l < r:
                        r -= 1

        return res
        