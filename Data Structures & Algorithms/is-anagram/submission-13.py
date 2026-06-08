class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
            CountS, CountT = {}, {}

            for n in range(len(s)):
                CountS[s[n]] = 1 + CountS.get(s[n], 0)
                CountT[t[n]] = 1 + CountT.get(t[n], 0)
            for c in CountS:
                if CountS[c] != CountT.get(c, 0):
                    return False
            
            return True