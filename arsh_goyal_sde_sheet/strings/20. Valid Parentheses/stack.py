class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(":")", "[":"]", "{":"}"}
        for c in s:
            if c not in pairs:
                if not stack: return False
                open_bracket = stack[-1]
                if pairs[open_bracket] != c: return False
                else: stack.pop()
            else:
                stack.append(c)
        
        return stack == []