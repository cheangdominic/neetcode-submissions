class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outDict = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in outDict:
                outDict[key] = []
            outDict[key].append(word)
        return list(outDict.values())