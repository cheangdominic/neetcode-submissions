class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gram_map = {}

        for n in strs:
            key = ''.join(sorted(n))
            if key not in gram_map:
                gram_map[key] = [n]
            else:
                gram_map[key].append(n)
        return list(gram_map.values())
