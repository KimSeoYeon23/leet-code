class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for string in s:
            if string in valid.values():
                stack.append(string)
            else:
                if stack and valid[string] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True