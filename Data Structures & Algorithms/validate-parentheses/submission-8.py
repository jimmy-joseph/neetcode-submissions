class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {
            "(": ")",
            "{": "}",
            "[": "]" 
        }

        for char in s:
            if char in valid:
                stack.append(valid[char])
            elif len(stack) > 0 and char == stack[-1]:
                stack.pop()
            else:
                return False
        
        if len(stack) > 0:
            return False

        return True