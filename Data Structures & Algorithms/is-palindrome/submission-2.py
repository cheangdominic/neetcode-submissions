class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaStr = ""

        for c in s:
            if c.isalnum():
                alphaStr += c.lower()
            
        return alphaStr.lower() == alphaStr[::-1].lower()