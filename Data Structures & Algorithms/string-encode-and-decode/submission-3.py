class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        num = ""
        index = 0
        res = []

        while index < len(s):
            num = ""
            while index < len(s) and s[index] != "#":
                num += s[index]
                index += 1

            index += 1
            length = int(num)

            res.append(s[index:index+length])
            index += length
        
        return res
