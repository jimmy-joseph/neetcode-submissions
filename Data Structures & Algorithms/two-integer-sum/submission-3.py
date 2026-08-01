class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in solution:
                return [solution[diff], i]
            solution[n] = i