class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gram_map = defaultdict(list)

        for n in strs:
            gram_map[tuple(sorted(n))].append(n)
        return list(gram_map.values())
