class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hm[num] += 1
        for num, value in hm.items():
            freq[value].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res