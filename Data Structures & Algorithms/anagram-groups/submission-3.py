class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gramMap = {}

        for n in strs:
            sortedWord = sorted(n)
            key = ''.join(sortedWord)
            if key not in gramMap:
                gramMap[key] = [n]
            else:
                gramMap[key].append(n)
        return list(gramMap.values())
