class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)

        for num in nums:
            hm[num] += 1

        sorted_desc = dict(sorted(hm.items(), key=lambda x: x[1], reverse=True))
        first = islice(sorted_desc.items(), k)

        solution = []
        for key, value in first:
            solution.append(key)

        return solution