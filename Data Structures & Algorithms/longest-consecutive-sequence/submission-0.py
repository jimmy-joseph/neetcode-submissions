class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lcs = defaultdict(lambda: 0)
        res = 0
        
        for num in nums:
            if lcs[num] != 0:
                continue

            lcs[num] = 1

            if lcs[num - 1] >= 1:
                lcs[num] += lcs[num - 1]
            
            if lcs[num + 1] >= 1:
                lcs[num] += lcs[num + 1]
            
            print(lcs[num])
            res = max(res, lcs[num])

            i = num
            while lcs[i - 1] < lcs[i] and lcs[i - 1] >= 1:
                    lcs[i - 1] = lcs[i]
                    i -= 1

            i = num
            while lcs[i + 1] < lcs[i] and lcs[i + 1] >= 1:
                    lcs[i + 1] = lcs[i]
                    i += 1
                
        return res
