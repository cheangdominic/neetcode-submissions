class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}
        for n in nums:
            numsMap[n] = 1 + numsMap.get(n, 0)
        
        sortedMap = sorted(numsMap.items(), key = lambda x : x[1], reverse=True)
        return [item[0] for item in sortedMap[:k]]