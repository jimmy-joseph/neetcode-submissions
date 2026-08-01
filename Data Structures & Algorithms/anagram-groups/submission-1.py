class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1st approach brute force
        # O(n^2) iteration time?

        count_map = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            count_map[tuple(count)].append(word)

        return list(count_map.values())

