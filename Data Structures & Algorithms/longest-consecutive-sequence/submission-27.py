class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_streak = 0

        for n in nums_set:
            j = n + 1
            curr_streak = 1
            while j in nums_set:
                curr_streak += 1
                j += 1
            longest_streak = max(curr_streak, longest_streak)
        return longest_streak