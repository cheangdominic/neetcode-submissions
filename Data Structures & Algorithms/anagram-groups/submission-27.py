class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = defaultdict(list)
        alpha_frequency = [0] * 26

        for s in strs:
            alpha_frequency = [0] * 26
            for c in s:
                index = ord(c) - ord('a') # a = 0 b = 1 c = 2 etc.
                alpha_frequency[index] += 1
            word_map[tuple(alpha_frequency)].append(s)
        
        return list(word_map.values())

