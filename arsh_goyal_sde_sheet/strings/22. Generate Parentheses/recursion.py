class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recurse(s, open, close):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if open < n: recurse(s + "(", open+1, close)
            if close < open: recurse(s + ")", open, close+1)
        
        ans = []
        recurse("", 0, 0)
        return ans
                