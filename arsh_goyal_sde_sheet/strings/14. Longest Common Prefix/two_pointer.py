class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        small = min(strs, key = len)
        for i, c in enumerate(small):
            for s in strs:
                if c != s[i]:
                    return small[:i]
        return small