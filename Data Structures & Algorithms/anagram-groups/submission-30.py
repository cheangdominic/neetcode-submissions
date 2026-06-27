class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gram_map = defaultdict(list)

        for s in strs:
            alpha_list = [0] * 26
            for c in s:
                alpha_list[ord(c) - ord('a')] += 1
            gram_map[tuple(alpha_list)].append(s)

        return list(gram_map.values())