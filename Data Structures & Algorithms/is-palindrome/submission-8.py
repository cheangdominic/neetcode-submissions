class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaStr = ""

        for c in s:
            if c.isalnum():
                alphaStr += c.lower()
        
        return alphaStr == alphaStr[::-1]