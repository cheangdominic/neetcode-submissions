class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0  
        i = 0
        for n in num_set:
            i = n
            curr_streak = 1
            while i + 1 in num_set:
                curr_streak += 1
                i += 1
            longest_streak = max(longest_streak, curr_streak)
        return longest_streak
