class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            alpha_count = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                alpha_count[index] += 1
            res[tuple(alpha_count)].append(s)
        
        return list(res.values())