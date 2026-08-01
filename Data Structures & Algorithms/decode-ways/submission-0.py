class Solution:
    def numDecodings(self, s: str) -> int:
        length = len(s)

        dp = [0] * (length + 1)
        if s[0] != 0:
            print(s[0])
            dp[0] = 1

        for i in range (1, length+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            if i >= 2:
                input = int(s[i-2:i])
                if 10 <= input <= 26:
                    dp[i] += dp[i-2]

        for i in dp:
            print(i)
        return dp[length]