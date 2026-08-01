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
            while s[index] != "#" and index < len(s):
                print(s[index])
                num += s[index]
                index += 1

            index += 1
            length = int(num)

            part = ""
            while length > 0:
                part += s[index]
                index += 1
                length -= 1
            res.append(part)
        return res
