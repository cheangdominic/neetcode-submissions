class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gram_map = defaultdict(list)

        for n in strs:
            key = ''.join(sorted(n))
            gram_map[key].append(n)
        return list(gram_map.values())
