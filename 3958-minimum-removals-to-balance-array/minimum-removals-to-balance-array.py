class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        right = 0
        max_window = 1
        for left in range(len(nums)):
            while (right < len(nums) and nums[right] <= nums[left] * k):
                max_window = max(max_window, right - left + 1)
                right += 1
        return len(nums) - max_window

