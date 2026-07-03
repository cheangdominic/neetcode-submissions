class Solution:
    def isPalindrome(self, s: str) -> bool:
        optimized_str = ""

        for c in s:
            if c.isalnum():
                optimized_str += c.lower()
        return optimized_str == optimized_str[::-1]