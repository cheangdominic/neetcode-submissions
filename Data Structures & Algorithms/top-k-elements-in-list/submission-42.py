class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        freq_buckets = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        for n, c in freq_map.items():
            freq_buckets[c].append(n)
        
        res = []
        for i in range(len(freq_buckets) - 1, -1, -1):
            for n in freq_buckets[i]:
                res.append(n)
                if len(res) >= k:
                    return res



