class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # for constant space just store the prev, and current of left and right respectively and use that to calculate the next ones
        left = []
        init_right = []
        length = len(nums)

        for index in range(length):
            if index == 0:
                left.append(nums[index])
                init_right.append(nums[length-(index+1)])
            else:
                left.append(nums[index] * left[index-1])
                init_right.append(nums[length-(index+1)] * init_right[index-1])

        right = init_right[::-1]

        res = []
        for index, num in enumerate(nums):
            if index == 0:
                res.append(right[1])
                continue
            if index == (len(nums) - 1):
                res.append(left[index-1])
                continue
            res.append(left[index-1] * right[index + 1])

        return res

