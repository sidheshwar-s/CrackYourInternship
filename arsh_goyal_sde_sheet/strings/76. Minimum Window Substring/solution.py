class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        target, source = Counter(t), Counter()
        have, need, resultLen = 0, len(target), inf
        result, left = (0, 0), 0
        
        for right, c in enumerate(s):
            source[c] += 1
            if c in target and source[c] == target[c]:
                have += 1
            while have == need:
                if resultLen > (right - left + 1):
                    resultLen = right - left + 1
                    result = (left, right+1)
                source[s[left]] -= 1
                if s[left] in target and source[s[left]] < target[s[left]]:
                    have -= 1
                left += 1
        left, right = result
        return s[left: right]