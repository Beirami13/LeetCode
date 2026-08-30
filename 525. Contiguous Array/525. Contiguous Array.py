from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        n = {0: -1}
        l = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                count -= 1

            if count in n:
                length = i - n[count]
                l = max(l, length)
            else:
                n[count] = i

        return l