class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    
    def smallestWindow(self, s, t):
        from collections import Counter
        target = Counter(t)
        source = Counter()
        have, need = 0, len(target)
        left, result, resultLen = 0, [0, 0], float('inf')
        for right, c in enumerate(s):
            source[c] += 1
            if c in target and target[c] == source[c]:
                have += 1
            while have == need:
                if (right - left + 1) < resultLen:
                    resultLen = right - left + 1
                    result = [left, right+1]
                source[s[left]] -= 1
                if s[left] in target and source[s[left]] < target[s[left]]:
                    have -= 1
                left += 1
        
        l, r = result
        return s[l: r] if resultLen != float('inf') else -1