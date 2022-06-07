class Solution:
    def validPalindrome(self, s: str) -> bool:
        is_palindrome = lambda s: s[::-1] == s
        left, right = 0, len(s)-1
        
        while left < right:
            if s[left] == s[right]:
                left, right = left + 1, right - 1
            else:
                return is_palindrome(s[left+1:right+1]) or is_palindrome(s[left:right])
        
        return True