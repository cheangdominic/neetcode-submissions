class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_str = ""

        for c in s:
            if c.isalnum():
                alpha_str += c.lower()
        return alpha_str == alpha_str[::-1]