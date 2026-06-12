class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        best_streak = 1

        for i, n in enumerate(nums):
            if n - 1 in nums:
                continue
            streak = 1
            next_streak = n + 1
            while next_streak in nums:
                if not next_streak - 2 in nums:
                    nums.remove(next_streak)
                streak += 1
                if streak > best_streak:
                    best_streak = streak
                next_streak += 1
        return best_streak