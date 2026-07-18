class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq_map = {}
        freq_list = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        for n, c in freq_map.items():
            freq_list[c].append(n)

        for i in range(len(freq_list) - 1, -1, -1):
            for n in freq_list[i]:
                res.append(n)
                if len(res) >= k:
                    return res
