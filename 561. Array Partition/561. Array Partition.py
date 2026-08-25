class Solution(object):
    def arrayPairSum(self, nums):
        nums = nums.sort()
        sum = 0
        for num in nums:
            if nums.index(num)%2==0:
                sum = sum + num
        print(sum)
