class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lcs = defaultdict(lambda: 0)
        res = 0
        
        for num in nums:
            if lcs[num] != 0:
                continue

            lcs[num] = lcs[num - 1] + lcs[num + 1] + 1
            lcs[num - lcs[num - 1]] = lcs[num]
            lcs[num + lcs[num + 1]] = lcs[num]

            res = max(res, lcs[num])
                
        return res
