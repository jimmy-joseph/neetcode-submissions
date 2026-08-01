class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1st approach brute force
        # O(n^2) iteration time?

        count_map = []

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            count_map.append(count)

        count_dict = defaultdict(list)

        for index, count in enumerate(count_map):
            count_dict[tuple(count)].append(index)

        solution = []
        for key, value in count_dict.items():
            entry = []
            for x in value:
                entry.append(strs[x])
            solution.append(entry)

        return solution

