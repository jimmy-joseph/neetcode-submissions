class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lcs = defaultdict(lambda: 0)
        res = 0
        
        for num in nums:
            if lcs[num] != 0:
                continue

            lcs[num] = 1
            prefix = 0
            suffix = 0
            
            if lcs[num - 1] >= 1:
                prefix = lcs[num - 1]
                lcs[num] += lcs[num - 1]
            
            if lcs[num + 1] >= 1:
                suffix = lcs[num + 1]
                lcs[num] += lcs[num + 1]

            for i in range(num - prefix, num + suffix + 1):
                lcs[i] = lcs[num]

            res = max(res, lcs[num])
                
        return res
