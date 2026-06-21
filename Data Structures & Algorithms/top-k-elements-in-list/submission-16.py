class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts_map = {}
        bucket_array = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            counts_map[n] = counts_map.get(n, 0) + 1

        for key, value in counts_map.items():
            bucket_array[value].append(key)

        res = []
        for s in range(len(bucket_array)-1, -1, -1):
            for c in bucket_array[s]:
                res.append(c)
                if len(res) >= k:
                    return res