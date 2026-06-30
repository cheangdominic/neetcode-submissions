class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gram_map = defaultdict(list)

        for s in strs:
            alpha_arr = [0] * 26
            for c in s:
                alpha_arr[ord(c) - ord('a')] += 1
            gram_map[tuple(alpha_arr)].append(s)
        return list(gram_map.values())