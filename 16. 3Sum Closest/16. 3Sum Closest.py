class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

        nums = sorted(nums)

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                distance = abs(total - target)

                if total == target:
                    return total

                if total < target:
                    left += 1
                else:
                    right -= 1